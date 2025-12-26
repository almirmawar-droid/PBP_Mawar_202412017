import math

# Class induk
class Bentuk:
    def luas(self):
        return 0


# Class Persegi
class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi


# Class Lingkaran
class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * self.jari_jari * self.jari_jari


# Demonstrasi pemanggilan method luas()
bentuk = Bentuk()
persegi = Persegi(4)
lingkaran = Lingkaran(7)

print("Luas Bentuk :", bentuk.luas())          # hasil 0
print("Luas Persegi :", persegi.luas())        # 4 × 4 = 16
print("Luas Lingkaran :", lingkaran.luas())    # π × 7²
