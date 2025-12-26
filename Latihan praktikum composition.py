# Class Penulis
class Penulis:
    def __init__(self, nama):
        self.nama = nama


# Class Buku (menggunakan Composition: memiliki Penulis)
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis   # objek dari class Penulis

    def info(self):
        return f"Buku: {self.judul}, ditulis oleh {self.penulis.nama}"


# Instansiasi
penulis = Penulis("Tere Liye")
buku = Buku("Rembulan Tenggelam di Wajahmu", penulis)

# Demonstrasi akses data penulis dari objek buku
print(buku.info())
