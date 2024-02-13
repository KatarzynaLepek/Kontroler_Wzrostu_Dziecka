from dziecko import Dziecko
from pomiar import Pomiar
from controller import Controller

Dziecko.create_table()
Pomiar.create_table()

while True:
    print ("""\n Witaj w Kontrolerze Wzrostu Dziecka do lat 5!
           Wybierz opcję z poniższego2 menu: 
                1 - Dodaj dziecko
                2 - Moje dzieci
                3 - Wyjdź""")
    wybor = input()
    if wybor == "1":
        Controller.utwórz_dziecko()
    elif wybor == "2":
        Controller.wyswietl_dzieci()
        Controller.rozszerzone_menu()
    elif wybor == "3":
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj jeszcze raz.")
print("Dziękuję, koniec programu")

