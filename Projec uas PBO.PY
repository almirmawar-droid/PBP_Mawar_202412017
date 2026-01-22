import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

# ================= CUSTOM EXCEPTION =================
class DataTidakValidError(Exception):
    pass


# ================= ABSTRACT CLASS =================
class Person(ABC):
    def __init__(self, nama):
        self.nama = nama  # public

    @abstractmethod
    def info(self):
        pass

    def __str__(self):
        return f"Nama: {self.nama}"


# ================= INHERITANCE =================
class Mahasiswa(Person):
    def __init__(self, nama, nim):
        super().__init__(nama)
        self._nim = nim        # protected
        self.__ipk = 0.0       # private

    def set_ipk(self, ipk):
        if ipk < 0 or ipk > 4:
            raise DataTidakValidError("IPK harus antara 0 - 4")
        self.__ipk = ipk

    def get_ipk(self):
        return self.__ipk

    def info(self):  # overriding
        return f"Mahasiswa | {self.nama} | NIM: {self._nim} | IPK: {self.__ipk}"


class Dosen(Person):
    def __init__(self, nama, nidn):
        super().__init__(nama)
        self.nidn = nidn

    def info(self):  # overriding
        return f"Dosen | {self.nama} | NIDN: {self.nidn}"


# ================= AGGREGATION =================
class DataManager:
    def __init__(self):
        self.data = []  # list of objects

    def tambah_data(self, obj):
        self.data.append(obj)

    def tampilkan_data(self):
        return "\n".join([obj.info() for obj in self.data])


# ================= GUI CLASS =================
class AplikasiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Manajemen Data PBO")
        self.root.geometry("500x400")

        self.manager = DataManager()  # composition

        # ====== FORM ======
        tk.Label(root, text="Nama").pack()
        self.entry_nama = tk.Entry(root)
        self.entry_nama.pack()

        tk.Label(root, text="NIM / NIDN").pack()
        self.entry_id = tk.Entry(root)
        self.entry_id.pack()

        tk.Label(root, text="IPK (khusus Mahasiswa)").pack()
        self.entry_ipk = tk.Entry(root)
        self.entry_ipk.pack()

        # ====== BUTTON ======
        tk.Button(root, text="Tambah Mahasiswa", command=self.tambah_mahasiswa).pack(pady=5)
        tk.Button(root, text="Tambah Dosen", command=self.tambah_dosen).pack(pady=5)
        tk.Button(root, text="Tampilkan Data", command=self.tampilkan).pack(pady=5)

        # ====== OUTPUT ======
        self.text_output = tk.Text(root, height=10)
        self.text_output.pack()

    # ================= EVENT HANDLER =================
    def tambah_mahasiswa(self):
        try:
            nama = self.entry_nama.get()
            nim = self.entry_id.get()
            ipk = float(self.entry_ipk.get())

            mhs = Mahasiswa(nama, nim)
            mhs.set_ipk(ipk)

            self.manager.tambah_data(mhs)
            messagebox.showinfo("Sukses", "Mahasiswa berhasil ditambahkan")

        except ValueError:
            messagebox.showerror("Error", "IPK harus berupa angka")
        except DataTidakValidError as e:
            messagebox.showerror("Error", str(e))
        finally:
            self.clear_input()

    def tambah_dosen(self):
        nama = self.entry_nama.get()
        nidn = self.entry_id.get()

        dosen = Dosen(nama, nidn)
        self.manager.tambah_data(dosen)

        messagebox.showinfo("Sukses", "Dosen berhasil ditambahkan")
        self.clear_input()

    def tampilkan(self):
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, self.manager.tampilkan_data())

    def clear_input(self):
        self.entry_nama.delete(0, tk.END)
        self.entry_id.delete(0, tk.END)
        self.entry_ipk.delete(0, tk.END)


# ================= MAIN PROGRAM =================
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiGUI(root)
    root.mainloop()
