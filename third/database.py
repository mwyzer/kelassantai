
# database.py

import json
from model import Siswa


FILE_DB = "siswa.json"


def simpan_json(daftar_siswa, nama_file=FILE_DB):
    """Menyimpan daftar object siswa ke JSON."""

    data = [s.to_dict() for s in daftar_siswa]

    with open(nama_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"-> {len(data)} siswa disimpan ke {nama_file}")


def muat_json(nama_file=FILE_DB):
    """Membaca JSON dan mengubahnya menjadi object Siswa."""

    try:
        with open(nama_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        return [Siswa.from_dict(d) for d in data]

    except FileNotFoundError:
        print(f"-> {nama_file} belum ada, mulai dengan data kosong.")
        return []

    except json.JSONDecodeError:
        print(f"-> File {nama_file} rusak atau format JSON tidak valid.")
        return []
