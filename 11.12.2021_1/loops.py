licznik = 0

# while licznik < 10:
#     print(f"Licznik tyka {licznik}...")
#     licznik += 1



while True:
    licznik += 1
    print(f"{licznik=}")
    if licznik % 20 == 0:
        opcja = input("Czy chcesz wyjsc z petli ? (Y/N)").lower()
        if(opcja == "y"):
            break