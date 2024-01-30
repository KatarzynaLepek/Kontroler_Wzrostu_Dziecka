from dziecko import Dziecko
from pomiar import Pomiar
from datetime import datetime, timedelta

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
    def dodaj_pomiar(cls):
        id = input("Podaj ID dziecka: ")
        if not Dziecko.exists_with_id(id):
            print("Dziecko o podanym ID nie istnieje!")
            return
        
        data_urodzenia = datetime.strptime(Dziecko.get_by_id(id).data_urodzenia, '%d-%m-%Y')

        waga = input("Podaj wagę (kg): ")
        wzrost = input("Podaj wzrost (cm): ")
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

        data_pomiaru = data_pomiaru.strftime('%d-%m-%Y')
        pomiar = Pomiar(id, data_pomiaru, wzrost, waga)
        pomiar.save_to_db()

    @classmethod
    def wyswietl_pomiary(cls):
        id = input("Podaj ID dziecka: ")
        if not Dziecko.exists_with_id(id):
            print("Dziecko o podanym ID nie istnieje!")
            return
        
        pomiary = Pomiar.get_all_for_dziecko(id)
        if len(pomiary) == 0:
            print(f"Brak pomiarów dla ID: {id}")

        for pomiar in pomiary:
            pomiar.print_pomiar()
            print("------------------")
