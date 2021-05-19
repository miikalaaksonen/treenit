import secrets
from peli import Peli
from kirjasto.koekirjasto import Tulosta
from kirjasto.koekirjasto import LueKayttaja
from kirjasto.koekirjasto import Piirustukset

class TauluAsetukset:
    maksimi = 0
    maksimiaika = 0
    vinkit = False
    ajastus = False
    tekijakysely = False

class Kertolaskupeli(Peli):

    def TulostaVinkit(self, kysymys, taulunnumero):
        edellinen = (kysymys-1) * taulunnumero
        seuraava = (kysymys+1) * taulunnumero
        if edellinen > seuraava:
            vaihto = edellinen
            edellinen = seuraava
            seuraava = vaihto
        Tulosta.Normaali("Vinkki: isompi kuin " + str(edellinen) +
                         " pienempi kuin " + str(seuraava))

    def Taulutesti(self, taulunnumero, asetukset):
        numerot = list(range(1, asetukset.maksimi+1))
        secrets.SystemRandom().shuffle(numerot)

        oikeat = 0
        vaarat = 0

        Piirustukset().PirraViiva()
        Tulosta.Normaali("Kertotaulu " + str(taulunnumero) + " valittu.\n")
        Tulosta.Normaali("Aloitetaan")
        Piirustukset().PirraViiva()
        for indeksi, kysymys in enumerate(numerot):
            Tulosta.Normaali(
                "Kysymys (" + str(indeksi+1) + "/" + str(asetukset.maksimi) + ")")
            Tulosta.Normaali("")
            if asetukset.tekijakysely:
                tulo = kysymys * taulunnumero
                Tulosta.Keltainen("Paljonko on " + str(taulunnumero) +
                                " * X = " + str(tulo)+" ?")
                oikeavastaus = kysymys

            else:
                Tulosta.Keltainen("Paljonko on " + str(kysymys) +
                                " * " + str(taulunnumero)+" ?")
                oikeavastaus = kysymys * taulunnumero
            Tulosta.Normaali("")
            if asetukset.vinkit:
                self.TulostaVinkit(kysymys, taulunnumero)

            aika = 999999
            if asetukset.ajastus:
                aika = asetukset.maksimiaika

            vastausnumero = LueKayttaja().LueNumeroAjastettu(aika, len(str(oikeavastaus)))

            if vastausnumero == oikeavastaus:
                Tulosta.Korostus("Oikein")
                Piirustukset().PirraLaivaAuto()
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
        asetuksetIni = self.Aloita()
        asetukset = TauluAsetukset()
        asetukset.maksimi = asetuksetIni.getint("kertotaulu", "maksimi")
        asetukset.maksimiaika = asetuksetIni.getint("kertotaulu", "maksimiaika")
        asetukset.vinkit = asetuksetIni.getboolean("kertotaulu", "vinkit")
        asetukset.tekijakysely = asetuksetIni.getboolean("kertotaulu", "tekijakysely")

        Piirustukset().PiirraKuutiot()
        Tulosta.Normaali("")
        Tulosta.Normaali(
            "Anna kertotaulun numero jota haluat haluat harjoitella. Mikä vain kokonaisluku")
        taulunnumero = LueKayttaja().LueNumero()

        if not asetukset.tekijakysely:
            if asetukset.vinkit:
                Tulosta.Normaali("\nVinkit käytössä\n")
            else:
                Tulosta.Normaali("\nVinkit ei käytössä\n")

            Tulosta.Normaali("")
        Tulosta.Korostus("Haluatko "+str(asetukset.maksimiaika) +
                         "s ajastuksen käyttöön? (k/e)")
        asetukset.ajastus = LueKayttaja().LueVastausKnappi()
        if asetukset.ajastus:
            Tulosta.Normaali("Ajastus käytössä")
        else:
            Tulosta.Normaali("Ajastus ei käytössä")

        jatka = True
        while jatka == True:
            self.Taulutesti(taulunnumero, asetukset)
            jatka = self.Jatka()
        self.Lopeta()


if __name__ == "__main__":
    peli = Kertolaskupeli()
    peli.AloitaPeli()
