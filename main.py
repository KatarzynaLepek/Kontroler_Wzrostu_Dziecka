from dziecko import Dziecko

while True:
    print ("""Witaj w Kontrolerze Wzrostu Dziecka!
           Wybierz opcję z poniższego menu: 
                1 - Dodaj dziecko
                2 - Moje dzieci
                3 - Wyjdź
           Wybieram:        """)
    wybor = input()
    if wybor == "1":
        Dziecko.dodaj_dziecko()
    elif wybor == "2":
        print("Moje dzieci")
    elif wybor == "3":
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj jeszcze raz.")
print("Dziękuję, koniec programu")

