from modeli.identifikacija import Identifikacija

class Odsek(Identifikacija):
    
    def __init__(self, oznaka, ime, max_br_radnika, opis):
        super().__init__(oznaka)
        self.ime = ime 
        self.max_br_radnika = max_br_radnika 
        self.opis = opis 
        
    @property 
    def ime(self):
        return self._ime 
        
    @ime.setter 
    def ime(self, value):
        if not isinstance(value, str):
            raise ValueError("Ime mora biti tekstualna vrednost!")
        if value == "":
            raise ValueError("Morate uneti neku tekstualnu vrednost!")
        self._ime = value 
        
    @property 
    def max_br_radnika(self):
        return self._max_br_radnika 
    
    @max_br_radnika.setter 
    def max_br_radnika(self, value):
        if not isinstance(value, int):
            raise ValueError("Mora biti broj!")
        if value > 300:
            raise ValueError("Broj radnika mora biti manji od 300")
        self._max_br_radnika = value 
        
    @property
    def opis(self):
        return self._opis
    
    @opis.setter 
    def opis(self, value):
        if not isinstance(value, str):
            raise ValueError("Opis mora biti tekstualna vrednost!")
        if value == "":
            raise ValueError("Morate uneti neku tekstualnu vrednost ")
        self._opis = value 
        
        
    def __str__(self):
        return"Ime odseka: {}, maksimalan broj radnika: {}, opis: {}".format(self._ime, self._max_br_radnika, self._opis)
        
        
    