from io_loader.radnik_io import RadnikLoader

FILE_PATH = "data/radnici.txt"

def upis():
    with open(FILE_PATH, "w+") as file:
        for i in RadnikLoader.get_ucitani_radnici():
            file.write(i.to_data() + "\n")