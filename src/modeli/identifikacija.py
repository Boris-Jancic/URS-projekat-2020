from dekoratori.dekoratori import wrapisinstance

class Identifikacija:
    def __init__(self, oznaka: str):
        self.oznaka = oznaka
    
    @property
    def oznaka(self):
        return self._oznaka

    @oznaka.setter
    @wrapisinstance(str)
    def oznaka(self, vrednost):
        self._oznaka = vrednost
