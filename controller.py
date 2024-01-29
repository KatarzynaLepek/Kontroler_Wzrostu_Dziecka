from dziecko import Dziecko
from datetime import datetime, timedelta

class Controller:
    lista_dzieci = []

    @classmethod
    def utwórz_dziecko(cls):
        imie = input("Podaj imię dziecka:  ")
        plec = input("Wybierz płeć dziecka: Dz/Ch    ")
        plec = plec.lower()
        while plec != "dz" and plec != "ch":
            plec = input("""Żle zdefiniowana płeć.
                         Wybierz płeć dziecka: Dz/Ch    """)
            plec = plec.lower()
        
        data_urodzenia = input("Podaj datę urodzenia dziecka w formacie DD-MM-RRRR: ")
        while True:
            try:
                data_urodzenia = datetime.strptime(data_urodzenia, '%d-%m-%Y')
                if data_urodzenia > datetime.now():
                    print("Twoja data urodzenia jest w przyszłości!")
                    return
                if data_urodzenia < datetime.now() - timedelta(days=365 * 5):
                    print("Aplikacja jest przeznaczona dla dzieci do 5 roku życia!")
                    return
                break
            except ValueError:
                data_urodzenia = input("Nieprawidłowa data. Upewnij się, że podajesz datę urodzenia w formacie DD-MM-RRRR:  ")
        
        if plec == "dz":
            plec = 'dziewczynka'
        if plec == 'ch':
            plec = 'chłopiec'

        data_urodzenia = data_urodzenia.strftime('%d-%m-%Y')

        dziecko = Dziecko(imie, plec, data_urodzenia)
        print ('Utworzyłeś nowe dziecko: ')
        dziecko.print_dziecko()
        cls.lista_dzieci.append(dziecko)

    @classmethod
    def wyswietl_dzieci(cls):
        if cls.lista_dzieci == []:
            print("Nie utworzyłeś jeszcze żadnych dzieci.")
        else:
            for dziecko in cls.lista_dzieci:
                print("------------------")
                dziecko.print_dziecko()
                print("------------------")