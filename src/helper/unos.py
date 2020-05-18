from io_writer import automobil_io
from io_writer import radnik_io 
from io_writer import odsek_io

def unos() -> str:
    return input("Izaberite jednu od opcija: ")


def upis_u_fajl():
    automobil_io.dump()
    radnik_io.upis()
    odsek_io.upis()
