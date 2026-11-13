import json     # untuk File I/O format JSON
import os       # untuk cek apakah file sudah ada


# ============================================================
# BAGIAN A — DEMO KONSEP
# ============================================================

print("=" * 55)
print("DEMO 1 — OOP: class, object, method")
print("=" * 55)


class Siswa:
    """Cetakan (class) untuk membuat object siswa."""

    def __init__(self, nama, nilai):   # constructor: berjalan saat object dibuat
        self.nama = nama               # atribut object
        self.nilai = nilai

    def status(self):                  # method: function di dalam class
        if self.nilai >= 75:
            return f"{self.nama} LULUS (nilai {self.nilai})"
        return f"{self.nama} belum lulus (nilai {self.nilai})"


# Membuat object dari class
budi = Siswa("Budi", 85)
andi = Siswa("Andi", 68)

print(f"Nama object budi : {budi.nama}")
print(budi.status())
print(andi.status())
# Perhatikan: budi & andi punya data sendiri-sendiri, dari cetakan yang sama.


print()
print("=" * 55)
print("DEMO 2 — Inheritance (pewarisan)")
print("=" * 55)


class SiswaBerprestasi(Siswa):         # mewarisi semua dari Siswa
    def status(self):                  # meng-override method status()
        return f"{self.nama} JUARA! (nilai {self.nilai})"


sari = SiswaBerprestasi("Sari", 95)
print(f"Atribut nama diwarisi : {sari.nama}")
print(sari.status())                   # memakai versi baru


print()
print("=" * 55)
print("DEMO 3 — File I/O & JSON")
print("=" * 55)

contoh = {"nama": "Budi", "nilai": 85}

# MENULIS dictionary ke file JSON
with open("contoh.json", "w") as f:
    json.dump(contoh, f, indent=2)     # indent=2 -> rapi & mudah dibaca
print("-> data ditulis ke contoh.json")

# MEMBACA kembali dari file JSON
with open("contoh.json", "r") as f:
    hasil = json.load(f)
print(f"-> data dibaca kembali : {hasil}")
print(f"   ambil satu key       : {hasil['nama']}")
# JSON sangat mirip dictionary Python — inilah bahasa REST API nanti!
