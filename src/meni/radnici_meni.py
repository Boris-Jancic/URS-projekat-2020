from helper.unos import unos as _unos
from io_loader.radnik_io import RadnikLoader
from helper.oznaka_validator import OznakaError
from modeli.radnik import Radnik

def prikaz():
    opcija = ""

    while opcija != "q":
        _opcije()
        opcija = _unos()

        if opcija == "1":
            _prikaz_radnika()
        if opcija == "2":
            _dodavanje_radnika()
        if opcija == "3":
            _izmena_radnika()
        if opcija == "4":
            _pretraga_radnika()
        if opcija == "5":
            _sort_po_imenu()
        if opcija == "6":
            _sort_po_prezimenu()
        if opcija == "7":
            _sort_po_datumu()


def _opcije():
    print("[1] Prikaz svih radnika ")
    print("[2] Dodavanje novog radnika ")
    print("[3] Izmena vrednosti radnika ")
    print("[4] Pretraga radnika")
    print("[5] Sortiranje radnika po imenu ")
    print("[6] Sortiranje radnika po prezimenu ")
    print("[7] Sortiranje radnika po datumu rodjenja ")


def _prikaz_radnika():
    for i in RadnikLoader.get_ucitani_radnici():
        print(i)


def _dodavanje_radnika():
    try:
        oznaka = input("\nUnesite oznaku: ")
        ime = input("Unesite ime: ")
        prezime = input("Unesite prezime: ")
        jmbg = input("Unesite jmbg: ")
        datum_rodjenja = input("Unesite datum rodjenja (u formatu dd/mm/yyyy): ")
        mesto_rodjenja = input("Unesite mesto rodjenja: ")
        drzava_rodjenja = input("Unesite drzavu rodjenja: ")
        odsek_id = input("Unesite ID odseka u kojem se radnik nalazi: ")
        
        radnik = Radnik(oznaka, ime, prezime, jmbg, datum_rodjenja, mesto_rodjenja, drzava_rodjenja, odsek_id)
        RadnikLoader.get_ucitani_radnici().add(radnik)
    
    except ValueError:
        print("Neispravni podaci, pokusajte ponovo!")

    except OznakaError:
        print("Uneta oznaka je vec iskoriscena!")


def _izmena_radnika():
    pass


def _pretraga_radnika():
    pass


def _sort_po_imenu():
    pass


def _sort_po_prezimenu():
    pass


def _sort_po_datumu():
    pass
