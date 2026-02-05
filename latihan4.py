class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        # Enkapsulasi: HP bersifat private (hanya bisa diakses di dalam class)
        self.__hp = hp_awal

    # GETTER: Cara resmi melihat HP
    def get_hp(self):
        return self.__hp

    # SETTER: Cara resmi mengubah HP (dengan validasi)
    def set_hp(self, nilai_baru):
            self.__hp = nilai_baru

    def diserang(self, damage):
        # Pakai getter & setter agar tetap aman
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# -- Uji Coba --
hero1 = Hero("Layla", 100)

# hero1.__hp = 9999  # GAGAL (tidak mengubah HP asli)
# print(hero1.__hp)  # ERROR (tidak bisa diakses langsung)

hero1.set_hp(-100)     # Coba set HP negatif
print(hero1.get_hp()) # Output: 0
print(f"Mencoba akses paksa: {hero1._Hero__hp}")