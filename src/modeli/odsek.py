from dekoratori.dekoratori import wrapisinstance, isnotempty
from modeli.identifikacija import Identifikacija


class Odsek(Identifikacija):

    def __init__(self, oznaka, ime, max_br_radnika, opis):
        super().__init__(oznaka)
        self.ime = ime
        self.max_br_radnika = max_br_radnika
        self.opis = opis
        self._lista_radnika = set()
        self._lista_delova = set()


    def link_radnik(self, radnik):
        if radnik is not None:
            radnik.unlink_odsek()
            self._lista_radnika.add(radnik)
            radnik.odsek = self
    
    
    def unlink_radnik(self, radnik):
        if radnik is not None:
            self._lista_radnika.discard(radnik)
            radnik.odsek = None
            
            
    def link_deo(self, deo):
        if deo is not None:
            deo.unlink_odsek()
            self._lista_delova.add(deo)
            deo.odsek = self
    
    def unlink_deo(self, deo):
        if deo is not None:
            self._lista_delova.discard(deo)
            deo.odsek = None
    
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
        return "Ime odseka: {}, maksimalan broj radnika: {}, opis: {}, lista delova: ".format(self._ime, self._max_br_radnika,
                                                                              self._opis)
