import random
from kirjasto.koekirjasto import Tulosta
from kirjasto.koekirjasto import LueKayttaja
from kirjasto.koekirjasto import Piirustukset
from kirjasto.koekirjasto import LueAsetukset


class Kertolaskupeli:

    def TulostaVinkit(self, kysymys, taulunnumero):
        edellinen = (kysymys-1) * taulunnumero
        seuraava = (kysymys+1) * taulunnumero
        if edellinen > seuraava:
            vaihto = edellinen
            edellinen = seuraava
            seuraava = vaihto
        Tulosta.Normaali("Vinkki: isompi kuin " + str(edellinen) +
                         " pienempi kuin " + str(seuraava))

    def Taulutesti(self, taulunnumero, maksimi, vinkit, ajastus, maksimiaika):
        numerot = list(range(1, maksimi+1))
        random.shuffle(numerot)

        oikeat = 0
        vaarat = 0

        Tulosta.Normaali("Kertotaulu " + str(taulunnumero) + " valittu.\n")
        Tulosta.Normaali("Aloitetaan")
        Piirustukset().PirraViiva()
        for indeksi, kysymys in enumerate(numerot):
            Tulosta.Normaali(
                "Kysymys (" + str(indeksi+1) + "/" + str(maksimi) + ")")
            Tulosta.Normaali("")
            Tulosta.Keltainen("Paljonko on " + str(kysymys) +
                              " x " + str(taulunnumero)+" ?")
            Tulosta.Normaali("")
            if vinkit:
                self.TulostaVinkit(kysymys, taulunnumero)

            aika = 999999
            if ajastus:
                aika = maksimiaika

            oikeavastaus = kysymys * taulunnumero
            vastausnumero = LueKayttaja().LueNumeroAjastettu(aika, len(str(oikeavastaus)))

            if vastausnumero == oikeavastaus:
                Tulosta.Korostus("Oikein")
                Piirustukset().PiirraTahti()
                oikeat = oikeat+1
            else:
                Tulosta.Korostus(
                    "Väärin. Oikea vastaus on " + str(oikeavastaus))
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

        asetukset = LueAsetukset().HaeIni("../asetukset.ini")
        maksimi = asetukset.getint("kertotaulu", "maksimi")
        maksimiaika = asetukset.getint("kertotaulu", "maksimiaika")
        vinkit = asetukset.getboolean("kertotaulu", "vinkit")

        Piirustukset().PiirraTervetuloa()
        Piirustukset().PiirraKuutiot()
        Tulosta.Normaali("")
        Tulosta.Normaali(
            "Anna kertotaulun numero jota haluat haluat harjoitella. Mikä vain kokonaisluku")
        taulunnumero = LueKayttaja().LueNumero()

        if vinkit:
            Tulosta.Normaali("\nVinkit käytössä\n")
        else:
            Tulosta.Normaali("\nVinkit ei käytössä\n")

            Tulosta.Normaali("")
        Tulosta.Korostus("Haluatko "+str(maksimiaika) +
                         "s ajastuksen käyttöön? (k/e)")
        ajastus = LueKayttaja().LueVastausKnappi()
        if ajastus:
            Tulosta.Normaali("Ajastus käytössä")
        else:
            Tulosta.Normaali("Ajastus ei käytössä")

        jatka = True
        while jatka == True:
            Piirustukset().PirraViiva()
            self.Taulutesti(taulunnumero, maksimi,
                            vinkit, ajastus, maksimiaika)
            Tulosta.Korostus("Pelaataanko uudestaan? (k/e)")
            jatka = LueKayttaja().LueVastausKnappi()
            Tulosta.TyhjaRuutu()
        Tulosta.Normaali("Kiva kun pelasit ja opit uutta!")
        Tulosta.Normaali("")


def Aloita():
    Tulosta.TyhjaRuutu()
    peli = Kertolaskupeli()
    peli.AloitaPeli()
    Piirustukset().PirraViiva()
    Tulosta.Normaali("Paina jotain nappia lopettaaksesi")
    LueKayttaja().LueNappi()


if __name__ == "__main__":
    Aloita()
