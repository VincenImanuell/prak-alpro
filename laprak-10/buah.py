# list of dictionaries
daftar_harga = [
    {"nama": "apel", "harga": 10000},
    {"nama": "jeruk", "harga": 20000},
    {"nama": "durian", "harga": 120000},
    {"nama": "kiwi", "harga": 60000},
    {"nama": "melon", "harga": 300000}
]

# tampilkan semua nama buah dan harganya
for buah in daftar_harga:
    print(f'{buah["nama"]} - {buah["harga"]}')

# tampilkan nama buah yang paling mahal
termahal = 0
nama_buah_termahal = ''
for buah in daftar_harga:
    if buah["harga"] > termahal :
        termahal = buah["harga"]
        nama_buah_termahal = buah["nama"]
print(f'Buah termahal adalah buah {nama_buah_termahal}, dengan harga: Rp {termahal}')

# hapus buah yang harganya kurang dari 100.000
print('Hapus buah')

batas = 100000

# ambil dulu jumlah dalam list
count = len(daftar_harga)
index = 0
while index < count:
    if (daftar_harga[index])["harga"] < batas:
        del daftar_harga[index]
    else:
        index = index + 1
    count = len(daftar_harga)

for buah in daftar_harga:
    print(f'{buah["nama"]} - {buah["harga"]}')