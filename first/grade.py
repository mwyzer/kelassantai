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