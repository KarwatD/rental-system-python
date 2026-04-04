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


start()
