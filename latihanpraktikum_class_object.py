class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        print(f"Dosen {self.nama} (NIDN: {self.nidn}) mengajar mata kuliah {mata_kuliah}.")

# Membuat dua objek dosen
dosen1 = Dosen("Dr. Andi", "12345678")
dosen2 = Dosen("Prof. Budi", "87654321")

# Memanggil method
dosen1.ajar_mata_kuliah("Pemrograman Python")
dosen2.ajar_mata_kuliah("Sistem Basis Data")
