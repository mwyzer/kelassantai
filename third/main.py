
# main.py

import json

from model import Siswa, SiswaBerprestasi
from database import simpan_json, muat_json


print("=" * 55)
print("DEMO 1 — OOP: CLASS, OBJECT, METHOD")
print("=" * 55)

budi = Siswa("Budi", 85)
andi = Siswa("Andi", 68)

print(f"Nama object budi: {budi.nama}")
print(budi.status())
print(andi.status())


print()
print("=" * 55)
print("DEMO 2 — INHERITANCE")
print("=" * 55)

sari = SiswaBerprestasi("Sari", 95)

print(f"Atribut nama diwarisi: {sari.nama}")
print(sari.status())


print()
print("=" * 55)
print("DEMO 3 — FILE I/O & JSON")
print("=" * 55)

contoh = {
    "nama": "Budi",
    "nilai": 85
}

with open("contoh.json", "w", encoding="utf-8") as f:
    json.dump(contoh, f, indent=2)

print("-> Data ditulis ke contoh.json")

with open("contoh.json", "r", encoding="utf-8") as f:
    hasil = json.load(f)

print(f"-> Data dibaca kembali: {hasil}")
print(f"-> Nama siswa: {hasil['nama']}")


print()
print("=" * 55)
print("MINI DATABASE SISWA — KELAS SANTAI")
print("=" * 55)

# 1. Memuat database lama
daftar = muat_json()

# 2. Jika database kosong, buat data awal
if not daftar:
    daftar = [
        Siswa("Budi", 85),
        Siswa("Sari", 92),
        Siswa("Andi", 68)
    ]

    print("\nMengisi data awal...")

else:
    print(f"\nData lama ditemukan ({len(daftar)} siswa):")

    for siswa in daftar:
        print(f"- {siswa.status()}")

# 3. Menyimpan database
print()
simpan_json(daftar)

print("\nProgram selesai!")
print("Jalankan kembali untuk membuktikan data persisten.")
