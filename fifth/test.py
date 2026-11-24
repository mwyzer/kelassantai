# ============================================================
#  PRAKTIK PERTEMUAN 5 — Membangun REST API dengan Flask
#  CRUD API Catatan (Notes) — menggunakan Blueprint (in-memory)
#  Course : Python Fullstack AI Engineer — Kelas Santai
#  Cara menjalankan :
#    1) Aktifkan venv  &  pip install flask
#    2) python praktik_pertemuan_05.py
#    3) Uji dengan browser (GET) atau Postman/Thunder Client (POST/PUT/DELETE)
#       Base URL: http://127.0.0.1:5000
# ------------------------------------------------------------
#  REST API = sekumpulan endpoint yang mengikuti pola:
#    GET    /notes        -> baca semua catatan
#    GET    /notes/<id>   -> baca satu catatan
#    POST   /notes        -> tambah catatan baru
#    PUT    /notes/<id>   -> perbarui catatan
#    DELETE /notes/<id>   -> hapus catatan
#  Semua data dikirim/diterima dalam format JSON.
#  CATATAN: data disimpan di memori (list) -> hilang saat server
#  dimatikan. Menyambung ke database sungguhan dibahas Pertemuan 6.
# ============================================================

from flask import Blueprint, Flask, jsonify, request

app = Flask(__name__)

# Mendefinisikan Blueprint untuk modul Notes dengan prefix /notes
notes_bp = Blueprint("notes", __name__, url_prefix="/notes")

# "Database" sementara di memori + penghasil id sederhana
notes = [
    {"id": 1, "judul": "Belajar Flask", "isi": "Membuat REST API pertama"},
    {"id": 2, "judul": "Tugas", "isi": "Kerjakan api_biodata.py"},
]
next_id = 3


# ------------------------------------------------------------
# HELPER — mencari catatan berdasarkan id
# ------------------------------------------------------------
def cari_note(note_id):
    for n in notes:
        if n["id"] == note_id:
            return n
    return None


# ------------------------------------------------------------
# READ — semua catatan   (GET /notes)
# ------------------------------------------------------------
# Dukungan query parameter opsional: /notes?cari=flask
# request.args mengambil query string dari URL.
@notes_bp.route("/", methods=["GET"])
def get_notes():
    kata = request.args.get("cari")  # None bila tidak ada
    if kata:
        hasil = [n for n in notes if kata.lower() in n["judul"].lower()]
        return jsonify(hasil), 200
    return jsonify(notes), 200


# ------------------------------------------------------------
# READ — satu catatan   (GET /notes/<id>)
# ------------------------------------------------------------
@notes_bp.route("/<int:note_id>", methods=["GET"])
def get_note(note_id):
    note = cari_note(note_id)
    if note is None:
        return jsonify({"error": "Notes is not found"}), 404
    return jsonify(note), 200


# ------------------------------------------------------------
# CREATE — tambah catatan   (POST /notes)
# ------------------------------------------------------------
# Data baru dikirim client di request body (JSON).
# request.get_json() mengubahnya menjadi dictionary Python.
@notes_bp.route("/", methods=["POST"])
def create_note():
    global next_id
    data = request.get_json()

    # Validasi sederhana: judul & isi wajib ada
    if not data or "judul" not in data or "isi" not in data:
        return jsonify({"error": "judul dan isi wajib diisi"}), 400

    note_baru = {"id": next_id, "judul": data["judul"], "isi": data["isi"]}
    notes.append(note_baru)
    next_id += 1
    return jsonify(note_baru), 201  # 201 Created


# ------------------------------------------------------------
# UPDATE — perbarui catatan   (PUT /notes/<id>)
# ------------------------------------------------------------
@notes_bp.route("/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    note = cari_note(note_id)
    if note is None:
        return jsonify({"error": "Catatan tidak ditemukan"}), 404

    data = request.get_json() or {}
    # Perbarui hanya field yang dikirim (judul dan/atau isi)
    note["judul"] = data.get("judul", note["judul"])
    note["isi"] = data.get("isi", note["isi"])
    return jsonify(note), 200


# ------------------------------------------------------------
# DELETE — hapus catatan   (DELETE /notes/<id>)
# ------------------------------------------------------------
@notes_bp.route("/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = cari_note(note_id)
    if note is None:
        return jsonify({"error": "Catatan tidak ditemukan"}), 404

    notes.remove(note)
    return jsonify({"pesan": f"Catatan {note_id} dihapus"}), 200


# Daftarkan Blueprint ke aplikasi Flask utama
app.register_blueprint(notes_bp)


# ------------------------------------------------------------
# Beranda kecil sebagai petunjuk
# ------------------------------------------------------------
@app.route("/")
def beranda():
    return jsonify({
        "pesan": "API Catatan Kelas Santai",
        "endpoint": {
            "GET /notes": "semua catatan (opsional ?cari=kata)",
            "GET /notes/<id>": "satu catatan",
            "POST /notes": "tambah (body: judul, isi)",
            "PUT /notes/<id>": "perbarui",
            "DELETE /notes/<id>": "hapus",
        },
    })


if __name__ == "__main__":
    app.run(debug=True)