from io_loader.deo_io import DeoLoader

FILE_PATH = "data/delovi.txt"


def dump() -> None:
    with open(FILE_PATH, "w+") as _file:
        for _ in DeoLoader.get_loaded_parts():
            _file.write(_.to_data() + "\n")