from datetime import date, timedelta

# =================== CLASS BUKU ===================
class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul
        self.penulis = penulis
        self.kode_buku = kode_buku
        self._stok = stok                # protected
        self.__lokasi_rak = lokasi_rak   # private

    # Getter & Setter lokasi rak
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    def set_lokasi_rak(self, lokasi):
        self.__lokasi_rak = lokasi

    def tambah_stok(self, jumlah):
        self._stok += jumlah

    def kurangi_stok(self, jumlah):
        if self._stok >= jumlah:
            self._stok -= jumlah
            return True
        return False

    def info_buku(self):
        return f"{self.judul} | {self.penulis} | Stok: {self._stok}"


# =================== CLASS PEMINJAMAN ===================
class Peminjaman:
    def __init__(self, kode_buku, tanggal_pinjam, tanggal_kembali, status="Dipinjam"):
        self.kode_buku = kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status

    def info_peminjaman(self):
        return f"{self.kode_buku} | {self.tanggal_pinjam} → {self.tanggal_kembali} | {self.status}"


# =================== CLASS ANGGOTA ===================
class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam=3):
        self.id_anggota = id_anggota
        self.nama = nama
        self._maks_pinjam = maks_pinjam  # protected
        self.__status_aktif = True       # private
        self.daftar_peminjaman = []      # aggregation

    # Getter & Setter status
    def get_status(self):
        return "Aktif" if self.__status_aktif else "Nonaktif"

    def set_status(self, status):
        self.__status_aktif = status

    # Pinjam buku
    def pinjam_buku(self, buku: Buku):
        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            print(f"{self.nama} telah mencapai batas maksimal peminjaman!")
            return

        if buku.kurangi_stok(1):
            peminjaman = Peminjaman(
                buku.kode_buku,
                date.today(),
                date.today() + timedelta(days=7)  # tanggal kembali 7 hari
            )
            self.daftar_peminjaman.append(peminjaman)
            print(f"{self.nama} berhasil meminjam {buku.judul}")
        else:
            print(f"Stok buku {buku.judul} habis!")

    # Kembalikan buku
    def kembalikan_buku(self, buku: Buku):
        for pinjam in self.daftar_peminjaman:
            if pinjam.kode_buku == buku.kode_buku and pinjam.status == "Dipinjam":
                pinjam.status = "Dikembalikan"
                buku.tambah_stok(1)
                print(f"{self.nama} mengembalikan {buku.judul}")
                return
        print(f"Tidak ada peminjaman aktif untuk buku {buku.judul}")


# =================== CLASS PERPUSTAKAAN (Composition) ===================
class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku: Buku):
        self.daftar_buku.append(buku)

    def info_semua_buku(self):
        for buku in self.daftar_buku:
            print(buku.info_buku())


# =================== DEMONSTRASI PROGRAM ===================

# 1. Instansiasi 3 buku
b1 = Buku("Algoritma", "Dony", "B001", 3, "Rak A")
b2 = Buku("Basis Data", "Rini", "B002", 2, "Rak B")
b3 = Buku("Python", "Sakti", "B003", 1, "Rak C")

# Perpustakaan (composition)
perpus = Perpustakaan()
perpus.tambah_buku(b1)
perpus.tambah_buku(b2)
perpus.tambah_buku(b3)

# 2. Instansiasi 2 anggota
a1 = Anggota("A01", "Mawar")
a2 = Anggota("A02", "Adek")

# 3. Anggota 1 pinjam 2 buku
a1.pinjam_buku(b1)
a1.pinjam_buku(b2)

# 4. Anggota 2 pinjam 1 buku
a2.pinjam_buku(b3)

# 5. Pengembalian buku
a1.kembalikan_buku(b1)

# =================== OUTPUT / PRINT ===================
print("\n=== Informasi Buku & Stok ===")
perpus.info_semua_buku()

print("\n=== Informasi Anggota ===")
print(f"{a1.nama} | Status: {a1.get_status()}")
print(f"{a2.nama} | Status: {a2.get_status()}")

print("\n=== Daftar Peminjaman Anggota ===")
print(f"\n>> {a1.nama}")
for p in a1.daftar_peminjaman:
    print(p.info_peminjaman())

print(f"\n>> {a2.nama}")
for p in a2.daftar_peminjaman:
    print(p.info_peminjaman())
