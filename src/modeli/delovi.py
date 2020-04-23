from modeli.identifikacija import Identifikacija

class Delovi(Identifikacija):
    def __init__(self, oznaka: str, naziv: str, duzina: float, sirina: float, visina: float, \
                        tezina : float, opis: str, broj: int, pod_delovi: int, materijal: str ):
        super().__init__(oznaka)
        self._naziv = naziv
        self._duzina = duzina
        self._sirina = sirina
        self._visina = visina
        self._tezina = tezina
        self._opis = opis
        self._broj = broj
        self._pod_delovi = pod_delovi
        self._materijal = materijal
    
    @property
    def naziv(self):
        return self._naziv

    @naziv.setter
    def naziv(self, naziv):
        if (naziv != ""):
            self._naziv = naziv
        else:
            raise ValueError("Ime ne sme biti prazan tekst !")
    
    @property
    def duzina(self):
        return self._duzina
    
    @duzina.setter
    def duzina(self, duzina):
        if (duzina > 0):
            self._duzina = duzina
        else:
            raise ValueError("Ne sme biti dodeljena vrednost manja ili jednaka 0 !")

    
    @property
    def sirina(self):
        return self._sirina

    @sirina.setter
    def sirina(self, sirina):
        if (sirina > 0):
            self._sirina
        else:
            raise ValueError("Ne sme biti dodeljena vrednost manja ili jednaka 0 !")


    @property
    def visina(self):
        return self._visina
    
    @visina.setter
    def visina(self, visina):
        if (visina > 0):
            self._visina
        else:
            raise ValueError("Ne sme biti dodeljena vrednost manja ili jednaka 0 !")


    @property
    def tezina(self):
        return self._tezina
    
    @tezina.setter
    def tezina(self, tezina):
        if (tezina > 0):
            self._tezina
        else:
            raise ValueError("Ne sme biti dodeljena vrednost manja ili jednaka 0 !")

    @property
    def opis(self):
        return self._opis
    
    @opis.setter
    def opis(self, opis):
        self._opis

    
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
    def pod_delovi(self, pod_delovi):
        if (pod_delovi > 0 and pod_delovi is type(int)):
            self._pod_delovi = pod_delovi 
        else:
            raise ValueError("Broj pod-delova ne sme biti manja od nule i mora biti CELOBROJAN broj")

    
    @property
    def materijal(self):
        return self._materijal
    
    @materijal.setter
    def materijal(self, materijal):
        if (materijal != ""):
            self._materijal = materijal
        else:
            raise ValueError("Materijal ne sme biti prazan tekst !")


    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}".format(self._oznaka, \
                self._naziv, self._duzina, self._sirina, self._visina, self._tezina, \
                self._opis, self._broj, self._pod_delovi, self._materijal)
                