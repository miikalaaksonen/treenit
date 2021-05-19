from kirjasto.koekirjasto import LueKayttaja
from kirjasto.koekirjasto import Piirustukset
from kirjasto.koekirjasto import Tulosta
from kirjasto.koekirjasto import LueAsetukset

class Peli:

    def Aloita(self):
        Tulosta.TyhjaRuutu()
        Piirustukset().PiirraTervetuloa()
        Tulosta.Normaali("")
        return LueAsetukset().HaeIni("../asetukset.ini")

    def Jatka(self):
        Tulosta.Korostus("Pelaataanko uudestaan? (k/e)")
        jatka = LueKayttaja().LueVastausKnappi()
        Tulosta.TyhjaRuutu()
        return jatka

    def Lopeta(self):
        Tulosta.Normaali("Kiva kun pelasit ja opit uutta!")
        Tulosta.Normaali("")
        Piirustukset().PirraViiva()
        Tulosta.Normaali("Paina jotain nappia lopettaaksesi")
        LueKayttaja().LueNappi()