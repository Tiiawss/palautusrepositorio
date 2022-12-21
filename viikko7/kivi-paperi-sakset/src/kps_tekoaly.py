from tekoaly import Tekoaly


class KPSTekoaly:
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _toisen_pelaajan_valinta(self, *siirrot):
        tokan_valinta = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_valinta}")
        return tokan_valinta
