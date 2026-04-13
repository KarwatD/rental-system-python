# System dla wypożyczalni gier/filmów (CRUD)

Prosty program dla pracowników wypożyczalni pozwalający na zarządzanie 
użytkownikami oraz towarem: wyświetlanie, dodawanie, wypożyczanie oraz zwracanie

# Funkcjonalności

* Zarządzanie użytkownikami i towarem - dodawanie oraz wyświetlanie z pliku
* System wypożyczeń i zwrotów - automatyczna aktualizacja statusu dostępności towarów
* Obsługa dat - automatyczne wyliczanie terminu zwrotu przy użyciu biblioteki `datetime`
* Generator ID - program samodzielnie nadaje unikalne 4-cyfrowe identyfikatory

# Bezawaryjność

Program został napisany tak, aby był odporny na pomyłki użytkownika:
* Walidacja danych - funkcja `num()` zapobiega przerwaniu pracy programu w razie wpisania
  litery zamiast liczby
* Integralność bazy - program sprawdza czy użytkownik oraz towar istnieje przed wypożyczeniem
* Logika dostępności - system nie pozwala na wypożyczenie towaru który jest niedostępny
* Weryfikacja zwrotu - program sprawdza czy to właśnie ten użytkownik wypożyczył dany towar

# Jak uruchomić

1. Upewnij się że masz zainstalowanego Pythona
2. Pobierz plik ze skryptem (`main.py`)
3. Uruchom program w terminalu:
```bash
python main.py
```