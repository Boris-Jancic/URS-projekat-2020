from modeli.automobil import Automobil
import gc

FILE_PATH = "data/automobili.txt"


def load():
    var = set()
    with open(FILE_PATH, "r") as _file:
        lines = _file.readlines()
        for line in lines:
            _split = line.split("|")
            oznaka = _split[0]
            duzina = float(_split[1])
            sirina = float(_split[2])
            visina = float(_split[3])
            tezina = float(_split[4])
            model = _split[5]
            broj_vrata = int(_split[6])
            kamion_id = _split[7]

            automobil = Automobil(oznaka, duzina, sirina, visina, tezina, model, broj_vrata, kamion_id)
            var.add(automobil)

    return var


class AutomobilLoader:
    __loaded_cars = load()

    @staticmethod
    def reload():
        AutomobilLoader.__loaded_cars = load()
        gc.collect()

    @staticmethod
    def get_loaded_cars():
        return AutomobilLoader.__loaded_cars
