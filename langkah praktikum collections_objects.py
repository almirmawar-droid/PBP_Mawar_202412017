# a. Membuat class Buku dengan atribut judul, penulis, dan tahun
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"{self.judul} - {self.penulis} ({self.tahun})"


# b. Membuat list yang berisi 5 objek buku
daftar_buku = [
    Buku("Pemrograman Python", "Andi", 2021),
    Buku("Struktur Data", "Budi", 2020),
    Buku("Basis Data", "Andi", 2019),
    Buku("Algoritma", "Citra", 2022),
    Buku("OOP dengan Python", "Andi", 2023)
]


# c. Fungsi untuk mencari buku berdasarkan penulis
def cari_buku_berdasarkan_penulis(nama_penulis):
    hasil = []
    for buku in daftar_buku:
        if buku.penulis.lower() == nama_penulis.lower():
            hasil.append(buku)
    return hasil


# d. Menampilkan hasil pencarian
penulis_dicari = "Andi"
hasil_pencarian = cari_buku_berdasarkan_penulis(penulis_dicari)

print("=== Hasil Pencarian Buku ===")
print(f"Penulis: {penulis_dicari}")

if hasil_pencarian:
    for buku in hasil_pencarian:
        print(buku.info())
else:
    print("Buku tidak ditemukan.")
