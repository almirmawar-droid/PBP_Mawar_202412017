class Kendaraan:
    # Class attribute
    bahan_bakar = "Pertamax"

    # Constructor
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    # Method untuk menampilkan info kendaraan
    def info(self):
        return f"{self.merk} warna {self.warna} tahun {self.tahun}"


# Membuat 2 objek kendaraan
k1 = Kendaraan("Toyota Avanza", "Hitam", 2020)
k2 = Kendaraan("Honda Beat", "Merah", 2022)

# Menampilkan informasi dari instance attribute
print(k1.info())
print(k2.info())

# Akses class attribute
print("Bahan bakar (akses via class):", Kendaraan.bahan_bakar)

# Akses class attribute via objek
print("Bahan bakar (akses via objek):", k1.bahan_bakar)

# Mengubah class attribute
Kendaraan.bahan_bakar = "Solar"

print("\nSetelah class attribute diubah:")
print("Bahan bakar via class:", Kendaraan.bahan_bakar)
print("Bahan bakar via objek:", k1.bahan_bakar)
