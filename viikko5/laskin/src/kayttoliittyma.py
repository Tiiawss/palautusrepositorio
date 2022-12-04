from enum import Enum
from sovelluslogiikka import Sovelluslogiikka
from tkinter import ttk, constants, StringVar

class Summa:
    def __init__(self, sovelluslogiikka, hae_luku):
        self._sovellus = sovelluslogiikka
        self._hae_luku = hae_luku

    def suorita(self):
        self._sovellus.plus(int(self._hae_luku()))

class Erotus:
    def __init__(self, sovelluslogiikka, hae_luku):
        self._sovellus = sovelluslogiikka
        self._hae_luku = hae_luku

    def suorita(self):
        self._sovellus.miinus(int(self._hae_luku()))

class Nollaus:
    def __init__(self, sovelluslogiikka, hae_luku):
        self._sovellus = sovelluslogiikka
        self._hae_luku = hae_luku

    def suorita(self):
        self._sovellus.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, hae_luku):
        self._sovellus = sovelluslogiikka
        self._hae_luku = hae_luku

    def suorita(self):
        self._sovellus.aseta_arvo(int(self._hae_luku()))

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovellus = sovelluslogiikka
        self._root = root
        self._edellinen = 0

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote),
            Komento.KUMOA: Kumoa(sovelluslogiikka, self._anna_edellinen)
        }

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        self._edellinen= self._syote_kentta.get()
        return self._syote_kentta.get()

    def _anna_edellinen(self):
        return self._edellinen

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)
