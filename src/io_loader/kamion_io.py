from modeli.kamion import Kamion
import gc

FILE_PATH = "data/kamioni.txt"


def load():
    kamioni = set()
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()
        for line in lines:
            split = line.split("|")
            oznaka = split[0]
            model = split[1]
            max_tezina = float(split[2])
            broj_automobila = int(split[3])

            kamion = Kamion(oznaka, model, max_tezina, broj_automobila)
            kamioni.add(kamion)

    return kamioni


class KamioniLoader:
    __loaded_trucks = load()

    @staticmethod
    def reload():
        KamioniLoader.__loaded_trucks = load()
        gc.collect()

    @staticmethod
    def get_loaded_trucks():
        return KamioniLoader.__loaded_trucks
