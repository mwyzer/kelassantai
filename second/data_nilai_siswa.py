# ============================================================
# BAGIAN B — PRAKTIK: PENGOLAH DATA NILAI SISWA
# ============================================================
# Studi kasus: hitung rata-rata kelas, filter siswa lulus,
# dan tampilkan ranking dari nilai tertinggi.
# ============================================================

# --- 1. Data: list berisi dictionary --------------------------
data_siswa = [
    {"nama": "Budi",  "nilai": 70, "kelas": "XII"},
    {"nama": "Sari",  "nilai": 60, "kelas": "XII"}, 
    {"nama": "Andi",  "nilai": 50, "kelas": "XII"},
    {"nama": "Dewi",  "nilai": 40, "kelas": "XII"}, 
    {"nama": "Rizky", "nilai": 30, "kelas": "XII"},
    {"nama": "Aris",  "nilai": 80, "kelas": "XII"}
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
print(f"\nJumlah siswa      : {len(data_siswa)}")
print(f"Kelas             : {data_siswa[0]['kelas']}")
print(f"Rata-rata kelas   : {rata2:.2f}")


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