from io_loader.automobil_io import AutomobilLoader
from io_loader.deo_io import DeoLoader
from io_loader.kamion_io import KamioniLoader


class OznakaError(Exception):
    pass


def validacija_oznake_za_automobil(oznaka: str):
    for _ in AutomobilLoader.get_loaded_cars():
        if _.oznaka == oznaka:
            raise OznakaError("Neispravna oznaka!")


def validacija_oznake_za_deo(oznaka: str):
    for _ in DeoLoader.get_loaded_parts():
        if _.oznaka == oznaka:
            raise OznakaError("Neispravna oznaka!")


def validacija_oznake_za_kamion(oznaka: str):
    for _ in KamioniLoader.get_loaded_trucks():
        if _.oznaka == oznaka:
            raise OznakaError("Neispravna oznaka!")