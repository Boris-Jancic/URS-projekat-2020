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
         
def _unos():
    return input("Izaberite jednu od opcija: ")

def _opcije():
    print("[1] Prikaz svih radnika ")
    print("[2] Dodavanje novog radnika ")
    print("[3] Izmena vrednosti radnika ")
    print("[4] Pretraga radnika")
    print("[5] Sortiranje radnika po imenu ")
    print("[6] Sortiranje radnika po prezimenu ")
    print("[7] Sortiranje radnika po datumu rodjenja ")
    
def _prikaz_radnika():
    pass 

def _dodavanje_radnika():
    pass 

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