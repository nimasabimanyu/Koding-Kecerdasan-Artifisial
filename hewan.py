# Parent Class
class Hewan:
 def makan(self):
     print("Hewan ini sedang makan.")
# Child Class (Mewarisi Hewan)
class Burung(Hewan):
 def terbang(self):
     print("Burung sedang terbang.")
# Object
beo = Burung()
beo.makan() # Mewarisi dari Hewan (Output: Hewan ini sedangmakan.)
beo.terbang() # Method milik sendiri