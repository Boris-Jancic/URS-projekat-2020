from io_loader.automobil_io import AutomobilLoader

FILE_PATH = "data/automobili.txt"


def dump() -> None:
    with open(FILE_PATH, "w+") as _file:
        for _ in AutomobilLoader.get_loaded_cars():
            _file.write(_.to_data() + "\n")
