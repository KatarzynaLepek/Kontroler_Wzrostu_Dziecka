from dziecko import Dziecko
from controller import Controller
import sqlite3

dziecko = Dziecko('d','d','d')

while True:
    print ("""\n Witaj w Kontrolerze Wzrostu Dziecka do lat 5!
           Wybierz opcję z poniższego menu: 
                1 - Dodaj dziecko
                2 - Moje dzieci
                3 - Wyjdź
           Wybieram:        """)
    wybor = input()
    if wybor == "1":
        Controller.utwórz_dziecko()
    elif wybor == "2":
        Controller.wyswietl_dzieci()
    elif wybor == "3":
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj jeszcze raz.")
print("Dziękuję, koniec programu")

