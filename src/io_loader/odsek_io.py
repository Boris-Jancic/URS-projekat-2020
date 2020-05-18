from modeli.odsek import Odsek
import gc


FILE_PATH = "data/odseci.txt"

def load():
    odseci = set()
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()
        for line in lines:
            split = line.split("|")
            oznaka = split[0]
            ime = split[1]
            max_br_radnika = int(split[2])
            opis = split[3]

            odsek = Odsek(oznaka, ime, max_br_radnika, opis)
            odseci.add(odsek)

    return odseci


class OdsekLoader: 
    __ucitani_odseci = load()

    @staticmethod
    def reload():
        OdsekLoader.__ucitani_odseci = load()
        gc.collect()

    @staticmethod
    def get_ucitani_odseci():
        return OdsekLoader.__ucitani_odseci
