from abc import ABC, abstractmethod
# Ini bertindak sebagai Interface
class TombolInterface(ABC):
 @abstractmethod
 def tekan(self):
     pass
# Class ini WAJIB punya method tekan()
class TombolMerah(TombolInterface):
 def tekan(self):
     print("Sistem Dimatikan!")
class TombolHijau(TombolInterface):
 def tekan(self):
     print("Sistem Dinyalakan!")