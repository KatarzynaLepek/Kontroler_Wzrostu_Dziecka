import datetime

class Dziecko:
    _name = "Dziecko"
    def __init__(self, imie, plec, data_urodzenia):
        self.imie = imie
        self.plec = plec
        self.data_urodzenia = data_urodzenia

    def print_dziecko(self):
        print(f"Imię: {self.imie}")
        print(f"Płeć: {self.plec}")
        print(f"Data Urodzenia: {self.data_urodzenia}")

