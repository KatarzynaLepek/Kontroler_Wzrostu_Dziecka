import datetime

class Dziecko:
    _name = "Dziecko"
    def __init__(self, imie, plec, data_urodzenia):
        self.imie = imie
        self.plec = plec
        self.data_urodzenia = data_urodzenia

    def dodaj_dziecko():
        imie = input("Podaj imię dziecka:  ")  #zakładam, że można nazwać dziecko jakkolwiek się chce
        
        plec = input("Wybierz płeć dziecka: Dz/Ch    ")
        plec = plec.lower()
        while plec != ("dz" and "ch"):
            plec = input("""Żle zdefiniowana płeć.
                         Wybierz płeć dziecka: Dz/Ch    """)
            plec = plec.lower()
        
        data_urodzenia = input("Podaj datę urodzenia dziecka w formacie DD-MM-RRRR: ")
        while True:
            try:
                data_urodzenia = datetime.datetime.strptime(data_urodzenia, '%d-%m-%Y')
                print("Wprowadzona data urodzenia:  ", data_urodzenia)
                break
            except ValueError:
                data_urodzenia = input("Nieprawidłowa data. Upewnij się, że podajesz datę urodzenia w formacie DD-MM-RRRR:  ")
