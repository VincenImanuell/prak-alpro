data = {}

while True:
    n = int(input('Masukkan angka (negatif untuk berhenti): '))
    if n < 0:
        break
    else:
        if n%2 == 0:
            if data.get("genap") != None:
                data["genap"].append(n)
            else:
                data['genap'] = [n]
        else:
            if data.get("ganjil"):
                data["ganjil"].append(n)
            else:
                data["ganjil"] = [n]
print(data)