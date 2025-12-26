class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def __str__(self):
        return f"Nama: {self.nama}, Nilai: {self.nilai}"

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __add__(self, other):
        return self.nilai + other.nilai

    def __mul__(self, faktor):
        return self.nilai * faktor

    # __len__ → panjang nama mahasiswa
    def __len__(self):
        return len(self.nama)

    # __eq__ → sama jika nilai sama
    def __eq__(self, other):
        return self.nilai == other.nilai


# === Membuat minimal 2 objek ===
m1 = Mahasiswa("Andi", 85)
m2 = Mahasiswa("Budi", 85)

# === Representasi string ===
print(m1)
print(m2)

# === Perbandingan menggunakan == (memakai __eq__) ===
print("Nilai sama?", m1 == m2)

# === Operasi matematika ===
print("m1 + m2 =", m1 + m2)

print("m1 * 2 =", m1 * 2)

# === Panjang nama (memakai __len__) ===
print("Panjang nama m1 =", len(m1))
print("Panjang nama m2 =", len(m2))

# === Mengurutkan tanpa __lt__ ===
daftar = [m2, m1]
urut = sorted(daftar, key=lambda x: x.nilai)
print("Hasil sorting berdasarkan nilai:")
for mhs in urut:
    print(mhs)
