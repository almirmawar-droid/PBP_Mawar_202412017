class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim              # public
        self.nama = nama            # public
        self._semester = semester   # protected
        self.__ipk = ipk            # private

    # Getter protected
    def get_semester(self):
        return self._semester

    # Setter protected
    def set_semester(self, smt):
        if smt < 1:
            raise ValueError("Semester tidak boleh kurang dari 1.")
        self._semester = smt

    # Getter private
    def get_ipk(self):
        return self.__ipk

    # Setter private
    def set_ipk(self, nilai):
        if not (0.0 <= nilai <= 4.0):
            raise ValueError("IPK harus antara 0.0 - 4.0")
        self.__ipk = round(nilai, 2)


# --------------------- (b) Buat 2 objek mahasiswa --------------------
m1 = Mahasiswa("23001", "Budi", 2, 3.1)
m2 = Mahasiswa("23002", "Siti", 4, 3.7)

print("DATA AWAL")
print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())
print()

# --------------------- (c) Ganti semester dan IPK --------------------
m1.set_semester(3)
m1.set_ipk(3.5)

m2.set_semester(5)
m2.set_ipk(3.9)

print("DATA SETELAH DIUPDATE")
print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())
