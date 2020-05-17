from meni.glavni_meni import prikaz_menija
from helper.unos import upis_u_fajl

try:
    prikaz_menija()
except (KeyboardInterrupt, SystemExit):
    upis_u_fajl()