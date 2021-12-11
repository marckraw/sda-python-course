MAGIC_NUMBER = 9


amount_of_tries = 10
while amount_of_tries > 0:
    number = int(input("Podaj liczbe: "))

    if number > 1000 or number < 0:
        print("Podaj liczbe z zakresu (0, 1000)")
        continue

    if number == MAGIC_NUMBER:
        print("Zgadles!")
        break
    elif number > MAGIC_NUMBER:
        print("Proboj dalej, Powinienes podac liczbe mniejsza :)")
    elif number < MAGIC_NUMBER:
        print("Proboj dalej, Powinienes podac liczbe wieksza :)")

    amount_of_tries -= 1

else:
    print()
    print("############################")
    print("Niestety nie zgadles liczby.")
    print("############################")


