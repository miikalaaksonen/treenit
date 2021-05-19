from kirjasto.koekirjasto import LueKayttaja
from kirjasto.koekirjasto import Piirustukset
from kirjasto.koekirjasto import Tulosta

class Peli:

    def Lopeta(self):
        Tulosta.Normaali("Kiva kun pelasit ja opit uutta!")
        Tulosta.Normaali("")
        Piirustukset().PirraViiva()
        Tulosta.Normaali("Paina jotain nappia lopettaaksesi")
        LueKayttaja().LueNappi()