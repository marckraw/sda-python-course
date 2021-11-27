import datetime
# import getpass

# name = getpass.getpass('Podaj imie: ')
name = input('Podaj swoje imie: ')
born_in = input('Podaj rok twojego urodzenia: ')

current_year = datetime.date.today().year
age = current_year - int(born_in)

print(f'Nazywam sie {name} i mam {age} lat')