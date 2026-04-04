# Tworzenie / Sprawdzenie plików
def start():
    try:
        with open("users.txt", "r") as file:
            print()
    except FileNotFoundError:
        with open("users.txt", "w") as file:
            file.write("")
    try:
        with open("items.txt", "r") as file:
            print()
    except FileNotFoundError:
        with open("items.txt", "w") as file:
            file.write("")
    try:
        with open("rentals.txt", "r") as file:
            print()
    except FileNotFoundError:
        with open("rentals.txt", "w") as file:
            file.write("")


# Generator ID
def id_gen(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            if not lines:
                return "0001"
            last_line = lines[-1].strip()
            parts = last_line.split(",")
            last_id = int(parts[0])
            new_id = last_id + 1
            return str(new_id).zfill(4)
    except FileNotFoundError:
        return "0001"


# Dodawanie użytkownika
def user_add():
    user_id = id_gen("users.txt")
    name = input("Podaj imie: ").lower()
    surname = input("Podaj nazwisko: ").lower()
    new_user = f"{user_id},{name},{surname}\n"
    with open("users.txt", "a") as file:
        file.write(new_user)


# Wyświetlanie użytkowników
def user_list():
    with open("users.txt", "r") as file:
        print()
        for line in file:
            line = line.strip()
            if not line:
                continue
            user_id, name, surname = line.split(",")
            print(f"ID: {user_id:<8} Imie: {name:<12} Nazwisko: {surname:<12}")


# Dodawanie towaru
def item_add():
    item_id = id_gen("items.txt")
    title = input("Podaj tytuł: ").lower()
    while True:
        item_type = input("Typ towaru (FILM/GRA): ").lower()
        if item_type == "gra" or item_type == "film":
            break
        else:
            print("Podaj prawidłową wartość")
    while True:
        availability = input("Czy jest dostepny? (TAK/NIE): ").strip().lower()
        if availability == "tak":
            availability = 1
            break
        elif availability == "nie":
            availability = 0
            break
        else:
            print("Podaj poprawną opcje")
    new_item = f"{item_id},{title},{item_type},{availability}\n"
    with open("items.txt", "a") as file:
        file.write(new_item)


# Struktura

start()
while True:
    print()
    print(
        "1.Dodaj użytkownika",
        "2.Wyświetl wszystkich użytkowników",
        "3.Dodaj przedmiot",
        "4.Wyświetl dostepny towar",
        "5.Wypożyczanie towarów",
        "6.Zwrot towarów",
        "7.Wyświetl aktywne wypożyczenia",
        "8.Wyjdź",
        sep="\n",
    )
    decision = int(input("Wybierz akcje: "))

    if decision == 1:
        user_add()
    elif decision == 2:
        user_list()
    elif decision == 3:
        item_add()
    elif decision == 4:
        print()
    elif decision == 5:
        print()
    elif decision == 6:
        print()
    elif decision == 7:
        print()
    elif decision == 8:
        break
    else:
        print()
