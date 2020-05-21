from io_loader.kamion_io import KamioniLoader

FILE_PATH = "data/kamioni.txt"


def dump() -> None:
    with open(FILE_PATH, "w+") as _file:
        for _ in KamioniLoader.get_loaded_trucks():
            _file.write(_.to_data() + "\n")