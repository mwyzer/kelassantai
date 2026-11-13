import logging
import subprocess
import sys
import time
from threading import Event
from pathlib import Path

from watchdog.events import FileSystemEvent, LoggingEventHandler
from watchdog.observers import Observer

ROOT_DIR = Path(__file__).resolve().parent
APP_DIR = ROOT_DIR / "kalkulator"


class RestartHandler(LoggingEventHandler):
    def __init__(self, restart_requested: Event) -> None:
        super().__init__()
        self.restart_requested = restart_requested

    def dispatch(self, event: FileSystemEvent) -> None:
        paths = [Path(event.src_path)]
        if event.dest_path:
            paths.append(Path(event.dest_path))

        if event.is_directory or any(
            "__pycache__" in path.parts or path.suffix == ".pyc" for path in paths
        ):
            return

        super().dispatch(event)
        if event.event_type in {"created", "deleted", "modified", "moved"}:
            self.restart_requested.set()


def start_server() -> subprocess.Popen[bytes]:
    return subprocess.Popen(
        [
            sys.executable,
            "-m",
            "flask",
            "--app",
            "kalkulator.app",
            "run",
            "--no-reload",
        ],
        cwd=ROOT_DIR,
    )


def stop_server(process: subprocess.Popen[bytes]) -> None:
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()


def main() -> int:
    if not APP_DIR.is_dir():
        raise FileNotFoundError(f"Application directory not found: {APP_DIR}")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    watch_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else APP_DIR
    if not watch_path.is_dir():
        raise NotADirectoryError(f"Watch path is not a directory: {watch_path}")

    restart_requested = Event()
    observer = Observer()
    observer.schedule(RestartHandler(restart_requested), str(watch_path), recursive=True)
    observer.start()
    server: subprocess.Popen[bytes] | None = None

    try:
        server = start_server()
        logging.info("Watching %s for changes. Press Ctrl+C to stop.", watch_path)
        while True:
            changed = restart_requested.wait(timeout=1)
            if server.poll() is not None:
                logging.error("Flask server exited with status %s.", server.returncode)
                return server.returncode if server.returncode is not None else 1

            if changed:
                time.sleep(0.25)
                restart_requested.clear()
                logging.info("Change detected; restarting Flask server.")
                stop_server(server)
                server = start_server()
    except KeyboardInterrupt:
        logging.info("Stopping Flask server.")
        return 0
    finally:
        observer.stop()
        observer.join()
        if server is not None and server.poll() is None:
            stop_server(server)


if __name__ == "__main__":
    raise SystemExit(main())
