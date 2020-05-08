from modeli.identifikacija import Identifikacija
from dekoratori.dekoratori import  wrapisinstance, isnotempty

class Odsek(Identifikacija):
    
    def __init__(self, oznaka, ime, max_br_radnika, opis, lista_radnika, lista_delova):
        super().__init__(oznaka)
        self.ime = ime 
        self.max_br_radnika = max_br_radnika 
        self.opis = opis 
        self.lista_radnika = []
        self.lista_delova = []
        
    @property
    def lista_radnika(self):
        return self._lista_radnika 
    
    @lista_radnika.setter 
    def lista_radnika(self, value):
        self._lista_radnika = value   
        
    @property 
    def lista_delova(self):
        return self._lista_delova 
    
    @lista_delova.setter 
    def lista_delova(self, value):
        self._lista_delova = value   
        
    @property 
    def ime(self):
        return self._ime 
        
    @ime.setter 
    @wrapisinstance(str)
    @isnotempty
    def ime(self, value):
        self._ime = value 
        
    @property 
    def max_br_radnika(self):
        return self._max_br_radnika 
    
    @max_br_radnika.setter 
    @wrapisinstance(int)
    def max_br_radnika(self, value):
        if value > 300:
            raise ValueError("Broj radnika mora biti manji od 300")
        self._max_br_radnika = value 
        
    @property
    def opis(self):
        return self._opis  

    @opis.setter 
    @wrapisinstance(str)
    @isnotempty
    def opis(self, value):
        self._opis = value 
        
        
    def __str__(self):
        return"Ime odseka: {}, maksimalan broj radnika: {}, opis: {}".format(self._ime, self._max_br_radnika, self._opis)
        
        
    