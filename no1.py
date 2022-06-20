dataMahasiswa = [
    {
        "Nama": "Bagus Maulidan",
        "NIM": "421313249",
        "Jurusan": "Teknologi Informasi"
    },
    {
        "Nama": "Ary Mahendra",
        "NIM": "421313248",
        "Jurusan": "Teknologi Informasi"
    },
    {
        "Nama": "Tri Kusuma",
        "NIM": "421313247",
        "Jurusan": "Teknologi Informasi"
    }

]

print("Silahkan Pilih Nama Mahasiswa Berikut : ")
num = 1
while num < len(dataMahasiswa):
    for data in dataMahasiswa:
        print(num, data["Nama"])
        num += 1

input = input("\nMasukkan Angka 1-3 :")


def tampil(indeks):
    print("Nama = ", dataMahasiswa[indeks]['Nama'])
    print("Nim = ", dataMahasiswa[indeks]['NIM'])
    print("Jurusan = ", dataMahasiswa[indeks]['Jurusan'])


if input == '1':
    tampil(0)

elif input == '2':
    tampil(1)
else:
    tampil(2)
