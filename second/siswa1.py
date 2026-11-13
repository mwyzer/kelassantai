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


# ============================================================
# BAGIAN B — PRAKTIK: MINI DATABASE SISWA (persisten via JSON)
# ============================================================
# Tujuan: simpan daftar object Siswa ke file JSON, lalu buktikan
# datanya bisa dimuat kembali setelah program ditutup.
# ============================================================

FILE_DB = "siswa.json"


# --- Tambahkan method konversi ke dictionary pada class Siswa ---
# (object tidak bisa langsung disimpan sebagai JSON, jadi kita
#  ubah dulu menjadi dictionary.)
def siswa_jadi_dict(s):
    """Mengubah satu object Siswa menjadi dictionary."""
    return {"nama": s.nama, "nilai": s.nilai}


def dict_jadi_siswa(d):
    """Kebalikannya: dictionary -> object Siswa."""
    return Siswa(d["nama"], d["nilai"])


# --- Function menyimpan daftar siswa ke JSON --------------------
def simpan_json(daftar_siswa, nama_file):
    """Menulis list object Siswa ke file JSON."""
    data = [siswa_jadi_dict(s) for s in daftar_siswa]   # list of dict
    with open(nama_file, "w") as f:
        json.dump(data, f, indent=2)
    print(f"-> {len(data)} siswa disimpan ke {nama_file}")


# --- Function memuat daftar siswa dari JSON ---------------------
def muat_json(nama_file):
    """Membaca file JSON dan mengembalikannya sebagai list object Siswa.
    Aman bila file belum ada (try/except)."""
    try:
        with open(nama_file, "r") as f:
            data = json.load(f)
        return [dict_jadi_siswa(d) for d in data]
    except FileNotFoundError:
        print(f"-> {nama_file} belum ada, mulai dengan data kosong.")
        return []


# --- Program utama ---------------------------------------------
print()
print("=" * 55)
print("MINI DATABASE SISWA — KELAS SANTAI")
print("=" * 55)

# 1) Coba muat data lama (kalau ada dari menjalankan sebelumnya)
daftar = muat_json(FILE_DB)
if daftar:
    print(f"\nData lama ditemukan ({len(daftar)} siswa):")
    for s in daftar:
        print(f"  - {s.status()}")

# 2) Kalau kosong, isi dengan data awal
if not daftar:
    daftar = [
        Siswa("Budi", 85),
        Siswa("Sari", 92),
        Siswa("Andi", 68),
    ]
    print("\nMengisi data awal...")

# 3) Simpan ke file (persisten!)
print()
simpan_json(daftar, FILE_DB)

print("\nSelesai! Jalankan file ini SEKALI LAGI —")
print("kali kedua, data akan dimuat dari siswa.json (bukan data awal).")
print("Itu bukti data sudah persisten. Coba juga buka siswa.json di editor.")

