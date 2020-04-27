from helper.unos import unos as _unos

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
    print("[1] Prikaz svih delova ")
    print("[2] Dodavanje novog dela ")
    print("[3] Izmena vrednosti dela ")
    print("[4] Pretraga dela")
    print("[5] Sortiranje delova po nazivu ")
    print("[6] Sortiranje delova po tezini ")

def _prikaz_delova():
    pass

def _dodavanje_delova():
    pass

def _izmena_dela():
    pass

def _pretraga_dela():
    pass

def _sort_po_nazivu():
    pass

def  _sort_po_tezini():
    pass