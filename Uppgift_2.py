""" Lösning av uppgift 2 i tentamen 1: John Nordstrand S2300891"""

# ---------------------------------- Klassen Dator ---------------------------------------------

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

    def processortyp(self):
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


# ---------------------------------- Huvudprogram ---------------------------------------------

# Jag gjorde detta till en global variabel, inte så snyggt men funkar
datorer = []

def visa_data():
    """ skriv ut information om alla sparade datorer """
    print('')
    print('  Tillverkare    Modell         Processortyp   Installerat RAM     Pris[kr]')
    print('==============================================================================')
    
    # Loop över alla datorer och skriv ut information
    for dator in datorer:
        til = dator.tillverkare()
        mod = dator.modell()
        pro = dator.processortyp()
        ram = str(dator.installerad_ram())
        pri = str(dator.pris)

        # Padding för att få information att matcha rubriker
        til_padding = max(15 - len(til), 0)
        mod_padding = max(15 - len(mod), 0)
        pro_padding = max(15 - len(pro), 0)
        ram_padding = max(20 - len(ram), 0)

        print(  " "*2 + \
                til + " "*til_padding + \
                mod + " "*mod_padding + \
                pro + " "*pro_padding + \
                ram + " "*ram_padding + \
                pri)
    print("")


def lista():
    """ function för att lagra data om datorer """
    global datorer

    # Ta input om hur många datorer som ska hanteras
    while True:
        try:
            antal_datorer = int(input('Ange antal datorer som ska skrivas in: '))
            if antal_datorer < 1 or antal_datorer > 20:
                raise ValueError
            break
        except ValueError:
            print("Du måste ange ett heltal mellan 1 och 20")

    # Ta input information för varje dator
    for i in range(antal_datorer):
        print('')
        print(f'Dator {i+1}')
        tillverkare = input('Ange tillverkare: ')
        modell = input('Ange modell: ')
        processortyp = input('Ange processortyp: ')

        # Test att RAM är ett vettigt heltal
        while True:
            try:
                installerad_ram = int(input('Ange installerad RAM (GB): '))
                if installerad_ram < 0 or installerad_ram > 100000:
                    raise ValueError
                break
            except ValueError:
                print('RAM-minne brukar ligga mellan 0 och 100000 GB')

        # Test att priset är ett vettigt heltal
        while True:
            try:
                pris = int(input('Ange inköpspris: '))
                if pris < 0 or pris > 100000:
                    raise ValueError
                break
            except ValueError:
                print('Du måste ange ett pris mellan 0 och 100000 kr')

        # Skapa Dator-objekt
        dator = Dator(tillverkare=tillverkare,
                      modell=modell,
                      processortyp=processortyp,
                      installerad_ram=str(installerad_ram),
                      pris=pris)

        # Lägg till datorn bland datorerna
        datorer.append(dator)

    # Skriv ut en snygg lista av alla datorer
    visa_data()

# Denna kör hela a-uppgiften
lista()
