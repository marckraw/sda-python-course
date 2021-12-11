# for

for i in range(10): # petla for zajebiscie rozumie "generatory" wiec nie trzeba ich konwertowac na liste zeby iterowac
    print(i)

########################################################################################################################
print()

names = ['Bartek', 'Maria', 'Ola']

for idx, name in enumerate(names, 1):
    print(f'{idx}: {name}')

########################################################################################################################
print()

numbers = [1, 45, 23, 6, 23, 2, 1, 13]

max_number = numbers[0]
min_number = numbers[0]
for number in numbers:
    max_number = number if number > max_number else max_number
    min_number = number if number < min_number else min_number

print(f'Minimalna wartosc z tablicy: {min_number}')
print(f'Maksymalna wartosc z tablicy: {max_number}')


########################################################################################################################\

# numbers = [1, 45, 23, 6, 23, 2, 1, 13, 8]
# dla kazdej liczby, sprawdzasz liczbe sasiednia

