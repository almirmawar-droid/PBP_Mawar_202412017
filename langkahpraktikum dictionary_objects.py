#  Membuat class Pelanggan dengan atribut id_pelanggan, nama, dan email
class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"{self.id_pelanggan} - {self.nama} ({self.email})"


#  Dictionary untuk menyimpan objek pelanggan
# key   : id_pelanggan
# value : objek Pelanggan
data_pelanggan = {}


#  Fungsi menambah pelanggan
def tambah_pelanggan(id_pelanggan, nama, email):
    if id_pelanggan in data_pelanggan:
        print("ID pelanggan sudah ada!")
    else:
        data_pelanggan[id_pelanggan] = Pelanggan(id_pelanggan, nama, email)
        print("Pelanggan berhasil ditambahkan.")


#  Fungsi menghapus pelanggan
def hapus_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        del data_pelanggan[id_pelanggan]
        print("Pelanggan berhasil dihapus.")
    else:
        print("Pelanggan tidak ditemukan.")


#  Fungsi mencari pelanggan
def cari_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        return data_pelanggan[id_pelanggan]
    else:
        return None


# Menambahkan beberapa pelanggan
tambah_pelanggan("C001", "Ahmad", "ahmad@gmail.com")
tambah_pelanggan("C002", "Budi", "budi@gmail.com")
tambah_pelanggan("C003", "Citra", "citra@gmail.com")

print("\n=== Daftar Pelanggan ===")

#  Menampilkan seluruh daftar pelanggan
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())


# Mencari pelanggan
print("\n=== Hasil Pencarian ===")
hasil = cari_pelanggan("C002")
if hasil:
    print("Pelanggan ditemukan:", hasil.info())
else:
    print("Pelanggan tidak ditemukan.")


# Menghapus pelanggan
print("\n=== Menghapus Pelanggan ===")
hapus_pelanggan("C001")

print("\n=== Daftar Pelanggan Setelah Penghapusan ===")
for pelanggan in data_pelanggan.values():
    print(pelanggan.info())
