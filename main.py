from dziecko import Dziecko

dziecko = Dziecko('d','d','d')

while True:
    print ("""\n Witaj w Kontrolerze Wzrostu Dziecka!
           Wybierz opcję z poniższego menu: 
                1 - Dodaj dziecko
                2 - Moje dzieci
                3 - Wyjdź
           Wybieram:        """)
    wybor = input()
    if wybor == "1":
        dziecko.utwórz_dziecko()
        dziecko.dodaj_dziecko()
    elif wybor == "2":
        print(f"Moje dzieci to: {dziecko.wyswietl_dzieci()}")
    elif wybor == "3":
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj jeszcze raz.")
print("Dziękuję, koniec programu")

