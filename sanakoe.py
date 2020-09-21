import os
import random
import sys
import time
import msvcrt
import json
from kirjasto.koekirjasto import *

class Sanasto:
    def LueSanasto(self):
        nimi = "sanakoe\sanasto.json"
        hakemisto = os.path.dirname(__file__)
        tiedostonimi = os.path.join(hakemisto, nimi)
        tiedosto = open(tiedostonimi, mode="r", encoding="utf-8")
        sanastoHakemisto = json.load(tiedosto)
        tiedosto.closed
        return sanastoHakemisto

class Sanakoe:

    def Koe(self, otsikko, sanat):
        sanalista = list(sanat.keys())
        random.shuffle(sanalista)

        oikeat = 0
        vaarat = 0

        print(otsikko + " valittu\n")
        print("Aloitetaan")
        Piirustukset().PirraViiva()
        for indeksi, kysymys in enumerate(sanalista):
            print("Kysymys (" + str(indeksi+1) + "/" + str(len(sanalista)) + ")")
            print("")
            print(bcolors.WARNING + kysymys +" ?" + bcolors.ENDC)
            print("")

            oikeavastaus = sanat[kysymys]
            vastaus = LueKayttaja().LueVastausSana()

            if vastaus == oikeavastaus:
                print(bcolors.BOLD + "Oikein" + bcolors.ENDC)
                oikeat = oikeat+1
            else:

                print(bcolors.BOLD + "Väärin. Oikea vastaus on " +
                      str(oikeavastaus) + bcolors.ENDC)
                if vastaus.lower() == oikeavastaus.lower():
                    print("Muista isot kirjaimet")
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

    def AloitaPeli(self):
        jatka = True
        Piirustukset().PiirraTervetuloa()
        print("")

        sanastot = Sanasto().LueSanasto()

        for indeksi, sanat in enumerate(sanastot):
            print(str(indeksi+1) + ". " + sanat)

        sanastonValinta = LueKayttaja().LueNumero()

        while jatka == True:
            otsikko = [*sanastot][sanastonValinta-1]
            sanasto = sanastot[otsikko]
            self.Koe(otsikko,sanasto)
            print(bcolors.BOLD + "Pelaataanko uudestaan? (k/e)" + bcolors.ENDC)
            jatka = LueKayttaja().LueVastausKnappi()
            os.system('cls')
        print("Kiva kun pelasit ja opit uutta!")
        print("")


os.system('cls')
peli = Sanakoe()
peli.AloitaPeli()
print("Paina jotain nappia lopettaaksesi")
LueKayttaja().LueNappi()
