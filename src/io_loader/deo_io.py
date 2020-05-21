from modeli.deo import Deo
import gc

FILE_PATH = "data/delovi.txt"


def load():
    delovi = set()
    with open(FILE_PATH, "r") as _file:
        lines = _file.readlines()
        for line in lines:
            _split = line.split("|")
            oznaka = _split[0]
            naziv = _split[1]
            duzina = float(_split[2])
            sirina = float(_split[3])
            visina = float(_split[4])
            tezina = float(_split[5])
            opis = _split[6]
            pod_delovi = _split[7]
            materijal = _split[8]
            odsek_id = _split[9]

            deo = Deo(oznaka, naziv, duzina, sirina, visina, tezina,
                      opis, pod_delovi, materijal, odsek_id)
            delovi.add(deo)

    return delovi


class DeoLoader:
    __loaded_parts = load()

    @staticmethod
    def reload():
        DeoLoader.__loaded_parts = load()
        gc.collect()

    @staticmethod
    def get_loaded_parts():
        return DeoLoader.__loaded_parts
