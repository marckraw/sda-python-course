import sys

print('Program działa')
print('Wersja interpretera:', sys.version)


print("Książka \"Mały Książe\" została napisana przez Antione de Saint Excupery")
print('Książka \"Mały Książe\" została napisana przez Antione de Saint Excupery')
print("Książka 'Mały Książe' została napisana przez Antione de {Saint Excupery}")


imie = 'Bartek'
wiek = 32
waga = 96.5

# Finalne zdanie: "Mam na imię Bartek. Mam 32 lata i ważę 96.5 kg"
print('Mam na imię ', imie, '. Mam ', wiek, ' lata i ważę ', waga,' kg.', sep='')


# PIERWSZA METODA PRINTOWANIA
print('Mam na imię %s. Mam %d lata i ważę %10.2f kg.' % (imie, wiek, waga)) # 10 miejsc na wagę, w tym 2 miejsca po przecinku
print('Mam na imię %s. Mam %d lata i ważę %.2f kg.' % (imie, wiek, waga)) # waga z dokładnością do 2 miejsc po przecinku

print('%-20s %f' % (imie, waga)) # wyrównanie do lewej strony, szrokość imienia ustawiona na 20
print('%20s %f' % (imie, waga))  # bez minusa, wyrównanie domyślnie do prawej strony

'''
ćwiczenie
'''
towar1 = 'Kapusta'
towar2 = 'Mango'
towar3 = 'Banany'
cena1 = 12.6
cena2 = 3.4
cena3 = 42
#Kapusta               12.6
#Mango                  3.4
#Banany                  42
print('%s %15.1f' %(towar1.ljust(20, '.'), cena1))
print('%s %15.1f' %(towar2.ljust(20, '.'), cena2))
print('%s %15d' %(towar3.ljust(20, '.'), cena3))
print()

help_text = '''Ten program %s w wersji %d uruchamia się następująco:
> python pisanie.py

Ten program służy tylko programiście do nauki pisania/
To był wielolinijkowy tekst'''

print(help_text % ('PISANIE', 12))

# DRUGA METODA PRINTOWANIA
print('FUNKCJA FORMAT: Mam na imię {}. Mam {} lata i ważę {} kg.'.format(imie, wiek, waga))
print('FUNKCJA FORMAT: Mam na imię {0}. Mam {1} lata i ważę {2:.2f} kg.'.format(imie, wiek, waga))

# TRZECIA METODA PRINTOWANIA
print(f'FSTRING: Mam na imię {imie}. Mam {wiek} lata i ważę {waga:.3f} kg. Wpisanie klamerki {{ <- podwójny znak')
print(f'|{imie:_<20}|')
print(f'|{imie:->20}|')
print(f'|{imie:.^20}|')
#Kapusta...............12.6
#Mango..................3.4
#Banany..................42

# Szybkie sprawdzenie wartości zmiennych
print(f'imie={imie} wiek={wiek} waga={waga}')

print(f'{imie=} {wiek=} {waga=}') # nowy sposób