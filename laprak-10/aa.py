# dictionary kosong, data = dict() atau data = {}
data = dict()
print(data)
data["nama"] = "apel"
print(data)
data["harga"] = 5000
print(data)
data["nama"] = "sawo"
data["harga"] = 3000
print(data)

print(dir(data))
data["harga"] = 5000

print(data.keys())
print(data.values())

# warna tidak ada, dengan get tidak akan error
print(data.get('warna'))
print(data.get('nama'))

# hapus atribut harga
del data["harga"]
print(data)