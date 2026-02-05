from abc import ABC, abstractmethod

# 1. Interface / Abstract Class
# Ini adalah KONTRAK. Semua class turunan WAJIB
# mengimplementasikan method di bawah ini.
class GameUnit(ABC):

    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


# 2. Implementasi pada Class Konkret
class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    # Wajib implementasi method dari abstract class
    # def serang(self, target):
        # print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    # Implementasi serang versi Monster
    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


# -- Uji Coba --
# unit = GameUnit()  # ERROR: Abstract class tidak bisa dibuat objek

h = Hero("Alucard")
m = Monster("Serigala")
unit = GameUnit()

h.info()
m.info()
h.serang("Monster")
m.serang("Hero")
