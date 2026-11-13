# ============================================================
#  PRAKTIK PERTEMUAN 2 — Dasar Python II
#  Control Flow & Struktur Data
#  Course : Python Fullstack AI Engineer — Kelas Santai
#  Cara menjalankan :  python praktik_pertemuan_02.py
# ============================================================
#  File ini berisi 2 bagian:
#    BAGIAN A — DEMO  : contoh kecil tiap konsep (dibahas instruktur)
#    BAGIAN B — PRAKTIK: studi kasus "Pengolah Data Nilai Siswa"
#  Ubah-ubah angkanya, jalankan ulang, dan amati hasilnya!
# ============================================================


# ============================================================
# BAGIAN A — DEMO KONSEP
# ============================================================

print("=" * 50)
print("DEMO 1 — Percabangan if / elif / else")
print("=" * 50)

nilai = 85  # coba ganti jadi 70 atau 50, lalu jalankan ulang

if nilai >= 80:
    print(f"Nilai {nilai} -> Grade A")
elif nilai >= 60:
    print(f"Nilai {nilai} -> Grade B")
else:
    print(f"Nilai {nilai} -> Belum lulus")
# Ingat: titik dua (:) di akhir kondisi, isi blok menjorok 4 spasi.


print()
print("=" * 50)
print("DEMO 2 — Perulangan for & while")
print("=" * 50)

# for: mengulang untuk SETIAP item di dalam list
buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print(f"Saya suka {item}")

# for dengan range(n): mengulang n kali (0 sampai n-1)
for i in range(3):
    print(f"Putaran ke-{i}")

# while: mengulang SELAMA kondisi masih True
hitung_mundur = 3
while hitung_mundur > 0:
    print(f"Hitung mundur: {hitung_mundur}")
    hitung_mundur = hitung_mundur - 1  # WAJIB! tanpa ini = infinite loop
print("Meluncur!")


print()
print("=" * 50)
print("DEMO 3 — Struktur Data")
print("=" * 50)

# List [ ] : daftar berurutan, bisa diubah, index mulai dari 0
angka = [80, 75, 90, 85]
angka.append(95)                 # menambah item di akhir
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


print()
print("=" * 50)
print("DEMO 4 — Function & try/except")
print("=" * 50)

def sapa(nama):
    """Function dengan parameter, tanpa return (hanya menampilkan)."""
    print(f"Halo, {nama}!")

def kali_dua(x):
    """Function dengan return: MENGIRIM hasil keluar."""
    return x * 2

sapa("Kelas Santai")
hasil = kali_dua(21)
print(f"kali_dua(21) = {hasil}")

# try/except: jaring pengaman agar program tidak crash
teks = "abc"  # pura-puranya ini input pengguna; coba ganti jadi "42"
try:
    angka_input = int(teks)
    print(f"Berhasil dikonversi: {angka_input}")
except ValueError:
    print(f"'{teks}' bukan angka — program tetap jalan, tidak crash!")


# ============================================================
# BAGIAN B — PRAKTIK: PENGOLAH DATA NILAI SISWA
# ============================================================
# Studi kasus: hitung rata-rata kelas, filter siswa lulus,
# dan tampilkan ranking dari nilai tertinggi.
# ============================================================

# --- 1. Data: list berisi dictionary --------------------------
data_siswa = [
    {"nama": "Budi",  "nilai": 85},
    {"nama": "Sari",  "nilai": 92},
    {"nama": "Andi",  "nilai": 68},
    {"nama": "Dewi",  "nilai": 74},
    {"nama": "Rizky", "nilai": 84},
]
# Tantangan: tambahkan dirimu sendiri ke daftar ini!


# --- 2. Function: hitung rata-rata ----------------------------
def hitung_rata2(data):
    """Menjumlahkan semua nilai lalu membagi dengan jumlah siswa."""
    total = 0
    for siswa in data:
        total = total + siswa["nilai"]
    return total / len(data)


# --- 3. Function: filter siswa lulus --------------------------
def filter_lulus(data, batas):
    """Mengembalikan list siswa dengan nilai >= batas."""
    lulus = []
    for siswa in data:
        if siswa["nilai"] >= batas:
            lulus.append(siswa)
    return lulus


# --- 4. Function: ranking dari nilai tertinggi ----------------
def buat_ranking(data):
    """Mengurutkan siswa dari nilai tertinggi ke terendah."""
    return sorted(data, key=lambda s: s["nilai"], reverse=True)
    # sorted() membuat list baru yang terurut.
    # key=lambda s: s["nilai"] artinya: urutkan berdasarkan nilai.
    # reverse=True artinya: dari yang terbesar.


# --- 5. Program utama -----------------------------------------
print()
print("=" * 50)
print("LAPORAN NILAI KELAS — KELAS SANTAI")
print("=" * 50)

BATAS_LULUS = 75  # coba ubah batasnya, lalu jalankan ulang

rata2 = hitung_rata2(data_siswa)
print(f"\nJumlah siswa    : {len(data_siswa)}")
print(f"Rata-rata kelas : {rata2:.2f}")

print(f"\n-- Siswa LULUS (nilai >= {BATAS_LULUS}) --")
for siswa in filter_lulus(data_siswa, BATAS_LULUS):
    print(f"  {siswa['nama']:<8} : {siswa['nilai']}")

print("\n-- RANKING KELAS --")
ranking = buat_ranking(data_siswa)
peringkat = 1
for siswa in ranking:
    print(f"  #{peringkat} {siswa['nama']:<8} : {siswa['nilai']}")
    peringkat = peringkat + 1

print("\nSelesai! Coba ubah data/batas lulus di atas, lalu jalankan lagi.")

# ============================================================
# TUGAS MANDIRI (dikerjakan di file baru: kasir_mini.py)
# ------------------------------------------------------------
# Buat program kasir dengan menu berulang (while):
#   1. Tambah item (nama, harga, jumlah) -> simpan sebagai dict di list
#   2. Lihat daftar belanja
#   3. Checkout: tampilkan total belanja
#   4. Keluar
# Wajib: minimal 1 function, dictionary per item, dan try/except
# agar input harga/jumlah yang bukan angka tidak membuat crash.
# Kumpulkan via LMS / GitHub sebelum Pertemuan 3. Semangat!
# ============================================================
