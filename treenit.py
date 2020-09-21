import os
import sys
import sanakoe
import kertotaulu
from kirjasto.koekirjasto import LueKayttaja
from kirjasto.koekirjasto import Piirustukset


def main():
    os.system('cls')

    pelit = {"sanakoe": sanakoe.Sanakoe(), "kertotaulut": kertotaulu.Kertolaskupeli()}

    for indeksi, sanat in enumerate(pelit):
        print(str(indeksi+1) + ". " + sanat)

    peliValinta = LueKayttaja().LueNumeroAjastettu(99999,len(str(len(pelit))))
    os.system('cls')
    pelinNimi = [*pelit][peliValinta-1]
    peli = pelit[pelinNimi]
    peli.AloitaPeli()

    Piirustukset().PirraViiva()
    print("Paina jotain nappia lopettaaksesi")
    LueKayttaja().LueNappi()

if __name__ == "__main__":
    main()
