# Function untuk menghitung harga setelah diskon
def hitung_diskon(harga, diskon):
    return harga - (harga * diskon / 100)

# Program utama
harga_awal = float(input("Masukkan harga barang: Rp"))
diskon = float(input("Masukkan diskon (%): "))

harga_akhir = hitung_diskon(harga_awal, diskon)
print(f"Harga setelah diskon: Rp{harga_akhir}")
