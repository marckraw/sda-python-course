imie = input("Wpisz imie: ")

black_list = ['Kacper', 'Mufasa', 'Asmodeusz']

if imie in black_list:
    print("Tych klientow nie obslugujemy")
elif imie.lower() == "Bartek":
    print("Mam na imie tak samo jak ja")
    print("Druga linia")
elif imie.startswith("B"):
    print("Nasze imiona zaczynaja sie na te sama litere")
    print("Ciesze sie")
elif imie.endswith("a"):
    if imie != "Barnaba":
        print("Prawdopodobnie jestes kobieta")
    else:
        print("Jestes mezczyzna")
else:
    if len(imie) < 2:
        print("cos dziwnego")
    else:
        print("Niestety nie mam infromacji dla Ciebie")

print("Koniec programu")