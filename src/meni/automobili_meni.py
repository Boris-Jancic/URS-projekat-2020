from dekoratori.dekoratori import cleanshell

__lista_automobila = []


@cleanshell
def prikaz_menija(lista_automobila) -> None:
    global __lista_automobila
    __lista_automobila = lista_automobila

    opcija = ""
    while opcija != "q":
        _prikaz_opcija()
        opcija = _unos()
        if opcija == "1":
            _prikaz_svih_automobila()
        elif opcija == "2":
            _dodavanje_novog_automobila()
        elif opcija == "3":
            _izmena_vrednosti_automobila()
        elif opcija == "4":
            _pretraga_automobila()
        elif opcija == "5":
            _sortiranje_po_modelu()
        elif opcija == "6":
            _sortiranje_po_tezini()
        elif opcija == "7":
            _prikaz_delova_automobila()


def _prikaz_opcija() -> None:
    print("[1] Prikaz svih automobila")
    print("[2] Dodavanje novog automobila")
    print("[3] Izmena vrednosti automobila")
    print("[4] Pretraga automobila")
    print("[5] Sortiranje automobila po modelu")
    print("[6] Sortiranje automobila po tezini")
    print("[7] Prikaz delova automobila")
    print("[q] Izlaz iz menija")


def _unos() -> str:
    return input("Izaberite jednu od opcija: ")


@cleanshell
def _prikaz_svih_automobila() -> None:
    pass


@cleanshell
def _dodavanje_novog_automobila() -> None:
    pass


@cleanshell
def _izmena_vrednosti_automobila() -> None:
    pass


@cleanshell
def _pretraga_automobila() -> None:
    pass


@cleanshell
def _sortiranje_po_modelu() -> None:
    pass


@cleanshell
def _sortiranje_po_tezini() -> None:
    pass


@cleanshell
def _prikaz_delova_automobila() -> None:
    pass
