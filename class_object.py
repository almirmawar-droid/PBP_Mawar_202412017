class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        
    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIM {self.nim}"
    
# pembuatan object
mhs1 = Mahasiswa("Budi santoso", "TI001")
mhs2 = Mahasiswa("siti Aminah", "TI002")

print(mhs1.perkenalan())
print(mhs2.perkenalan())
