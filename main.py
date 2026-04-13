from datetime import datetime, timedelta


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


# Pobieranie w INT
def num(value):
    while True:
        try:
            number = int(input(value))
            if number < 0:
                print("!!! Ta wartość jest ujemna !!!")
            else:
                return number
        except ValueError:
            print("!!! Niepoprawny typ danych podaj liczbe !!!")


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


# Wyświetlanie dostępnego towaru
def aval_items():
    with open("items.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            item_id, title, item_type, availability = line.split(",")
            if int(availability) == 1:
                print(f"Tytuł: {title:<15} Typ: {item_type:<10}")


# Wypożyczanie towaru
def rent():
    while True:
        user_id = str(num("Podaj ID użytkownika: ")).strip().zfill(4)
        found = False
        with open("users.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if user_id == parts[0]:
                    found = True
                    break
        if found:
            break
        else:
            print("Taki użytkownik nie istnieje")
    while True:
        item_id = str(num("Podaj ID towaru: ")).strip().zfill(4)
        found = False
        exist = False
        with open("items.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if parts[0] == item_id:
                    if parts[3] == "1":
                        found = True
                    else:
                        exist = True
        if found:
            break
        elif exist:
            print("Ten film jest niedostepny")
        else:
            print("Nie ma takiego towaru")
    time = num("Na ile dni wypożyczasz?: ")
    time_now = datetime.now().strftime("%Y-%m-%d")
    time_end = (datetime.now() + timedelta(days=time)).strftime("%Y-%m-%d")
    new_rent = f"{user_id},{item_id},{time_now},{time_end}\n"
    with open("rentals.txt", "a") as file:
        file.write(new_rent)
    all_lines = []
    with open("items.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if parts[0] == item_id:
                parts[3] = "0"
            all_lines.append(",".join(parts) + "\n")
    with open("items.txt", "w") as file:
        file.writelines(all_lines)
    print(f"Wypożyczono do: {time_end}")


# Zwrot towaru
def check_in():
    while True:
        user_id = str(num("Podaj ID użytkownika: ")).zfill(4)
        item_id = str(num("Podaj ID towaru: ")).zfill(4)
        rented = False
        with open("rentals.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if parts[0] == user_id and parts[1] == item_id:
                    rented = True
                    break
        if rented:
            break
        else:
            print("Użytkownik nie wypożyczył wybranego towaru")
    all_lines = []
    with open("rentals.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if parts[0] == user_id and parts[1] == item_id:
                continue
            all_lines.append(line + "\n")
    with open("rentals.txt", "w") as file:
        file.writelines(all_lines)
    all_lines = []
    with open("items.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if parts[0] == item_id:
                parts[3] = "1"
            all_lines.append(",".join(parts) + "\n")
    with open("items.txt", "w") as file:
        file.writelines(all_lines)


# Wyświetlanie aktywnych wypożyczeń
def active():
    with open("rentals.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            rentals = line.split(",")
            with open("items.txt", "r") as file2:
                for line2 in file2:
                    line2 = line2.strip()
                    if not line2:
                        continue
                    items = line2.split(",")
                    with open("users.txt", "r") as file3:
                        for line3 in file3:
                            line3 = line3.strip()
                            if not line3:
                                continue
                            users = line3.split(",")
                            if users[0] == rentals[0] and items[0] == rentals[1]:
                                print(
                                    f"Wypożyczający: {users[1]} {users[2]} | Towar: {items[1]} | Data zwrotu: {rentals[3]}"
                                )


# Struktura
start()
while True:
    print()
    print(
        " MENU UŻYTKOWNIKA",
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
    decision = num("Wybierz akcje: ")
    print()

    if decision == 1:
        user_add()
    elif decision == 2:
        user_list()
    elif decision == 3:
        item_add()
    elif decision == 4:
        aval_items()
    elif decision == 5:
        rent()
    elif decision == 6:
        check_in()
    elif decision == 7:
        active()
    elif decision == 8:
        break
    else:
        print()
