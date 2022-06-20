from contextlib import nullcontext
import connectdb


def insert():
    nama = input("Masukkan Nama : ")
    nim = input("Masukkan NIM  : ")

    if len(nama) == 0 and len(nim) == 0:
        print("Data Kosong")
    else:
        koneksiTest = connectdb.koneksi.cursor()

        koneksiTest.execute(
            "insert into mahasiswa (nama, nim) VALUES (%s, %s)", (nama, nim))

        connectdb.koneksi.commit()

        print("Data Berhasil Ditambahkan")


def update():
    idupdate = input("Masukkan Id yang ingin di update : ")
    print("Pilih tabel yang ingin diupdate : ")
    print("1. Nama")
    print("2. NIM")
    print("3. Ubah Seluruhnya")
    aksiupdate = input("Pilih 1-3 : ")
    if aksiupdate == '1':
        namaupdate = input("Masukkan Nama Baru : ")
        koneksiTest = connectdb.koneksi.cursor()
        koneksiTest.execute(
            f"update mahasiswa set nama = '{namaupdate}' where id = '{idupdate}'")
        connectdb.koneksi.commit()
        print("Data Nama Berhasil Diupdate")
    elif aksiupdate == '2':
        nimupdate = input("Masukkan NIM Baru : ")
        koneksiTest = connectdb.koneksi.cursor()
        koneksiTest.execute(
            f"update mahasiswa set nim = '{nimupdate}' where id = '{idupdate}'")
        connectdb.koneksi.commit()
        print("Data NIM Berhasil Diupdate")
    elif aksiupdate == '3':
        namaupdate = input("Masukkan Nama Baru : ")
        nimupdate = input("Masukkan NIM Baru : ")
        koneksiTest = connectdb.koneksi.cursor()
        koneksiTest.execute(
            f"update mahasiswa set nama = '{namaupdate}', nim = '{nimupdate}' where id = '{idupdate}'")
        connectdb.koneksi.commit()
        print("Data Berhasil Diupdate")
    else:
        print("Masukkan 1-3")


def delete():
    iddelete = input("Masukkan ID yang ingin di hapus : ")
    koneksiTest = connectdb.koneksi.cursor()
    koneksiTest.execute(
        f"delete from mahasiswa where id='{iddelete}'")
    connectdb.koneksi.commit()
    print("Data Berhasil Dihapus")



