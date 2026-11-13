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
teks = "84"  # pura-puranya ini input pengguna; coba ganti jadi "42"
try:
    angka_input = int(teks)
    print(f"Berhasil dikonversi: {angka_input}")
except ValueError:
    print(f"'{teks}' bukan angka — program tetap jalan, tidak crash!")

