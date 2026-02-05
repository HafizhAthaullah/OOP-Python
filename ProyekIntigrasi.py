from abc import ABC, abstractmethod

# ===============================
# ABSTRACT CLASS (Abstraction)
# ===============================
class BarangElektronik(ABC):
    def __init__(self, nama, stok, harga_dasar):
        self.nama = nama
        self.__stok = 0
        self.__harga_dasar = 0

        self.tambah_stok(stok)
        self._set_harga_dasar(harga_dasar)

    # --------- ENCAPSULATION ----------
    def get_stok(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}: Stok tidak boleh negatif ({jumlah})")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {self.__stok} unit")

    def _set_harga_dasar(self, harga):
        if harga > 0:
            self.__harga_dasar = harga

    def _get_harga_dasar(self):
        return self.__harga_dasar

    # --------- ABSTRACT METHOD ----------
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


# ===============================
# CHILD CLASS: Laptop
# ===============================
class Laptop(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, processor):
        super().__init__(nama, stok, harga_dasar)
        self.processor = processor

    def tampilkan_detail(self):
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"Harga Dasar: Rp {self._get_harga_dasar():,}")

    def hitung_harga_total(self, jumlah):
        pajak = 0.10 * self._get_harga_dasar()
        subtotal = (self._get_harga_dasar() + pajak) * jumlah
        print(f"Pajak(10%): Rp {pajak:,.0f}")
        print(f"Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}")
        return subtotal


# ===============================
# CHILD CLASS: Smartphone
# ===============================
class Smartphone(BarangElektronik):
    def __init__(self, nama, stok, harga_dasar, kamera):
        super().__init__(nama, stok, harga_dasar)
        self.kamera = kamera

    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"Harga Dasar: Rp {self._get_harga_dasar():,}")

    def hitung_harga_total(self, jumlah):
        pajak = 0.05 * self._get_harga_dasar()
        subtotal = (self._get_harga_dasar() + pajak) * jumlah
        print(f"Pajak(5%): Rp {pajak:,.0f}")
        print(f"Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}")
        return subtotal


# ===============================
# FUNGSI KERANJANG BELANJA
# ===============================
def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total = 0
    for barang, jumlah in daftar_barang:
        barang.tampilkan_detail()
        total += barang.hitung_harga_total(jumlah)
        print("-" * 30)

    print(f"TOTAL TAGIHAN: Rp {total:,.0f}")
    return total


# ===============================
# MAIN PROGRAM (User Story)
# ===============================
if __name__ == "__main__":
    print("\n--- SETUP DATA ---")

    laptop = Laptop("ROG Zephyrus", 10, 20_000_000, "Ryzen 9")
    smartphone = Smartphone("iPhone 13", 0, 15_000_000, "12MP")

    smartphone.tambah_stok(-5)   # harus gagal
    smartphone.tambah_stok(20)   # berhasil

    keranjang = [
        (laptop, 2),
        (smartphone, 1)
    ]

    proses_transaksi(keranjang)