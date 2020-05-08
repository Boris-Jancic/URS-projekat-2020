from dekoratori.dekoratori import isgreaterthan, wrapisinstance, isnotempty
from modeli.identifikacija import Identifikacija


class Deo(Identifikacija):
    def __init__(self, oznaka: str, naziv: str, duzina: float, sirina: float, visina: float, \
                 tezina: float, opis: str, broj: int, pod_delovi: int, materijal: str):
        super().__init__(oznaka)
        self.naziv = naziv
        self.duzina = duzina
        self.sirina = sirina
        self.visina = visina
        self.tezina = tezina
        self.opis = opis
        self.broj = broj
        self.pod_delovi = pod_delovi
        self.materijal = materijal
        self._automobil = None

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}".format(self._oznaka, self._naziv,
                                                                         self._duzina, self._sirina,
                                                                         self._visina, self._tezina,
                                                                         self._opis, self._broj, self._pod_delovi,
                                                                         self._materijal)

    def unlink_automobil(self):
        self.automobil.lista_delova.discard(self)

    @property
    def automobil(self):
        return self._automobil

    @automobil.setter
    def automobil(self, _automobil):
        if _automobil is not None:
            if self._automobil is not None:
                self._automobil.lista_delova.discard(self)
            self._automobil = _automobil
            _automobil.lista_delova.add(self)
        else:
            self._automobil.lista_delova.discard(self)
            self._automobil = None

    @property
    def naziv(self):
        return self._naziv

    @naziv.setter
    @wrapisinstance(str)
    def naziv(self, naziv):
        self._naziv = naziv

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
    @isgreaterthan(0)
    def sirina(self, sirina):
        self._sirina = sirina

    @property
    def visina(self):
        return self._visina

    @visina.setter
    @isgreaterthan(0)
    def visina(self, visina):
        self._visina = visina

    @property
    def tezina(self):
        return self._tezina

    @tezina.setter
    @isgreaterthan(0)
    def tezina(self, tezina):
        self._tezina = tezina

    @property
    def opis(self):
        return self._opis

    @opis.setter
    @isnotempty
    def opis(self, opis):
        self._opis = opis

    @property
    def broj(self):
        return self._broj

    @broj.setter
    def broj(self, broj):
        self._broj = broj

    @property
    def pod_delovi(self):
        return self._pod_delovi

    @pod_delovi.setter
    @isgreaterthan(-1)
    def pod_delovi(self, pod_delovi):
        self._pod_delovi = pod_delovi

    @property
    def materijal(self):
        return self._materijal

    @materijal.setter
    @isnotempty
    def materijal(self, materijal):
        self._materijal = materijal
