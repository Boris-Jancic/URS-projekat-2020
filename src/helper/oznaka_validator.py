from io_loader.automobil_io import AutomobilLoader


class OznakaError(Exception):
    pass


def validacija_oznake_za_automobil(oznaka: str):
    for _ in AutomobilLoader.get_loaded_cars():
        if _.oznaka == oznaka:
            raise OznakaError("Neispravna oznaka!")
