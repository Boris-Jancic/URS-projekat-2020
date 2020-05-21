from helper.oznaka_validator import OznakaError, validacija_oznake_za_kamion
from helper.unos import unos as _unos
from io_loader.kamion_io import KamioniLoader
from modeli.kamion import Kamion


def prikaz():
    opcija = ""

    while opcija != "q":
        _opcije()
        opcija = _unos()

        if opcija == "1":
            _prikaz_kamiona()
        if opcija == "2":
            _dodavanje_kamiona()
        if opcija == "3":
            _izmena_kamiona()
        if opcija == "4":
            _pretraga_kamiona()
        if opcija == "5":
            _sort_po_modelu()
        if opcija == "6":
            _sort_po_max_automobila()
        if opcija == "7":
            _sort_po_tezini_tereta()
        if opcija == "8":
            _prikaz_svih_automobila_na_kamionu()


def _opcije():
    print("\n[1] Prikaz svih kamiona ")
    print("[2] Dodavanje novog kamiona ")
    print("[3] Izmena vrednosti kamiona ")
    print("[4] Pretraga kamiona")
    print("[5] Sortiranje kamiona po modelu ")
    print("[6] Sortiranje kamiona po max broju automobila ")
    print("[7] Sortiranje kamiona po tezini tereta ")
    print("[8] Prikaz svih automobila na datom kamionu ")


def _prikaz_kamiona():
    for x in KamioniLoader.get_loaded_trucks():
        print(x)


def _dodavanje_kamiona():
    try:
        oznaka = input("\nUnesite oznaku:").lower()
        model = input("Unesite model:")
        tezina = float(input("Unesite tezinu:"))
        broj_automobila = int(input("Unesite broj automobila:"))
        validacija_oznake_za_kamion(oznaka)

        kamion = Kamion(oznaka, model, tezina, broj_automobila)
        KamioniLoader.get_loaded_trucks().add(kamion)

    except ValueError:
        print("Neispravni podaci, pokusajte ponovo!")

    except OznakaError:
        print("Uneta oznaka je vec iskoriscena!")


def _izmena_kamiona():
    pass


def _pretraga_kamiona():
    pass


def _sort_po_modelu():
    pass


def _sort_po_max_automobila():
    pass


def _sort_po_tezini_tereta():
    pass


def _prikaz_svih_automobila_na_kamionu():
    pass
