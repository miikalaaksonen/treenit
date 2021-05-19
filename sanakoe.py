import os
from peli import Peli
import random
import json
import configparser
from kirjasto.koekirjasto import Tulosta
from kirjasto.koekirjasto import LueKayttaja
from kirjasto.koekirjasto import Piirustukset
from kirjasto.koekirjasto import LueAsetukset

class SanakoeAsetukset:
    maksimiaika = 0
    ajastus = False

class Sanakoe(Peli):

    def Koe(self, otsikko, sanat, asetukset):
        sanalista = list(sanat.keys())
        random.shuffle(sanalista)

        oikeat = 0
        vaarat = 0

        Tulosta.Normaali(otsikko + " valittu\n")
        Tulosta.Normaali("Aloitetaan")
        Piirustukset().PirraViiva()
        for indeksi, kysymys in enumerate(sanalista):
            Tulosta.Normaali("Kysymys (" + str(indeksi+1) +
                             "/" + str(len(sanalista)) + ")")
            Tulosta.Normaali("")
            Tulosta.Keltainen(kysymys + " ?")
            Tulosta.Normaali("")

            oikeavastaus = sanat[kysymys]
            if asetukset.ajastus:
                vastaus = LueKayttaja().LueSanaAjastettu(asetukset.maksimiaika)
            else:
                vastaus = LueKayttaja().LueVastausSana()

            if vastaus == oikeavastaus:
                Tulosta.Korostus("Oikein")
                Piirustukset().PiirraTahti()
                oikeat = oikeat+1
            else:

                Tulosta.Korostus(
                    "Väärin. Oikea vastaus on " + str(oikeavastaus))
                if vastaus.lower() == oikeavastaus.lower():
                    Tulosta.Normaali("Muista isot kirjaimet")
                vaarat = vaarat+1
            Piirustukset().PirraViiva()

        Tulosta.Normaali("************************")
        Tulosta.Normaali("* Oikein " + str(oikeat) +
                         " * Väärin " + str(vaarat)+" *")
        Tulosta.Normaali("************************")

        if vaarat == 0:
            Tulosta.Normaali("Erittäin hyvä!")
            Piirustukset().PirraSatunnainen()
            Tulosta.Normaali("")

        else:
            Tulosta.Normaali("Harjoittele vielä!")

    def AloitaPeli(self):
        asetuksetIni = self.Aloita()
        asetukset = SanakoeAsetukset()
        asetukset.maksimiaika = asetuksetIni.getint("sanakoe","maksimiaika")

        sanastot = LueAsetukset().LueIni("../sanakoe/sanasto.ini")

        for indeksi, sanasto in enumerate(sanastot):
            Tulosta.Normaali(str(indeksi+1) + ". " + sanasto)

        sanastonValinta = LueKayttaja().LueNumeroAjastettu(99999, len(str(len(sanastot))))

        Tulosta.Korostus("Haluatko "+str(asetukset.maksimiaika) +
                         "s ajastuksen käyttöön? (k/e)")
        asetukset.ajastus = LueKayttaja().LueVastausKnappi()
        if asetukset.ajastus:
            Tulosta.Normaali("Ajastus käytössä")
        else:
            Tulosta.Normaali("Ajastus ei käytössä")

        jatka = True
        while jatka == True:
            Piirustukset().PirraViiva()
            otsikko = [*sanastot][sanastonValinta-1]
            sanasto = sanastot[otsikko]
            self.Koe(otsikko, sanasto, asetukset)
            jatka = self.Jatka()
        self.Lopeta()


if __name__ == "__main__":
    peli = Sanakoe()
    peli.AloitaPeli()
