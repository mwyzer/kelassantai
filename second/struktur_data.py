print()
print("=" * 50)
print("DEMO 3 — Struktur Data")
print("=" * 50)

# List [ ] : daftar berurutan, bisa diubah, index mulai dari 0
angka = [80, 75, 90, 85]
angka.append(95) # menambah item di akhir
angka.append(55)

print(f"List      : {angka}")
print(f"Item ke-0 : {angka[0]}")
print(f"Jumlah    : {len(angka)} item, totalnya {sum(angka)}")

# Dictionary { } : pasangan key -> value (fondasi format JSON!)
siswa = {"nama": "Budi", "nilai": 85}
siswa["kelas"] = "XII"           # menambah key baru
print(f"Dict      : {siswa}")
print(f"Ambil key : {siswa['nama']}")
print(f"Key aman  : {siswa.get('alamat')}")  # get() -> None, tidak error

# Tuple ( ) : seperti list tapi TIDAK bisa diubah (immutable)
koordinat = (-6.2, 106.8)
print(f"Tuple     : {koordinat}")

# Set { } : item unik, duplikat otomatis dibuang
hadir = {"Budi", "Sari", "Budi", "Andi"}
print(f"Set       : {hadir}")    # "Budi" hanya muncul sekali

