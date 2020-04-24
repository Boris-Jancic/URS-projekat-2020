from modeli.identifikacija import Identifikacija

class Kamion(Identifikacija):
    def __init__(self,oznaka: str, model: str, max_tezina: float, broj_automobila: int):
        super().__init__(oznaka)
        self.model = model
        self.max_tezina = max_tezina
        self.broj_automobila = broj_automobila

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not model:
            raise ValueError("Zadata vrednost je prazan")
        self._model = model



    @property
    def max_tezina(self):
        return self._max_tezina

    @max_tezina.setter
    def max_tezina(self, max_tezina):
        if(isinstance(max_tezina , int) or max_tezina < 0):
            raise ValueError("Zadata vrednost je manja od nule ili nije decimalna vrednost")
        self._max_tezina = max_tezina



    @property
    def broj_automobila(self):
        return self._broj_automobila

    @broj_automobila.setter
    def broj_automobila(self, broj_automobila):
        if(broj_automobila <= 1 or broj_automobila >= 6):
            raise ValueError("Kamion moze podrzati 1-6 automobila")
        self._broj_automobila = broj_automobila

    
    def __str__(self):
        return "{0}, {1}, {2}, {3}".format(self._oznaka, self._model, self._max_tezina, self._broj_automobila)
