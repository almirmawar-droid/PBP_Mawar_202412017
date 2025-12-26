# Custom Exception
class UmurTerlaluMudaError(Exception):
    pass


class UmurTerlaluTuaError(Exception):
    pass


class AkunTidakDiizinkanError(Exception):
    pass


def set_umur(umur):
    if umur < 5:
        raise UmurTerlaluMudaError("Umur terlalu muda (minimal 5 tahun).")
    if umur > 100:
        raise UmurTerlaluTuaError("Umur terlalu tua (maksimal 100 tahun).")
    return umur


def daftar_akun(umur):
    if umur < 18:
        raise AkunTidakDiizinkanError("Umur belum memenuhi syarat membuat akun (minimal 18 tahun).")
    print("Akun berhasil dibuat!")


if __name__ == "__main__":
    while True:
        try:
            u = int(input("Masukkan umur: "))
            umur_valid = set_umur(u)
            daftar_akun(umur_valid)
            break  # keluar loop jika sukses

        except ValueError:
            print("Error: Input harus berupa bilangan bulat!")

        except UmurTerlaluMudaError as e:
            print("Error:", e)

        except UmurTerlaluTuaError as e:
            print("Error:", e)

        except AkunTidakDiizinkanError as e:
            print("Error:", e)

        finally:
            print("Proses input selesai.\n")
