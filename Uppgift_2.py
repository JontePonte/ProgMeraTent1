""" Lösning av uppgift 2 i tentamen 1: John Nordstrand S2300891"""


class Dator:
    'Basklass för datorer'
    def __init__(self, tillverkare='', modell='', processortyp='', installerad_ram='', pris=0):
        # Call methods for car properties
        self.set_tillverkare(tillverkare)
        self.set_modell(modell)
        self.set_processortyp(processortyp)
        self.set_installerad_ram(installerad_ram)
        self.set_pris = pris

    def tillverkare(self):
        'Returnerar datorns tillverkare'
        return self.__tillverkare

    def modell(self):
        'Returnerar datorns modell'
        return self.__modell

    def processorypt(self):
        'Returnerar datorns processortyp'
        return self.__processortyp

    def installerad_ram(self):
        'Returnerar datorns installerade RAM-minne'
        return self.__installerad_ram

    @property
    def pris(self):
        'Returnerar datorns pris'
        return self.__pris


    def set_tillverkare(self, tillverkare):
        'Sätt tillverkare av dator'
        self.__tillverkare = tillverkare

    def set_modell(self, modell):
        'Sätt datorns modell'
        self.__modell = modell

    def set_processortyp(self, processortyp):
        'Sätt datorns processortyp'
        self.__processortyp = processortyp

    def set_installerad_ram(self, installerad_ram):
        'Sätt datorns installerade RAM-minne'
        self.__installerad_ram = installerad_ram

    @pris.setter
    def set_pris(self, pris):
        'Sätt datorns pris'
        assert pris >= 0, ('Negativs pris', pris)
        self.__pris = pris


