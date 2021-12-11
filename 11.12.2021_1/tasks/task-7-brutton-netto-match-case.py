def calculateBrutto(netto):
    return 10 / 8 * netto

def calculateNetto(brutto):
    return 8 / 10 * brutto

while True:
    print("----- MENU -----")
    print('1) Brutto -> Netto')
    print('2) Netto -> Brutto')
    print('3) Koniec')

    choice = int(input("Opcja: "))
    print("Wybrano opcje", choice)
    match choice:
        case 3:
            print("papa ")
            break
        case 2:
            money = float(input("Podaj kwote Netto: "))
            brutto = calculateBrutto(money)
            print(f"Wynik {brutto}")
        case 1:
            money = float(input("Podaj kwote Brutto: "))
            netto = calculateNetto(money)
            print(f"Wynik {netto}")
        case _:
            print("Nie rozumiem opcji.")

    print("Wcisnij enter...")
    input()
