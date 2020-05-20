from datetime import datetime
from modeli.radnik import Radnik
import gc

FILE_PATH = "data/radnici.txt"

def load():
    radnici = set()
    with open(FILE_PATH, "r") as file:
        lines = file.readlines()
        for line in lines:
            split = line.split("|")
            oznaka = split[0]
            ime = split[1]
            prezime = split[2]
            jmbg = split[3]
            datum_rodjenja = split[4]
            mesto_rodjenja = split[5]
            drzava_rodjenja = split[6]
            odsek_id = split[7]

            radnik = Radnik(oznaka, ime, prezime, jmbg, datum_rodjenja, mesto_rodjenja, drzava_rodjenja, odsek_id)
            radnici.add(radnik)

    return radnici 

class RadnikLoader: 
    __ucitani_radnici = load()

    @staticmethod
    def reload():
        RadnikLoader.__ucitani_radnici = load()
        gc.collect()

    @staticmethod 
    def get_ucitani_radnici():
        return RadnikLoader.__ucitani_radnici
    
    
    
    
    