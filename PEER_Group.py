# Program Kalkulasi Pengeluaran Mingguan
print("Test")
# Fungsi untuk menampilkan pengeluaran harian
def tampilkan_pengeluaran(hari, data):
    print(f"\nPengeluaran hari {hari.capitalize()}:")
    for item in data:
        print(f"- {item['kategori']} : Rp{item['jumlah']}")

# Fungsi untuk menghitung total pengeluaran Senin - Kamis
def total_senin_kamis(pengeluaran_mingguan):
    total = 0
    for hari in ["senin", "selasa", "rabu", "kamis"]:
        if hari in pengeluaran_mingguan:
            for item in pengeluaran_mingguan[hari]:
                total += item['jumlah']
    return total

# Fungsi untuk menghitung total per kategori selama seminggu
def total_per_kategori(pengeluaran_mingguan):
    kategori_total = {}
    for hari, data in pengeluaran_mingguan.items():
        for item in data:
            kategori = item['kategori']
            jumlah = item['jumlah']
            if kategori in kategori_total:
                kategori_total[kategori] += jumlah
            else:
                kategori_total[kategori] = jumlah
    return kategori_total


# ----------------- PROGRAM UTAMA -------------------
hari_list = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
pengeluaran_mingguan = {}

# Input pengeluaran 7 hari
for hari in hari_list:
    print(f"\nMasukkan data pengeluaran untuk hari {hari.capitalize()}:")
    pengeluaran_mingguan[hari] = []

    while True:
        jumlah = int(input("Masukkan jumlah pengeluaran (Rp): "))
        kategori = input("Masukkan kategori (transportasi, kebutuhan harian, jajan, makanan pokok, main): ").lower()

        pengeluaran_mingguan[hari].append({
            "jumlah": jumlah,
            "kategori": kategori
        })

        lanjut = input("Apakah ingin menambah pengeluaran lagi di hari ini? (y/n): ").lower()
        if lanjut == "n":   
            break

    # Tampilkan pengeluaran per hari
    tampilkan_pengeluaran(hari, pengeluaran_mingguan[hari])

# Setelah 7 hari input selesai
print("\n================ HASIL AKHIR =================")
print("Total pengeluaran dari Senin sampai Kamis:")
print(f"Rp{total_senin_kamis(pengeluaran_mingguan)}")

print("\nTotal pengeluaran per kategori selama seminggu (dari terbesar ke terkecil):")
kategori_total = total_per_kategori(pengeluaran_mingguan)
# Urutkan dari terbesar ke terkecil
kategori_urut = sorted(kategori_total.items(), key=lambda x: x[1], reverse=True)

for kategori, total in kategori_urut:
    print(f"- {kategori.capitalize()} : Rp{total}")