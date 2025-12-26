class Buku:
    # Class attribute
    perpustakaan = "perpustakaan STITEK"

    # Constructor
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info_buku(self):
        return f"Buku {self.judul} oleh {self.penulis} ({self.tahun})"

# Instansiasi object
Buku1 = Buku("Pemrograman python", "John Doe", 2023)
Buku2 = Buku("Struktur Data", "Jane Doe", 2022)

print(Buku1.info_buku())
print(Buku2.info_buku())
print(f"Lokasi: {Buku.perpustakaan}")
