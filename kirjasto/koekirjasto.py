import os
import msvcrt
import random
import sys
import time
import json
import configparser

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Tulosta:

    @classmethod
    def TyhjaRuutu(cls):
        os.system('cls')
    
    @classmethod
    def Normaali(cls,teksti):
        print(teksti)

    @classmethod
    def Korostus(cls,teksti):
        print(bcolors.BOLD + teksti + bcolors.ENDC)

    @classmethod
    def Keltainen(cls,teksti):
        print(bcolors.WARNING + teksti + bcolors.ENDC)

    @classmethod
    def Sininen(cls,teksti):
        print(bcolors.OKBLUE + teksti + bcolors.ENDC)

    @classmethod
    def Vihrea(cls,teksti):
        print(bcolors.OKGREEN + teksti + bcolors.ENDC)


class Piirustukset:

    kuvat = {
        1: "lintu.txt",
        2: "hevonen.txt",
        3: "hai.txt"
    }

    kansio = "kuvat/"

    def PirraSatunnainen(self):
        valinta = random.Random().randint(1, len(self.kuvat))
        self.Piirra(self.kansio + self.kuvat.get(valinta))

    def PiirraLintu(self):
        self.Piirra(self.kansio + self.kuvat.get(1))

    def PiirraHevonen(self):
        self.Piirra(self.kansio + self.kuvat.get(2))

    def PiirraKuutiot(self):
        self.Piirra(self.kansio + "kuutiot.txt")

    def PiirraTervetuloa(self):
        print(bcolors.OKBLUE)
        self.Piirra(self.kansio + "tervetuloa.txt")
        print(bcolors.ENDC)

    def PiirraTahti(self):
        self.Piirra(self.kansio + "tahti.txt")

    def Piirra(self, nimi):
        hakemisto = os.path.dirname(__file__)
        tiedostonimi = os.path.join(hakemisto, nimi)
        tiedosto = open(tiedostonimi, mode="r", encoding="utf-8")
        teksti = tiedosto.read()
        tiedosto.closed
        Tulosta.Normaali(teksti)

    def PirraViiva(self):
        Tulosta.Vihrea("--------------------------------------------------------------------------------")

class LueKayttaja:
    def OnkoNumero(self, teksti):
        try:
            int(teksti)
            return True
        except ValueError:
            return False

    def LueNumero(self):
        numero = 0
        luettu = False
        while luettu == False:
            lue = input()
            if self.OnkoNumero(lue) == True:
                numero = int(lue)
                luettu = True
            else:
                sys.stdout.write("\033[1A[\033[2K\b")
        return numero

    def LueVastausSana(self):
        vastaus = ""
        luettu = False
        while luettu == False:
            lue = input()
            if lue != "":
                vastaus = lue
                luettu = True
            else:
                sys.stdout.write("\033[1A[\033[2K\b")
        return vastaus

    def LueVastausKylla(self):
        vastaus = input()
        if vastaus.lower().startswith("k") == True:
            return True
        return False

    def LueVastausKnappi(self):
        while True:
            if msvcrt.kbhit():
                nappi = msvcrt.getwch()
                if nappi.lower() == 'k':
                    return True
                elif nappi.lower() == 'e':
                    return False
            time.sleep(0.04)

    def LueNappi(self):
        while True:
            if msvcrt.kbhit():
                return
            time.sleep(0.04)

    def LueNumeroAjastettu(self, timeout, pituus):
        timer = time.monotonic
        endtime = timer() + timeout
        result = []
        while timer() < endtime:
            if msvcrt.kbhit():
                nappi = msvcrt.getwch()
                if nappi == '\b' and len(result) > 0:
                    result = result[:-1]
                    msvcrt.putwch(nappi)

                elif self.OnkoNumero(nappi) or nappi == '\r' or (len(result) == 0 and nappi == '-'):
                    result.append(nappi)
                    msvcrt.putwch(nappi)
                    if len(result) == pituus:
                        lue = ''.join(result)
                        if self.OnkoNumero(lue) == True:
                            numero = int(lue)
                            print()
                            return numero
                        else:
                            result = []
            time.sleep(0.04)
        return -99999999

class LueAsetukset:

    def LueSanastoJson(self,nimi):
        hakemisto = os.path.dirname(__file__)
        tiedostonimi = os.path.join(hakemisto, nimi)
        tiedosto = open(tiedostonimi, mode="r", encoding="utf-8")
        sanastoHakemisto = json.load(tiedosto)
        tiedosto.closed
        return sanastoHakemisto

    def LueIni(self,nimi):
        hakemisto = os.path.dirname(__file__)
        tiedostonimi = os.path.join(hakemisto, nimi)
        config = configparser.ConfigParser()
        config.read(tiedostonimi, encoding="utf-8")
        sanastoHakemisto = config._sections
        return sanastoHakemisto
