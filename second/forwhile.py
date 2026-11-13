print()
print("=" * 50)
print("DEMO 2 — Perulangan for & while")
print("=" * 50)

# for: mengulang untuk SETIAP item di dalam list
sayur = ["bayam", "asem", "lodeh"]
for item in sayur:
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