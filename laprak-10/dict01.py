data_mahasiswa = {
    "nim": "71220856",
    "nama": "Bambang",
    "prodi": "informatika",
    "ipk": 5.2,
    "semester": 4,
    "matkul": [
        {"nama": "IMK", "sks": 3, "nilai": "E"},
        {"nama": "Tekkom", "sks": 3, "nilai": "C"},
        {"nama": "Jarkom", "sks": 5, "nilai": "E"}
    ],
}
print(data_mahasiswa["nama"])
print(f'IPK-nya: {data_mahasiswa["ipk"]}')
print(f'Sudah mengambil {len(data_mahasiswa["matkul"])} mata kuliah')
transkrip = data_mahasiswa["matkul"]
total_sks = 0
total_bobot = 0
for matkul in transkrip:
    if matkul["nilai"] == "E":
        print(matkul["nama"])
    total_sks = total_sks + matkul["sks"]
    if matkul["nilai"] == "A":
        total_bobot = total_bobot + 4 * matkul["sks"]
    elif matkul["nilai"] == "B":
        total_bobot = total_bobot + 3 * matkul["sks"]
    elif matkul["nilai"] == "C":
        total_bobot = total_bobot + 2 * matkul["sks"]
    elif matkul["nilai"] == "D":
        total_bobot = total_bobot + 1 * matkul["sks"]
    elif matkul["nilai"] == "E":
        total_bobot = total_bobot + 0 * matkul["sks"]
print(f'Total sks: {total_sks}')
ipk = total_bobot / total_sks
data_mahasiswa["ipk"] = ipk
print(data_mahasiswa)