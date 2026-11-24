# ============================================================
#  PRAKTIK PERTEMUAN 6 — Database & SQLAlchemy ORM
#  CRUD API Catatan tersambung DATABASE (SQLite)
#  Course : Python Fullstack AI Engineer — Kelas Santai
#  Cara menjalankan :
#    1) Aktifkan venv
#    2) pip install flask flask-sqlalchemy
#    3) python praktik_pertemuan_06.py
#       (file database "notes.db" otomatis dibuat di folder ini)
#    4) Uji endpoint dengan Postman / Thunder Client
#       Base URL: http://127.0.0.1:5000
# ------------------------------------------------------------
#  BEDA BESAR dari Pertemuan 5:
#    Pertemuan 5 -> data di list memori (HILANG saat server mati)
#    Pertemuan 6 -> data di DATABASE (TETAP ada walau server mati)
#
#  ORM (Object-Relational Mapping): kita bekerja dengan OBJECT
#  Python (class Note), SQLAlchemy yang menerjemahkannya menjadi
#  perintah SQL ke database. Jadi kita jarang menulis SQL manual.
# ============================================================

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfigurasi database. Untuk development kita pakai SQLite
# (satu file, tanpa server terpisah). Di production biasanya
# diganti PostgreSQL — cukup mengubah URI ini (dibahas Modul 4).
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ------------------------------------------------------------
# MODEL — cetakan tabel di database
# ------------------------------------------------------------
# Ingat OOP (Pertemuan 3): ini class biasa, tapi mewarisi db.Model
# sehingga SQLAlchemy tahu ini adalah sebuah TABEL.
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)          # kunci utama, auto
    judul = db.Column(db.String(100), nullable=False)     # wajib diisi
    isi = db.Column(db.String(500), nullable=False)

    # Helper: mengubah object baris menjadi dictionary (untuk JSON)
    def to_dict(self):
        return {"id": self.id, "judul": self.judul, "isi": self.isi}


# ------------------------------------------------------------
# READ — semua catatan   (GET /notes)
# ------------------------------------------------------------
@app.route("/notes", methods=["GET"])
def get_notes():
    kata = request.args.get("cari")
    if kata:
        # query dengan filter LIKE (mengandung kata)
        hasil = Note.query.filter(Note.judul.ilike(f"%{kata}%")).all()
    else:
        hasil = Note.query.all()                          # SELECT * FROM note
    return jsonify([n.to_dict() for n in hasil]), 200


# ------------------------------------------------------------
# READ — satu catatan   (GET /notes/<id>)
# ------------------------------------------------------------
@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    note = Note.query.get(note_id)                        # cari by primary key
    if note is None:
        return jsonify({"error": "Catatan tidak ditemukan"}), 404
    return jsonify(note.to_dict()), 200


# ------------------------------------------------------------
# CREATE — tambah catatan   (POST /notes)
# ------------------------------------------------------------
@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()
    if not data or "judul" not in data or "isi" not in data:
        return jsonify({"error": "judul dan isi wajib diisi"}), 400

    note = Note(judul=data["judul"], isi=data["isi"])     # buat object
    db.session.add(note)                                  # tandai untuk disimpan
    db.session.commit()                                   # SIMPAN ke database
    return jsonify(note.to_dict()), 201


# ------------------------------------------------------------
# UPDATE — perbarui catatan   (PUT /notes/<id>)
# ------------------------------------------------------------
@app.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    note = Note.query.get(note_id)
    if note is None:
        return jsonify({"error": "Catatan tidak ditemukan"}), 404

    data = request.get_json() or {}
    note.judul = data.get("judul", note.judul)
    note.isi = data.get("isi", note.isi)
    db.session.commit()                                   # simpan perubahan
    return jsonify(note.to_dict()), 200


# ------------------------------------------------------------
# DELETE — hapus catatan   (DELETE /notes/<id>)
# ------------------------------------------------------------
@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = Note.query.get(note_id)
    if note is None:
        return jsonify({"error": "Catatan tidak ditemukan"}), 404

    db.session.delete(note)
    db.session.commit()
    return jsonify({"pesan": f"Catatan {note_id} dihapus"}), 200


@app.route("/")
def beranda():
    return jsonify({"pesan": "API Catatan (Database) — Kelas Santai"})


# ------------------------------------------------------------
# Membuat tabel di database saat pertama kali dijalankan.
# db.create_all() membaca semua model (class) lalu membuat
# tabel yang belum ada. Untuk perubahan struktur tabel di
# project nyata, gunakan Flask-Migrate (lihat modul).
# ------------------------------------------------------------
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)


# ============================================================
# BUKTI DATA PERSISTEN (coba ini di kelas!)
# ------------------------------------------------------------
#  1) Jalankan server, POST beberapa catatan lewat Postman.
#  2) Matikan server (Ctrl+C).
#  3) Jalankan lagi, GET /notes -> catatan MASIH ADA.
#     (Berbeda dengan Pertemuan 5 yang datanya hilang.)
#  4) Buka file notes.db — itu database sungguhan di disk.
# ------------------------------------------------------------
# CATATAN tentang Flask-Migrate (migrasi struktur tabel):
#   pip install flask-migrate
#   flask db init      # sekali di awal
#   flask db migrate -m "buat tabel note"
#   flask db upgrade   # menerapkan perubahan ke database
#   Dipakai saat MENGUBAH struktur tabel (tambah kolom, dsb)
#   tanpa menghapus data yang sudah ada.
# ------------------------------------------------------------
# TUGAS MANDIRI (file baru: api_buku_db.py)
# ------------------------------------------------------------
#  Ubah tugas api_buku.py (Pertemuan 5) agar tersambung DATABASE:
#    - Model Buku(db.Model): id, judul, penulis, tahun
#    - CRUD lengkap: GET semua, GET satu, POST, PUT, DELETE
#      menggunakan db.session (add/commit/delete) & Buku.query
#    - Validasi POST (judul & penulis wajib) -> 400
#    - Buktikan data tetap ada setelah server dimatikan
#    - requirements.txt: flask, flask-sqlalchemy
#  Kumpulkan folder/zip atau link GitHub via LMS sebelum Pertemuan 7.
# ============================================================
