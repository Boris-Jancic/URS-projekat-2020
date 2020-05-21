from helper.oznaka_validator import OznakaError, validacija_oznake_za_deo
from helper.unos import unos as _unos
from io_loader.deo_io import DeoLoader
from modeli.deo import Deo


def prikaz():
    opcija = ""

    while opcija != "q":
        _opcije()
        opcija = _unos()

        if opcija == "1":
            _prikaz_delova()
        if opcija == "2":
            _dodavanje_delova()
        if opcija == "3":
            _izmena_dela()
        if opcija == "4":
            _pretraga_dela()
        if opcija == "5":
            _sort_po_nazivu()
        if opcija == "6":
            _sort_po_tezini()


def _opcije():
    print("\n[1] Prikaz svih delova ")
    print("[2] Dodavanje novog dela ")
    print("[3] Izmena vrednosti dela ")
    print("[4] Pretraga dela")
    print("[5] Sortiranje delova po nazivu ")
    print("[6] Sortiranje delova po tezini ")


def _prikaz_delova():
    for x in DeoLoader.get_loaded_parts():
        print(x)

def _dodavanje_delova():
    try:
        oznaka = input("\nUnesite oznaku:").lower()
        naziv = input("Unesite naziv:").lower()
        duzina = float(input("Unesite duzinu:"))
        sirina = float(input("Unesite sirinu:"))
        visina = float(input("Unesite visinu:"))
        tezina = float(input("Unesite tezinu:"))
        opis = input("Unesite opis:").lower()
        broj = int(input("Unesite broj delova:"))
        pod_delovi = int(input("Unesite pod delove:"))
        materijal = input("Unesite materijal:").lower()
        validacija_oznake_za_deo(oznaka)

        deo = Deo(oznaka, naziv, duzina, sirina, visina, tezina, opis, broj, pod_delovi, materijal, "Empty")
        DeoLoader.get_loaded_parts().add(deo)

    except ValueError:
        print("Neispravni podaci, pokusajte ponovo!")

    except OznakaError:
        print("Uneta oznaka je vec iskoriscena!")




def _izmena_dela():
    pass


def _pretraga_dela():
    pass


def _sort_po_nazivu():
    pass


def _sort_po_tezini():
    pass
