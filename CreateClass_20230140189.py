# Definisi Class
class PersegiPanjang:
    # Constructor
    def __init__(self, panjang, lebar):
        # Validasi Atribut
        if panjang <= 0 or lebar <= 0:
            raise ValueError("Panjang dan lebar harus lebih besar dari 0.")
        self.panjang = panjang
        self.lebar = lebar
    # Cara Menghitung Keliling
    def hitung_keliling(self):
        """Menghitung keliling persegi panjang."""
        return 2 * (self.panjang + self.lebar)
    # Cara Menghitung Luas
    def hitung_luas(self):
        """Menghitung luas persegi panjang."""
        return self.panjang * self.lebar
    # Representasi String
    def __str__(self):
        """Mengembalikan representasi string dari objek PersegiPanjang."""
        return f"Persegi Panjang, Panjang {self.panjang} cm, dan Lebar {self.lebar} cm"

def main():
    try:
        # Input dari pengguna
        panjang = float(input("Masukkan panjangnya (cm): "))
        lebar = float(input("Masukkan lebarnya (cm): "))
        if panjang <= 0  or lebar <= 0 :
            print('Panjang dan lebar harus lebih besar dari 0')
            return
        # Membuat objek PersegiPanjang
        pp = PersegiPanjang(panjang, lebar)
        # Menampilkan deskripsi objek
        print(pp)  # Menampilkan deskripsi objek
        print(f"Keliling: {pp.hitung_keliling()} cm")  # Menghitung dan menampilkan keliling
        print(f"Luas: {pp.hitung_luas()} cm²")  # Menghitung dan menampilkan luas
    except ValueError:
        print("Input tidak valid! Harap masukkan angka yang benar.")
if __name__ == "_main__":
    main()
    
