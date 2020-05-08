from dekoratori.dekoratori import isgreaterthan, wrapisinstance, isinrange, isnotempty
from modeli.identifikacija import Identifikacija

class Kamion(Identifikacija):
    def __init__(self, oznaka: str, model: str, max_tezina: float, broj_automobila: int):
        super().__init__(oznaka)
        self.model = model
        self.max_tezina = max_tezina
        self.broj_automobila = broj_automobila
        self._lista_automobila = set()

    def link_automobil(self, automobil):
        if automobil is not None:
            automobil.kamion = self

    @staticmethod
    def unlink_automobil(automobil):
        if not (automobil is None):
            automobil.kamion = None

    @property
    def lista_automobila(self):
        return self._lista_automobila


    @property
    def model(self):
        return self._model

    @model.setter
    @wrapisinstance(str)
    @isnotempty
    def model(self, model):
        self._model = model

    @property
    def max_tezina(self):
        return self._max_tezina

    @max_tezina.setter
    @wrapisinstance(int)
    @isgreaterthan(0)
    def max_tezina(self, max_tezina):
        self._max_tezina = max_tezina

    @property
    def broj_automobila(self):
        return self._broj_automobila

    @broj_automobila.setter
    @isinrange((1, 7))
    def broj_automobila(self, broj_automobila):
        self._broj_automobila = broj_automobila

    def __str__(self):
        return "{0}, {1}, {2}, {3}".format(self._oznaka, self._model, self._max_tezina, self._broj_automobila)
