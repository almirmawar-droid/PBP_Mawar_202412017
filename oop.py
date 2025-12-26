# pendekatan OOP
class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi
        
    def hitung_luas(self):
        return self.sisi * self.sisi
    
    def hitung_keliling(self):
        return 4 * self.sisi

# pembuatan object
persegi = Persegi(5)
print(f"Luas persegi: {persegi.hitung_luas()}")
print(f"Keliling persegi: {persegi.hitung_keliling()}")
