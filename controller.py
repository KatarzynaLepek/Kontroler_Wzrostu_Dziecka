from dziecko import Dziecko
from pomiar import Pomiar
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import wykres

class Controller:

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
                    raise ValueError
                if data_urodzenia < datetime.now() - timedelta(days=365 * 5):
                    print("Aplikacja jest przeznaczona dla dzieci do 5 roku życia!")
                    raise ValueError
                break
            except ValueError:
                data_urodzenia = input("Nieprawidłowa data. Upewnij się, że podajesz datę urodzenia w formacie DD-MM-RRRR:  ")

        if plec == "dz":
            plec = 'dziewczynka'
        if plec == 'ch':
            plec = 'chłopiec'

        data_urodzenia = data_urodzenia.strftime('%d-%m-%Y')

        dziecko = Dziecko(None, imie, plec, data_urodzenia)
        print ('Dziecko utworzone!')
        dziecko.save_to_db()

    @classmethod
    def wyswietl_dzieci(cls):
        lista_dzieci = Dziecko.get_all_from_db()
        if lista_dzieci == []:
            print("Nie utworzyłeś jeszcze żadnych dzieci.")
        else:
            for dziecko in lista_dzieci:
                print("------------------")
                dziecko.print_dziecko()
                print("------------------")

    @classmethod
    def rozszerzone_menu(cls):
        while True:
            print ("""Wybierz opcję z rozszerzonego menu: 
                    1 - Dodaj pomiar dla dziecka
                    2 - Wyświetl pomiary dla dziecka
                    3 - Wyjdź""")
            wybor = input()
            if wybor == "1":
                Controller.dodaj_pomiar()
            elif wybor == "2":
                Controller.wyswietl_pomiary()
            elif wybor == "3":
                break
            else:
                print("Nieprawidłowy wybór. Spróbuj jeszcze raz.")

    @classmethod
    def podaj_wage(cls):
        while True:
            try:
                user_input = input("Podaj wagę (kg): ")
                waga = float(user_input)
                if waga < 0:
                    raise ValueError
                return waga
            except ValueError:
                print("Nieprawidłowa wartość.")

    @classmethod
    def podaj_wzrost(cls):
        while True:
            try:
                user_input = input("Podaj wzrost (cm): ")
                wzrost = float(user_input)
                if wzrost < 0:
                    raise ValueError
                return wzrost
            except ValueError:
                print("Nieprawidłowa wartość.")

    @classmethod
    def dodaj_pomiar(cls):
        id = input("Podaj ID dziecka: ")
        if not Dziecko.exists_with_id(id):
            print("Dziecko o podanym ID nie istnieje!")
            return

        data_urodzenia = datetime.strptime(Dziecko.get_by_id(id).data_urodzenia, '%d-%m-%Y')

        waga = Controller.podaj_wage()
        wzrost = Controller.podaj_wzrost()
        data_pomiaru = input("Podaj datę pomiaru dziecka w formacie DD-MM-RRRR: ")
        while True:
            try:
                data_pomiaru = datetime.strptime(data_pomiaru, '%d-%m-%Y')
                if data_pomiaru > datetime.now():
                    print("Twoja data pomiaru jest w przyszłości!")
                    raise ValueError
                if data_pomiaru < data_urodzenia:
                    print("Data pomiaru jest przed narodzinami dziecka!")
                    raise ValueError
                break
            except ValueError:
                data_pomiaru = input("Nieprawidłowa data. Upewnij się, że podajesz datę urodzenia w formacie DD-MM-RRRR:  ")

        delta = relativedelta(data_pomiaru, data_urodzenia)
        delta = delta.years * 12 + delta.months

        data_pomiaru = data_pomiaru.strftime('%d-%m-%Y')
        pomiar = Pomiar(id, data_pomiaru, wzrost, waga, delta)
        pomiar.save_to_db()

    @classmethod
    def wyswietl_pomiary(cls):
        id = input("Podaj ID dziecka: ")
        if not Dziecko.exists_with_id(id):
            print("Dziecko o podanym ID nie istnieje!")
            return

        pomiary = Pomiar.get_all_for_dziecko(id)
        dziecko = Dziecko.get_by_id(id)

        if len(pomiary) == 0:
            print(f"Brak pomiarów dla ID: {id}")
            return

        for pomiar in pomiary:
            pomiar.print_pomiar()
            print("------------------")

        wykres.rysuj_procentyle_wzrostu(dziecko.plec, pomiary, dziecko.imie)
        wykres.rysuj_procentyle_wagi(dziecko.plec, pomiary, dziecko.imie)