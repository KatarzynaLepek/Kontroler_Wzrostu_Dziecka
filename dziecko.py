import datetime

class Dziecko:
    _name = "Dziecko"
    def __init__(self, imie, plec, data_urodzenia):
        self.imie = imie
        self.plec = plec
        self.data_urodzenia = data_urodzenia
        self.dziecko = None
        self.moje_dzieci = []

    def utwórz_dziecko(self):
        imie = input("Podaj imię dziecka:  ")  #zakładam, że można nazwać dziecko jakkolwiek się chce
        
        plec = input("Wybierz płeć dziecka: Dz/Ch    ")
        plec = plec.lower()
        while plec != "dz" and plec != "ch":
            plec = input("""Żle zdefiniowana płeć.
                         Wybierz płeć dziecka: Dz/Ch    """)
            plec = plec.lower()
        
        data_urodzenia = input("Podaj datę urodzenia dziecka w formacie DD-MM-RRRR: ")
        while True:
            try:
                data_urodzenia = datetime.datetime.strptime(data_urodzenia, '%d-%m-%Y')
                break
            except ValueError:
                data_urodzenia = input("Nieprawidłowa data. Upewnij się, że podajesz datę urodzenia w formacie DD-MM-RRRR:  ")
        
        if plec == "dz":
            plec = 'dziewczynka'
        if plec == 'ch':
            plec = 'chłopiec'

        data_urodzenia = data_urodzenia.strftime('%d-%m-%Y')

        self.dziecko = [imie, plec, data_urodzenia]
        print ('Utworzyłeś nowe dziecko: ', self.dziecko)

    def dodaj_dziecko(self):
        if self.dziecko is not None:
            dodaj_dziecko = input("Dodać dziecko do listy Twoich dzieci? T/N    ")
            dodaj_dziecko = dodaj_dziecko.lower()
            while dodaj_dziecko != 't' and dodaj_dziecko != "n":
                dodaj_dziecko = input("""Nieprawidłowa odpowiedź. Upewnij się, że wpisujesz T lub N.  
                                        Dodać dziecko do listy Twoich dzieci? T/N   """)
                dodaj_dziecko = dodaj_dziecko.lower()
            if dodaj_dziecko == 't':
                self.moje_dzieci.append(self.dziecko)
            if dodaj_dziecko == 'n':
                pass
        else:
            print("Nie utworzyłeś jeszcze dziecka.")

    def wyswietl_dzieci(self):
        return self.moje_dzieci

