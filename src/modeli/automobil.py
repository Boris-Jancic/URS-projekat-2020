from dekoratori.dekoratori import isgreaterthan, wrapisinstance, isinrange, isnotempty
from modeli.identifikacija import Identifikacija


class Automobil(Identifikacija):
    def __init__(self, oznaka: str, duzina: float, sirina: float, visina: float,
                 tezina: float, model: str, broj_vrata: int, kamion_id: str):
        super().__init__(oznaka)
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina
        self.tezina = tezina
        self.model = model
        self.broj_vrata = broj_vrata
        self._kamion = None
        self.kamion_id = kamion_id
        self._lista_delova = set()

    def to_data(self) -> str:
        if self._kamion is not None:
            k_oznaka = self._kamion.oznaka
        else:
            k_oznaka = "Empty"
        return "|".join(
            [self.oznaka, str(self.duzina), str(self.sirina), str(self.visina), str(self.tezina), self.model,
             str(self._broj_vrata), k_oznaka])

    def __str__(self):
        return f"Automobil modela {self._model} dimenzija(d,s,v)={self._duzina}x{self._sirina}x{self._visina}m, " + \
               f"tezine {self._tezina}kg sa {self._broj_vrata} vrata"

    def link_deo(self, deo):
        if deo is not None:
            deo.unlink_automobil()
            self._lista_delova.add(deo)
            deo.automobil = self

    def unlink_deo(self, deo):
        if deo is not None:
            self.lista_delova.discard(deo)
            deo.automobil = None

    def unlink_kamion(self):
        if self._kamion is not None:
            self._kamion.lista_automobila.discard(self)
            self._kamion = None

    def link_kamion(self, _kamion):
        if _kamion is not None:
            self.unlink_kamion()
            self._kamion = _kamion
            _kamion.lista_automobila.add(self)

    @property
    def lista_delova(self):
        return self._lista_delova

    @property
    def kamion(self):
        return self._kamion

    @kamion.setter
    def kamion(self, value):
        self._kamion = value

    @property
    def kamion_id(self):
        return self._kamion_id

    @kamion_id.setter
    @wrapisinstance(str)
    @isnotempty
    def kamion_id(self, value):
        self._kamion_id = value

    @property
    def duzina(self):
        return self._duzina

    @duzina.setter
    @wrapisinstance((float, int))
    @isgreaterthan(0)
    def duzina(self, duzina):
        self._duzina = duzina

    @property
    def sirina(self):
        return self._sirina

    @sirina.setter
    @wrapisinstance((float, int))
    @isgreaterthan(0)
    def sirina(self, sirina):
        self._sirina = sirina

    @property
    def visina(self):
        return self._visina

    @visina.setter
    @wrapisinstance((float, int))
    @isgreaterthan(0)
    def visina(self, visina):
        self._visina = visina

    @property
    def tezina(self):
        return self._tezina

    @tezina.setter
    @wrapisinstance((float, int))
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
    @isinrange((1, 5))
    def broj_vrata(self, broj_vrata):
        self._broj_vrata = broj_vrata
