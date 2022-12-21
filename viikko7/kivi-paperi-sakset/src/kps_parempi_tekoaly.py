from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly:
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)

    def _toisen_pelaajan_valinta(self, ensimmaisen_valinta):
        tokan_valinta = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_valinta}")
        self._tekoaly.aseta_siirto(ensimmaisen_valinta)
        return tokan_valinta