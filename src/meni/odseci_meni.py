from helper.unos import unos as _unos


def prikaz():
    
    opcija = ""
    
    while opcija != "q":
        _opcije()
        opcija = _unos()
        
        if opcija == "1":
            _prikaz_odseka()
        if opcija == "2":
            _dodavanje_odseka()
        if opcija == "3":
            _izmena_odseka()
        if opcija == "4":
            _pretraga_odseka()
        if opcija == "5":
            _sort_po_imenu()
        if opcija == "6":
            _sort_po_maxbr_radnika()
        if opcija == "7":
            _prikaz_radnika_odseka()
        if opcija == "8":
            _prikaz_delova_odseka()
            


def _opcije():
    print("[1] Prikaz svih odseka ")
    print("[2] Dodavanje novog odseka ")
    print("[3] Izmena vrednosti odseka ")
    print("[4] Pretraga odseka ")
    print("[5] Sortiranje odseka po imenu ")
    print("[6] Sortiranje odseka po maksimalnom broju radnika")
    print("[7] Prikaz svih radnika koji rade u odgovarajucem odseku ")
    print("[8] Prikaz svih delova koji se proizvode u odgovarajucem odseku")


def _prikaz_odseka():
    pass 

def _dodavanje_odseka():
    pass 

def _izmena_odseka():
    pass 

def _pretraga_odseka():
    pass 

def _sort_po_imenu():
    pass 

def _sort_po_maxbr_radnika():
    pass

def _prikaz_radnika_odseka():
    pass

def _prikaz_delova_odseka():
    pass