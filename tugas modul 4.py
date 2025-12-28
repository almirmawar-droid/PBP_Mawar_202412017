from abc import ABC, abstractmethod

# Custom Exception
class PoinTidakValidError(Exception):
    pass


# Abstract Class
class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        pass


# Class Member
class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    def akses(self):
        print("Hak akses: Member")

    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    def __add__(self, other):
        return self.poin + other.poin

    def __len__(self):
        return len(self.nama)


# Program Utama
try:
    poin_input = input("Masukkan poin member 1: ")

    if poin_input.strip() == "":
        print("Error: Input tidak boleh kosong!")
    else:
        poin1 = int(poin_input)
        if poin1 < 0:
            raise PoinTidakValidError("Poin tidak boleh negatif!")

        m1 = Member("Andi", poin1)
        m2 = Member("Budi", 50)

        print(m1)
        print(m2)
       
        print("Total poin:", m1 + m2)
       
        print("Panjang nama m1:", len(m1))

except ValueError:
    print("Error: Input harus berupa angka!")
except PoinTidakValidError as e:
    print("Custom Error:", e)
