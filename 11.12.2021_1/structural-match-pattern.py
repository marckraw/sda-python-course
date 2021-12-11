import sys
print("Wersja Pythona", sys.version)

number = int(input("Podaj liczbe: "))

match number:
    case 42:
        print("Ta liczba to moja ulubiona liczba")
    case 17:
        print("To liczba zwiazana z data urodzenia")
    case 8:
        print("Ta liczba kojarzy mi sie z pieniedzmi")
    case _:
        print("Ta liczba nie ma dla mnie znaczenia")