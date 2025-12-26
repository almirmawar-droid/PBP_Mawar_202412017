# ========== Parent Class ==========
class Karyawan:
    def __init__(self, nama, gaji_pokok):
        self.nama = nama
        self.gaji_pokok = gaji_pokok

    def info_gaji(self):
        return f"{self.nama} - Gaji pokok: {self.gaji_pokok}"


# ========== Child Class: Manager ==========
class Manager(Karyawan):
    def __init__(self, nama, gaji_pokok, tunjangan):
        super().__init__(nama, gaji_pokok)
        self.tunjangan = tunjangan

    # Override
    def info_gaji(self):
        total = self.gaji_pokok + self.tunjangan
        return f"Manager {self.nama} - Total Gaji: {total}"


# ========== Child Class: Programmer ==========
class Programmer(Karyawan):
    def __init__(self, nama, gaji_pokok, bonus):
        super().__init__(nama, gaji_pokok)
        self.bonus = bonus

    # Override
    def info_gaji(self):
        total = self.gaji_pokok + self.bonus
        return f"Programmer {self.nama} - Total Gaji: {total}"


# ========== Composition: Departemen ==========
class Departemen:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_karyawan = []    # list of objects

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_karyawan(self):
        print(f"Daftar gaji karyawan di departemen {self.nama}:")
        for k in self.daftar_karyawan:
            print(k.info_gaji())


# ========== Instansiasi ==========
# Membuat 2 Manager dan 2 Programmer
m1 = Manager("Dewi", 8_000_000, 3_000_000)
m2 = Manager("Budi", 9_500_000, 2_500_000)

p1 = Programmer("Sinta", 7_000_000, 2_000_000)
p2 = Programmer("Andi", 6_500_000, 1_500_000)

# Membuat departemen dan menambahkan karyawan
dept = Departemen("IT")
dept.tambah_karyawan(m1)
dept.tambah_karyawan(m2)
dept.tambah_karyawan(p1)
dept.tambah_karyawan(p2)

# Menampilkan info gaji semua karyawan
dept.tampilkan_karyawan()
