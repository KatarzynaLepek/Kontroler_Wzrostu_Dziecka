# Kontroler Wzrostu i Wagi Dziecka

Aplikacja powstała w ramach zaliczenia projektu na studiach podyplomowych Tester oprogramowania na Uniwersytecie WSB Merito. Temat pracy: "Projekt python - program śledzący wzrost i wagę dziecka, z obsługą biblioteki pandas oraz matplotlib."

Kontroler to aplikacja konsolowa i służy rodzicom dzieci w wieku 0-5 lat do śledzenia rozwoju dzieci. Pozwala nanieść pomiary na wykres siatek centylowych opracowanych przez WHO, aby lepiej orientować się, czy rozwój następuje prawidłowo.

## Wykorzystane biblioteki

* `matplotlib` 3.7.2
* `numpy` 1.25.1
* `pandas` 2.2.0
* `datetime`/`dateutil` 5.4
* `sqlite3`

## Wersje

* Python 3.11.2

## Struktura projektu

* `controller.py` : Ten plik zawiera klasę Controller, która jes odpowiedzialna za logikę sterowania w ninejszej aplikacji.
* `dziecko.py` : Plik zawiera klasę Dziecko, która przechowuje dane dotyczące dziecka, takie jak ID, imię, płec oraz datę urodzenia.
* `main.py` : Plik główny, który zawiera kod do uruchomienia aplikacji oraz interakcję z użytkownikiem.
* `pomiar.py` : Plik zawiera klasę Pomiar, która przechowuje dane dotyczące pomiarów fizycznych dziecka, takie jak wzrost i waga.
* `requirements.txt` : Plik zawiera listę zależności (bibliotek Pythona) niezbędnych do uruchomienia projektu wraz z ich wersjami.
* `wykres.py` : Plik zawiera funkcje do generowania wykresów i wizualizacji danych na podstawie pomiarów oraz na podstawie danych opracowanych przez WHO.

## Instalacja programu

1. Aby zainstalować ten program, należy pobrać kod źródłowy z tego repozytorium GitHub, np. poprzez sklonowanie za pomocą polecenia git:

git clone https://github.com/KatarzynaLepek/Kontroler_Wzrostu_Dziecka.git

Można także pobrać kod źródłowy jako archiwum ZIP i rozpakować go na swoim komputerze.

2. Następnie należy zainstalować wskazane wyżej biblioteki Pythona za pomocą polecenia pip install (jeśli takowych nie ma). Uwaga: Biblioteka `sqlite3` jest częścią standardowej biblioteki Pythona i nie wymaga osobnej instalacji.

3. Uruchamianie programu. Należy przejść do katalogu, gdzie znajduje się kod źródłowy programu, a następnie wykonać go za pomogą interpretera Pythona:

python main.py

## Użytkowanie programu

Ten program służy do monitorowania wzrostu i masy ciała dzieci oraz generowania wykresów siatek centylowych na podstawie pomiarów. Po zainstalowaniu wszystkich zależności i wykonaniu pliku `main.py` uruchomi się główne menu programu. Można w nim utworzyć dziecko, a następnie dodać dla tego dziecka pomiary wzorstu w (cm) oraz wagi w (kg) wraz z datą pomiaru.
Menu pozwala na wyświetlenie wprowadzonych pomiarów dla dzieci, program także pyta użytkownika, czy wyświetlić wykresy wzrostu, a następnie wagi oraz zbiorczej tabeli z danymi.
Program komunikuje się z użytkownikiem poprzez terminal, wyświetlając pomocne komunikaty i oczekując wprowadzenia wskazanych informacji. Aplikacja przechowuje wszystkie dane (dziecko wraz z jego pomiarami), dlatego użytkownik może wprowadzać kolejne wartości wzrostu i wagi i porównywać ich zmiany w czasie. Dzięki temu prostemu procesowi użytkownik może łatwo monitorować rozwój fizyczny dzieci i uzyskać wizualne reprezentacje siatek centylowych na podstawie tych pomiarów.

