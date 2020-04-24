from modeli.identifikacija import Identifikacija
from datetime import datetime

class Radnik(Identifikacija):
    
    def __init__(self,oznaka, ime, prezime, jmbg, datum_rodjenja, mesto_rodjenja, drzava_rodjenja):
        super().__init__(oznaka)
        self.ime = ime 
        self.prezime = prezime 
        self.jmbg = jmbg 
        self.mesto_rodjenja = mesto_rodjenja 
        self.drzava_rodjenja = drzava_rodjenja 
        
    @property 
    def ime(self):
        return self._ime 
    
    @ime.setter 
    def ime(self, value):
        if not isinstance(value, str):
            raise ValueError("Ime mora biti tekstualna vrednost! ")
        if value == "":
            raise ValueError("Morate uneti neku vrednost!")
        self._ime = value 
        
    @property 
    def prezime(self):
        return self._prezime 
    
    @prezime.setter 
    def prezime(self, value):
        if not isinstance(value, str):
            raise ValueError("Prezime mora biti tekstualna vrednost! ")
        if value == "":
            raise ValueError("Morate uneti neku vrednost!")
        self._prezime = value 
        
    @property 
    def jmbg(self):
        return self._jmbg 
    
    @jmbg.setter 
    def jmbg(self,value):
        if not isinstance(value, int):
            raise ValueError("U JMBG nema tekstualnih vrednosti! ")
        if len(str(value)) != 13:
            raise ValueError("JMBG se mora sastojati od tacno 13 cifara!")
        self._jmbg = value 
        
    @property
    def datum_rodjenja(self):
        return self._datum_rodjenja 
    
    @datum_rodjenja.setter 
    def datum_rodjenja(self, value):
        
        date_format = '%d/%m/%Y'
        
        try:
            datetime.strptime(value, date_format)
            
        except ValueError:
            raise ValueError("Uneli ste neispravan datum. On mora biti u formatu dd/mm/yyyy") from None
        
        val_date = datetime.strptime(value, "%d/%m/%Y").date()
        pocetni = datetime.strptime("01/01/1930", "%d/%m/%Y").date()
        
        if val_date < pocetni:
            raise ValueError("Datum mora biti iznad 01/01/1930!")
        
        self._datum_rodjenja = value
        
        
        #mesto rodjenja , drzava rodjenja 
        
    @property
    def mesto_rodjenja(self):
        return self._mesto_rodjenja 
    
    @mesto_rodjenja.setter 
    def mesto_rodjenja(self, value):
        if not isinstance(value, str):
            raise ValueError("Mora biti tekstualna vrednost!")
        self._mesto_rodjenja = value 
        
    @property 
    def drzava_rodjenja(self):
        return self._drzava_rodjenja 
    
    @drzava_rodjenja.setter 
    def drzava_rodjenja(self,value):
        if not isinstance(value, str):
            raise ValueError("Mora biti tekstualna vrednost!")
        
        
    def __str__(self):
        return"Radnik {} {}, JMBG: {}, Datum rodjenja: {}, Mesto rodjenja: {}, Drzava rodjenja: {}".format(self._ime, self._prezime, self._jmbg, self._datum_rodjenja, self._mesto_rodjenja, self._drzava_rodjenja)
        
        
        
        
    
    