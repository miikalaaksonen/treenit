import sanakoe
import kertotaulu
from kirjasto.koekirjasto import LueKayttaja
from kirjasto.koekirjasto import Piirustukset
from kirjasto.koekirjasto import Tulosta


def main():
    Tulosta.TyhjaRuutu()
    pelit = {"sanakoe": sanakoe.Sanakoe(), "kertotaulut": kertotaulu.Kertolaskupeli()}

    for indeksi, sanat in enumerate(pelit):
        Tulosta.Normaali(str(indeksi+1) + ". " + sanat)

    peliValinta = LueKayttaja().LueNumeroAjastettu(99999,len(str(len(pelit))))
    Tulosta.TyhjaRuutu()
    pelinNimi = [*pelit][peliValinta-1]
    peli = pelit[pelinNimi]
    peli.AloitaPeli()

    Piirustukset().PirraViiva()
    Tulosta.Normaali("Paina jotain nappia lopettaaksesi")
    LueKayttaja().LueNappi()

if __name__ == "__main__":
    main()
