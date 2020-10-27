import os
import random
import json
import configparser
from kirjasto.koekirjasto import Tulosta
from kirjasto.koekirjasto import LueKayttaja
from kirjasto.koekirjasto import Piirustukset
from kirjasto.koekirjasto import LueAsetukset

class Sanakoe:

    def Koe(self, otsikko, sanat):
        sanalista = list(sanat.keys())
        random.shuffle(sanalista)

        oikeat = 0
        vaarat = 0

        Tulosta.Normaali(otsikko + " valittu\n")
        Tulosta.Normaali("Aloitetaan")
        Piirustukset().PirraViiva()
        for indeksi, kysymys in enumerate(sanalista):
            Tulosta.Normaali("Kysymys (" + str(indeksi+1) + "/" + str(len(sanalista)) + ")")
            Tulosta.Normaali("")
            Tulosta.Keltainen(kysymys +" ?")
            Tulosta.Normaali("")

            oikeavastaus = sanat[kysymys]
            vastaus = LueKayttaja().LueVastausSana()

            if vastaus == oikeavastaus:
                Tulosta.Korostus("Oikein")
                oikeat = oikeat+1
            else:

                Tulosta.Korostus("Väärin. Oikea vastaus on " + str(oikeavastaus))
                if vastaus.lower() == oikeavastaus.lower():
                    Tulosta.Normaali("Muista isot kirjaimet")
                vaarat = vaarat+1
            Piirustukset().PirraViiva()

        Tulosta.Normaali("************************")
        Tulosta.Normaali("* Oikein " + str(oikeat) + " * Väärin " + str(vaarat)+" *")
        Tulosta.Normaali("************************")

        if vaarat == 0:
            Tulosta.Normaali("Erittäin hyvä!")
            Piirustukset().PirraSatunnainen()
            Tulosta.Normaali("")

        else:
            Tulosta.Normaali("Harjoittele vielä!")

    def AloitaPeli(self):
        jatka = True
        Piirustukset().PiirraTervetuloa()
        Tulosta.Normaali("")

        sanastot = LueAsetukset().LueIni("../sanakoe/sanasto.ini")

        for indeksi, sanasto in enumerate(sanastot):
            Tulosta.Normaali(str(indeksi+1) + ". " + sanasto)

        sanastonValinta = LueKayttaja().LueNumeroAjastettu(99999,len(str(len(sanastot))))

        while jatka == True:
            otsikko = [*sanastot][sanastonValinta-1]
            sanasto = sanastot[otsikko]
            self.Koe(otsikko,sanasto)
            Tulosta.Korostus("Pelaataanko uudestaan? (k/e)")
            jatka = LueKayttaja().LueVastausKnappi()
            Tulosta.TyhjaRuutu()
        Tulosta.Normaali("Kiva kun pelasit ja opit uutta!")
        Tulosta.Normaali("")


def main():
    Tulosta.TyhjaRuutu()
    peli = Sanakoe()
    peli.AloitaPeli()
    Tulosta.Normaali("Paina jotain nappia lopettaaksesi")
    LueKayttaja().LueNappi()

if __name__ == "__main__":
    main()



