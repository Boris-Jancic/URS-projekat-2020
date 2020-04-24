from dekoratori.dekoratori import isgreaterthan, wrapisinstance, isinrange, isnotempty
from modeli.identifikacija import Identifikacija


class Automobil(Identifikacija):
    def __init__(self, oznaka: float, duzina: float, sirina: float, visina: float, tezina: float, model: str, broj_vrata: int):
        super().__init__(oznaka)
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina
        self.tezina = tezina
        self.model = model
        self.broj_vrata = broj_vrata

    def __str__(self):
        return f"Automobil modela {self._model} dimenzija(d,s,v)={self._duzina}x{self._sirina}x{self._visina}m, " + \
            f"tezine {self._tezina}kg sa {self._broj_vrata} vrata"

    @property
    def duzina(self):
        return self._duzina

    @duzina.setter
    @wrapisinstance((float,int))
    @isgreaterthan(0)
    def duzina(self, duzina):
        self._duzina = duzina

    @property
    def sirina(self):
        return self._sirina

    @sirina.setter
    @wrapisinstance((float,int))
    @isgreaterthan(0)
    def sirina(self, sirina):
        self._sirina = sirina

    @property
    def visina(self):
        return self._visina

    @visina.setter
    @wrapisinstance((float,int))
    @isgreaterthan(0)
    def visina(self, visina):
        self._visina = visina

    @property
    def tezina(self):
        return self._tezina

    @tezina.setter
    @wrapisinstance((float,int))
    @isgreaterthan(0)
    def tezina(self, tezina):
        self._tezina = tezina

    @property
    def model(self):
        return self._model

    @model.setter
    @wrapisinstance(str)
    @isnotempty
    def model(self, model):
        self._model = model

    @property
    def broj_vrata(self):
        return self._broj_vrata

    @broj_vrata.setter
    @wrapisinstance(int)
    @isinrange((1,5))
    def broj_vrata(self, broj_vrata):
        self._broj_vrata = broj_vrata