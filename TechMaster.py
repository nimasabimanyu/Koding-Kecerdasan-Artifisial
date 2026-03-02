from abc import ABC, abstractmethod

# ==============================
# ABSTRACT CLASS (ABSTRACTION)
# ==============================
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar):
        self.nama = nama
        self.__stok = 0
        self.__harga_dasar = harga_dasar

    # Getter (Encapsulation)
    def get_stok(self):
        return self.__stok

    def get_harga_dasar(self):
        return self.__harga_dasar

    # Method untuk menambah stok (dengan validasi)
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {self.__stok} unit.")

    # Abstract Method
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


# ==============================
# INHERITANCE + POLYMORPHISM
# ==============================
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, processor):
        super().__init__(nama, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self):
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        pajak = 0.10 * self.get_harga_dasar()
        print(f" Harga Dasar: Rp {self.get_harga_dasar():,}".replace(",", ".") +
              f" | Pajak(10%): Rp {int(pajak):,}".replace(",", "."))

    def hitung_harga_total(self, jumlah):
        pajak = 0.10 * self.get_harga_dasar()
        harga_total = (self.get_harga_dasar() + pajak) * jumlah
        return harga_total


class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, kamera):
        super().__init__(nama, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        pajak = 0.05 * self.get_harga_dasar()
        print(f" Harga Dasar: Rp {self.get_harga_dasar():,}".replace(",", ".") +
              f" | Pajak(5%): Rp {int(pajak):,}".replace(",", "."))

    def hitung_harga_total(self, jumlah):
        pajak = 0.05 * self.get_harga_dasar()
        harga_total = (self.get_harga_dasar() + pajak) * jumlah
        return harga_total


# ==============================
# FUNGSI POLYMORPHIC TRANSAKSI
# ==============================
def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total_semua = 0
    nomor = 1

    for barang, jumlah in daftar_barang:
        print(f"{nomor}. ", end="")
        barang.tampilkan_detail()
        subtotal = barang.hitung_harga_total(jumlah)
        print(f" Beli: {jumlah} unit | Subtotal: Rp {int(subtotal):,}".replace(",", "."))
        print()
        total_semua += subtotal
        nomor += 1

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {int(total_semua):,}".replace(",", "."))
    print("----------------------------------------")


# ==============================
# ALUR PROGRAM (USER STORY)
# ==============================

print("--- SETUP DATA ---")

# 1. Admin membuat data produk
laptop1 = Laptop("ROG Zephyrus", 20000000, "Ryzen 9")
hp1 = Smartphone("iPhone 13", 15000000, "12MP")

# 2. Admin mencoba stok negatif
laptop1.tambah_stok(10)
hp1.tambah_stok(-5)
hp1.tambah_stok(20)

# 3. User membeli
keranjang = [
    (laptop1, 2),
    (hp1, 1)
]

# 4. Cetak transaksi
proses_transaksi(keranjang)