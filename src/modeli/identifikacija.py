class Identifikacija:
    def __init__(self, oznaka: str):
        self._oznaka = oznaka
    
    @property
    def oznaka(self):
        return self._oznaka

    @oznaka.setter
    def oznaka(self, vrednost):
        if isinstance(vrednost, str):
            self._oznaka = vrednost
        else:
            raise ValueError("Zadata vrednost nije ispravna!")