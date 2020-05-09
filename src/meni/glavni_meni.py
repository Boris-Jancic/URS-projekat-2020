from dekoratori.dekoratori import cleanshell_noinput
from helper.unos import unos as _unos



@cleanshell_noinput
def prikaz_menija() -> None:
    opcija = ""
    while opcija != "q":
        _prikaz_opcija()
        opcija = _unos()
        if opcija == "1":
            _rad_sa_radnicima()
        elif opcija == "2":
            _rad_sa_odsecima()
        elif opcija == "3":
            _rad_sa_delovima()
        elif opcija == "4":
            _rad_sa_automobilima([])  # placeholder list
        elif opcija == "5":
            _rad_sa_kamionima()
        elif opcija == "6":
            _ponovno_ucitavanje_podataka()


@cleanshell_noinput
def _rad_sa_radnicima():
    from meni.radnici_meni import prikaz as prikazi_meni
    prikazi_meni()


@cleanshell_noinput
def _rad_sa_odsecima():
    from meni.odseci_meni import prikaz as prikazi_meni
    prikazi_meni()


@cleanshell_noinput
def _rad_sa_delovima():
    from meni.deo_meni import prikaz as prikazi_meni
    prikazi_meni()
    pass


@cleanshell_noinput
def _rad_sa_automobilima(lista_automobila):
    from meni.automobili_meni import prikaz_menija as prikazi_meni
    prikazi_meni(lista_automobila)


@cleanshell_noinput
def _rad_sa_kamionima():
    from meni.kamion_meni import prikaz as prikazi_meni
    prikazi_meni()
    pass


def _ponovno_ucitavanje_podataka():
    pass


def _prikaz_opcija() -> None:
    print("[1] Rad sa radnicima")
    print("[2] Rad sa odsecima")
    print("[3] Rad sa delovima")
    print("[4] Rad sa automobilima")
    print("[5] Rad sa kamionima")
    print("[6] Ponovno ucitavanje podataka iz sistema")
    print("[q] Izlaz iz aplikacije")


if __name__ == "__main__":
    prikaz_menija()
