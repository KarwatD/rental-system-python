# Equipment Rental System (Games/Movies)

A simple but robust application for rental shop employees to manage users and inventory. It supports viewing, adding, renting, and returning items with automated status tracking.

# Features

* Managing users and products - adding and displaying from file
* Rents and returns system - automatical updating of product avaliability status
* Date Handling - automated return date calculation using the datetime library.
* ID Generator - the system automatically generates unique 4-digit identifiers for new entries.

# Reliability

Aplication takes focus on system robustness for users bads
* Data Validation - the num() function prevents system crashes if a user enters a letter instead of a number.
* Data Integrity - the system performs real-time validation to ensure both the user and the item exist in the database before processing any rental
* Avaliability logic - system forbid to rent product that's not available
* Check-in Verification - the application verifies the user identity during returns to ensure data consistency.

# How to use

1. Make sure you have installed Python
2. Download script file `main.py`
3. Launch application in terminal:
```bash
python main.py
```


        -------------------------------------------------------------------------------------------------------------------

# System dla wypożyczalni gier/filmów (CRUD)

Prosty program dla pracowników wypożyczalni pozwalający na zarządzanie użytkownikami oraz towarem: wyświetlanie, dodawanie, wypożyczanie oraz zwracanie

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
2. Pobierz plik ze skryptem `main.py`
3. Uruchom program w terminalu:
```bash
python main.py
```
