data = {
    "nama toko": "",
    "nama pembeli": "",
    "barang": [
    {"no": 1, "kode barang": "P001", "nama barang": "pensil", "harga": 1500, "jumlah beli": 2},
    {"no": 2, "kode barang": "P02B", "nama barang": "pensil 2b", "harga": 3500, "jumlah beli": 1},
    {"no": 3, "kode barang": "B001", "nama barang": "buku", "harga": 2500, "jumlah beli": 3},
    {"no": 4, "kode barang": "PG01", "nama barang": "penggaris", "harga": 1500, "jumlah beli": 4},
    {"no": 5, "kode barang": "PH01", "nama barang": "penghapus", "harga": 750, "jumlah beli": 2}
]
}

nama_toko = input("Masukkan nama toko: ")
nama_pembeli = input("Masukkan nama pembeli: ")

data["nama toko"] = nama_toko
data["nama pembeli"] = nama_pembeli

print("\n================================================\n")

print(f'Nama toko: {data["nama toko"]}')
print(f'Nama pembeli: {data["nama pembeli"]}')

beli = data["barang"]
index = 0
jumlah_barang = 0
total_harga = 0
for pembelian in beli:
    print(f'Beli {pembelian["nama barang"]}(Rp {pembelian["harga"]}) sebanyak {pembelian["jumlah beli"]} buah.')
    total_harga = total_harga + (pembelian["harga"]*pembelian["jumlah beli"])
    jumlah_barang = jumlah_barang + pembelian["jumlah beli"]

harga_setelah_diskon = total_harga-(total_harga*(20/100))

print(f'Jumlah barang: {jumlah_barang}\nTotal harga: Rp {total_harga}, setelah diskon 20%: Rp {harga_setelah_diskon:.2f}')