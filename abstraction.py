from abc import ABC, abstractmethod
class Kendaraan(ABC): # Class Abstrak
 @abstractmethod
 def bergerak(self):
     pass
class Mobil(Kendaraan):
 def bergerak(self):
     print("Berjalan dengan roda")
class Kapal(Kendaraan):
 def bergerak(self):
     print("Berlayar di air")
# k = Kendaraan() # Ini akan Error! Class abstrak tidak bisa diinstansiasi.
m = Mobil()
m.bergerak()