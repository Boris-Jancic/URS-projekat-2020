from datetime import datetime

from dekoratori.dekoratori import wrapisinstance, isnotempty
from modeli.identifikacija import Identifikacija


class Radnik(Identifikacija):

    def __init__(self, oznaka, ime, prezime, jmbg, datum_rodjenja, mesto_rodjenja, drzava_rodjenja,odsek_id):
        super().__init__(oznaka)
        self.ime = ime
        self.prezime = prezime
        self.jmbg = jmbg
        self.datum_rodjenja = datum_rodjenja 
        self.mesto_rodjenja = mesto_rodjenja
        self.drzava_rodjenja = drzava_rodjenja
        self._odsek = None
        self.odsek_id = odsek_id

    def link_odsek(self, _odsek):
        if _odsek is not None:
            self.unlink_odsek()
            self._odsek = _odsek
            _odsek.lista_radnika.add(self)

    def unlink_odsek(self):
        if self._odsek is not None:
            self._odsek.lista_radnika.discard(self)
            self._odsek = None


    @property
    def odsek(self):
        return self._odsek

    @odsek.setter
    def odsek(self, value):
        self._odsek = value

    @property
    def ime(self):
        return self._ime

    @ime.setter
    @wrapisinstance(str)
    @isnotempty
    def ime(self, value):
        self._ime = value

    @property
    def prezime(self):
        return self._prezime

    @prezime.setter
    @wrapisinstance(str)
    @isnotempty
    def prezime(self, value):
        self._prezime = value

    @property
    def jmbg(self):
        return self._jmbg

    @jmbg.setter
    @wrapisinstance(str)
    def jmbg(self, value):
        if len(value) != 13:
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

    @property
    def mesto_rodjenja(self):
        return self._mesto_rodjenja

    @mesto_rodjenja.setter
    @wrapisinstance(str)
    def mesto_rodjenja(self, value):
        self._mesto_rodjenja = value

    @property
    def drzava_rodjenja(self):
        return self._drzava_rodjenja

    @drzava_rodjenja.setter
    @wrapisinstance(str)
    def drzava_rodjenja(self, value):
        self._drzava_rodjenja = value
        
        
    @property
    def odsek_id(self):
        return self.odsek_id

    @odsek_id.setter
    @wrapisinstance(str)
    @isnotempty
    def odsek_id(self, value):
        self._odsek_id = value

    def __str__(self):
        return "Radnik {} {}, JMBG: {}, Datum rodjenja: {}, Mesto rodjenja: {}, Drzava rodjenja: {}".format(self._ime,
                                                                                                            self._prezime,
                                                                                                            self._jmbg,
                                                                                                            self._datum_rodjenja,
                                                                                                            self._mesto_rodjenja,
                                                                                                            self._drzava_rodjenja)
