from prettytable import PrettyTable
import connectdb
import crud

status = True

while status:
    programming = connectdb.koneksi.cursor()

    programming.execute('select*from mahasiswa')

    data = programming.fetchall()
    t = PrettyTable(['id', 'nama', 'nim'])

    for row in data:
        t.add_row(row)

    print("             ==================")
    print("               Data Mahasiswa")
    print("             ==================")
    print(t)

    print("Pilih Aksi : ")
    print("1. Tambah Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Exit")
    inputuser = input("\nMasukkan Pilihan : ")

    if inputuser == '1':
        crud.insert()
        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) :")
        if cek == 'No':
            status = False
    if inputuser == '2':
        crud.update()
        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) : ")
        if cek == 'No':
            status = False
    if inputuser == '3':
        crud.delete()
        cek = input("Apakah Anda Ingin Melanjutkan Program? (Ya/No) : ")
        if cek == 'No':
            status = False
    if inputuser == '4':
        status = False
