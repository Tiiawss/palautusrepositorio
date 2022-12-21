from tuomari import Tuomari
from luo_peli import LuoPeli

class KiviPaperiSakset:
    def __init__(self, tyyppi: str = "a") -> None:
        self._toinen_pelaaja = LuoPeli().luo_peli(tyyppi)

    def pelaa(self):
        tuomari = Tuomari()

        ekan_valinta = self._ekan_valinta()
        if not self._valinta_ok(ekan_valinta):
            tokan_valinta = "ei tarvetta"
        else:
            tokan_valinta = self._tokan_valinta(ekan_valinta)

        while self._valinta_ok(ekan_valinta) and self._valinta_ok(tokan_valinta):
            tuomari.kirjaa_siirto(ekan_valinta, tokan_valinta)
            print(tuomari)
            ekan_valinta = self._ekan_valinta()
            tokan_valinta = self._tokan_valinta(ekan_valinta)

        print("Kiitos!")
        print(tuomari)
    
    def _ekan_valinta(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _tokan_valinta(self, ensimmaisen_valinta):
        return self._toinen_pelaaja._toisen_pelaajan_siirto(ensimmaisen_valinta)

    def _valinta_ok(self, valinta):
        return valinta == "k" or valinta == "p" or valinta == "s"
            
