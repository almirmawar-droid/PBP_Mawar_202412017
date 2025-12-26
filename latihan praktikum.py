# Class Person
class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}"


# Class Mahasiswa (inherit dari Person)
class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)  # memanggil constructor parent
        self.nim = nim

    def info(self):
        return f"Mahasiswa: {self.nama}, Umur: {self.umur}, NIM: {self.nim}"


# Instansiasi objek
p = Person("Rina", 20)
m = Mahasiswa("Mawar", 19, "202412017")

# Memanggil method info()
print(p.info())
print(m.info())
