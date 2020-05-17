from io_writer import automobil_io


def unos() -> str:
    return input("Izaberite jednu od opcija: ")


def upis_u_fajl():
    automobil_io.dump()
