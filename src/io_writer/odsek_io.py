from io_loader.odsek_io import OdsekLoader

FILE_PATH = "data/odseci.txt"


def upis():
    with open(FILE_PATH, "w+") as file:
        for i in OdsekLoader.get_ucitani_odseci():
            file.write(i.to_data() + "\n")