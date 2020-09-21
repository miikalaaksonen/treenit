import os
import sys
import sanakoe
import kertotaulu
from kirjasto.koekirjasto import LueKayttaja
from kirjasto.koekirjasto import Piirustukset

pelit = ["sanakoe", "kertotaulut"]

def main():
    os.system('cls')
    for indeksi, sanat in enumerate(pelit):
        print(str(indeksi+1) + ". " + sanat)

    peliValinta = LueKayttaja().LueNumeroAjastettu(99999,len(str(len(pelit))))
    os.system('cls')
    if peliValinta == 1:
        peli = sanakoe.Sanakoe()
        peli.AloitaPeli()
    elif peliValinta == 2:
        peli  = kertotaulu.Kertolaskupeli()
        peli.AloitaPeli(10)
    Piirustukset().PirraViiva()
    print("Paina jotain nappia lopettaaksesi")
    LueKayttaja().LueNappi()

if __name__ == "__main__":
    main()
