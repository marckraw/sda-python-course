def calculateBrutto(netto):
    return 10 / 8 * netto

def calculateNetto(brutto):
    return 80 / 100 * brutto

while True:
    print("----- MENU -----")
    print('1) Brutto -> Netto')
    print('2) Netto -> Brutto')
    print('3) Koniec')

    choice = int(input("Opcja: "))
    print("Wybrano opcje", choice)
    if choice == 3:
        print("papa ")
        break
    elif choice == 2:
        money = float(input("Podaj kwote Netto: "))
        brutto = calculateBrutto(money)
        print(f"Wynik {brutto}")
    elif choice == 1:
        money = float(input("Podaj kwote Brutto: "))
        netto = calculateNetto(money)
        print(f"Wynik {netto}")

    print("Wcisnij enter...")
    input()
