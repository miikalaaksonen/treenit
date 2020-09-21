import os
import random
import sys
import time
import msvcrt
from kirjasto.koekirjasto import *


class Kertolaskupeli:

    def TulostaVinkit(self, kysymys, taulunnumero):
        edellinen = (kysymys-1) * taulunnumero
        seuraava = (kysymys+1) * taulunnumero
        if edellinen > seuraava:
            vaihto = edellinen
            edellinen = seuraava
            seuraava = vaihto
        print("Vinkki: isompi kuin " + str(edellinen) +
              " pienempi kuin " + str(seuraava))

    def Taulutesti(self, taulunnumero, maksimi, vinkit, ajastus):
        numerot = list(range(1, maksimi+1))
        random.shuffle(numerot)

        oikeat = 0
        vaarat = 0

        print("Kertotaulu " + str(taulunnumero) + " valittu.\n")
        print("Aloitetaan")
        Piirustukset().PirraViiva()
        for indeksi, kysymys in enumerate(numerot):
            print("Kysymys (" + str(indeksi+1) + "/" + str(maksimi) + ")")
            print("")
            print(bcolors.WARNING + "Paljonko on " + str(kysymys) +
                  " x " + str(taulunnumero)+" ?" + bcolors.ENDC)
            print("")
            if vinkit:
                self.TulostaVinkit(kysymys, taulunnumero)

            aika = 999999
            if ajastus:
                aika = 10

            oikeavastaus = kysymys * taulunnumero
            vastausnumero = LueKayttaja().LueNumeroAjastettu(aika,len(str(oikeavastaus)))

            if vastausnumero == oikeavastaus:
                print(bcolors.BOLD + "Oikein" + bcolors.ENDC)
                Piirustukset().PiirraTahti()
                oikeat = oikeat+1
            else:
                print(bcolors.BOLD + "Väärin. Oikea vastaus on " +
                      str(oikeavastaus) + bcolors.ENDC)
                vaarat = vaarat+1
            Piirustukset().PirraViiva()

        print("************************")
        print("* Oikein " + str(oikeat) + " * Väärin " + str(vaarat)+" *")
        print("************************")

        if vaarat == 0:
            print("Erittäin hyvä!")
            Piirustukset().PirraSatunnainen()
            print("")

        else:
            print("Harjoittele vielä!")

    def AloitaPeli(self, maksimi):
        jatka = True
        Piirustukset().PiirraTervetuloa()
        Piirustukset().PiirraKuutiot()
        print("")
        print("Anna kertotaulun numero jota haluat haluat harjoitella. Mikä vain kokonaisluku")
        taulunnumero = LueKayttaja().LueNumero()

        print(bcolors.BOLD + "Haluatko vinkit käyttöön? (k/e)" + bcolors.ENDC)
        vinkit = LueKayttaja().LueVastausKnappi()
        if vinkit:
            print("Vinkit käytössä")
        else:
            print("Vinkit ei käytössä")

            print("")
        print(bcolors.BOLD + "Haluatko 10s ajastuksen käyttöön? (k/e)" + bcolors.ENDC)
        ajastus = LueKayttaja().LueVastausKnappi()
        if ajastus:
            print("Ajastus käytössä")
        else:
            print("Ajastus ei käytössä")

        while jatka == True:
            Piirustukset().PirraViiva()
            self.Taulutesti(taulunnumero, maksimi, vinkit, ajastus)
            print(bcolors.BOLD + "Pelaataanko uudestaan? (k/e)" + bcolors.ENDC)
            jatka = LueKayttaja().LueVastausKnappi()
        print("Kiva kun pelasit ja opit uutta!")
        print("")


def main():
    os.system('cls')
    peli = Kertolaskupeli()
    peli.AloitaPeli(10)
    Piirustukset().PirraViiva()
    print("Paina jotain nappia lopettaaksesi")
    LueKayttaja().LueNappi()

if __name__ == "__main__":
    main()