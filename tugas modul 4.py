from abc import ABC, abstractmethod

# =========================
# Custom Exception
# =========================
class PoinTidakValidError(Exception):
    """Exception untuk poin yang bernilai negatif."""
    pass


# =========================
# Abstract Class
# =========================
class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        pass


# =========================
# Class Turunan
# =========================
class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    # Implementasi abstract method
    def akses(self):
        return "Hak akses: Member biasa"

    # Special Method __str__
    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    # Special Method __add__
    def __add__(self, other):
        if isinstance(other, Member):
            return self.poin + other.poin
        return NotImplemented

    # Special Method __len__
    def __len__(self):
        return len(self.nama)


# =========================
# Program Utama
# =========================
def input_poin():
    try:
        poin = input("Masukkan poin member: ")

        if poin == "":
            raise ValueError("Input poin tidak boleh kosong")

        poin = int(poin)

        if poin < 0:
            raise PoinTidakValidError("Poin tidak boleh bernilai negatif")

        return poin

    except ValueError as ve:
        print("Error:", ve)
        return None
    except PoinTidakValidError as pe:
        print("Error:", pe)
        return None


# =========================
# Eksekusi Program
# =========================
poin1 = input_poin()
poin2 = input_poin()

if poin1 is not None and poin2 is not None:
    m1 = Member("Andi", poin1)
    m2 = Member("Budi", poin2)

    # Menampilkan info member
    print("\n=== Info Member ===")
    print(m1)
    print(m2)

    # Menjumlahkan poin
    print("\nJumlah poin m1 + m2 =", m1 + m2)

    # Panjang nama
    print("Panjang nama m1 =", len(m1))

    # Hak akses
    print("\nHak akses m1:", m1.akses())
