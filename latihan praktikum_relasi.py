# relasi aggregation
class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []    # agregasi: objek Nilai dapat hidup sendiri

    def tambah_nilai(self, nilai: Nilai):
        self.daftar_nilai.append(nilai)

    # (f) method menghitung rata-rata nilai
    def rata_rata(self):
        if not self.daftar_nilai:
            return 0
        return sum(n.skor for n in self.daftar_nilai) / len(self.daftar_nilai)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama: str):
        self.nama = nama
        self.daftar_matakuliah = []   # agregasi terhadap MataKuliah

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)


# relasi composition (Universitas menciptakan ProgramStudi)
class Universitas:
    def __init__(self, nama: str):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


# fungsi report program
def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
    print(f"\nProgram Studi: {prodi.nama}")
    print("Mata Kuliah:", ", ".join([mk.kode for mk in prodi.daftar_matakuliah]) or "-")
    print("Mahasiswa dan Rata-Rata Nilai:")

    for m in semua_mahasiswa:
        relevan = [n for n in m.daftar_nilai if any(n.kode_mk == mk.kode for mk in prodi.daftar_matakuliah)]
        if relevan:
            avg = sum(n.skor for n in relevan) / len(relevan)
            print(f"  {m.nim} - {m.nama}: {round(avg,2)}")

    print("-" * 40)


# MAIN PROGRAM
if __name__ == "__main__":
    # Universitas dan Program Studi awal
    uni = Universitas("Universitas A")
    prodi_ti = uni.buat_program("Teknik Informatika")

    # (a) Tambahkan 2 Program Studi baru
    prodi_si = uni.buat_program("Sistem Informasi")
    prodi_tm = uni.buat_program("Teknik Mesin")

    # (b) Tambahkan minimal 2 Mata Kuliah di setiap Prodi
    prodi_ti.tambah_matakuliah(MataKuliah("TI101", "Pemrograman Dasar"))
    prodi_ti.tambah_matakuliah(MataKuliah("TI102", "Struktur Data"))

    prodi_si.tambah_matakuliah(MataKuliah("SI201", "Basis Data"))
    prodi_si.tambah_matakuliah(MataKuliah("SI202", "Sistem Informasi Manajemen"))

    prodi_tm.tambah_matakuliah(MataKuliah("TM301", "Termodinamika"))
    prodi_tm.tambah_matakuliah(MataKuliah("TM302", "Mekanika Material"))

    # (c) Buat 3 mahasiswa dan tambahkan nilai
    m1 = Mahasiswa("23001", "Budi")
    m2 = Mahasiswa("23002", "Siti")
    m3 = Mahasiswa("23003", "Andi")

    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))
    m1.tambah_nilai(Nilai("SI201", 70))

    m2.tambah_nilai(Nilai("SI201", 88))
    m2.tambah_nilai(Nilai("SI202", 92))

    m3.tambah_nilai(Nilai("TM301", 75))
    m3.tambah_nilai(Nilai("TM302", 80))

    daftar_mahasiswa = [m1, m2, m3]

    # (d) Tampilkan daftar mata kuliah setiap program studi
    print("\n========== DAFTAR MATA KULIAH PER PROGRAM STUDI ==========")
    for prodi in uni.programs:
        print(f"\n{prodi.nama}:")
        for mk in prodi.daftar_matakuliah:
            print(f"  {mk.kode} - {mk.nama}")

    # (e) Tampilkan daftar nilai setiap mahasiswa
    print("\n========== DAFTAR NILAI MAHASISWA ==========")
    for m in daftar_mahasiswa:
        print(f"\n{m.nim} - {m.nama}")
        for n in m.daftar_nilai:
            print(f"  {n.kode_mk}: {n.skor}")

    # (f) Tampilkan rata-rata nilai setiap mahasiswa
    print("\n========== RATA-RATA NILAI MAHASISWA ==========")
    for m in daftar_mahasiswa:
        print(f"{m.nim} - {m.nama}: {round(m.rata_rata(),2)}")

    # (g) Report per program studi
    print("\n========== REPORT PER PROGRAM STUDI ==========")
    for prodi in uni.programs:
        report_program(prodi, daftar_mahasiswa)
