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

status = True
while status:
    print("Silahkan Pilih Nama Mahasiswa Berikut : ")
    num = 1
    while num < len(dataMahasiswa):
        for data in dataMahasiswa:
            print(num, data["Nama"])
            num += 1

    userInput = input("\nMasukkan Angka 1-3 :")

    def tampil(indeks):
        print("Nama     = ", dataMahasiswa[indeks]['Nama'])
        print("Nim      = ", dataMahasiswa[indeks]['NIM'])
        print("Jurusan  = ", dataMahasiswa[indeks]['Jurusan'])

    if userInput == '1':
        tampil(0)
        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) : ")
        if cek == 'No':
            status = False
    elif userInput == '2':
        tampil(1)
        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) : ")
        if cek == 'No':
            status = False
    elif userInput == '2':
        tampil(2)
        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) : ")
        if cek == 'No':
            status = False
    else:
        print("Hanya dapat memasukkan Angka 1-3")
        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) : ")
        if cek == 'No':
            status = False
