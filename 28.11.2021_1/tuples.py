## Tuples

'''
Same stuff like in lists, you can use [0:3] stuff, but can't reassign
'''


name_tuples = ('Bartek', 'Ola', 'Ela')
print(
    name_tuples[0]
)


zgrywus_tuples = (1, 2, 3, True, ['a', 'b', 'c'])

## conversion from list to tuple
names = ["Filon", "ola", "ela"]
names_list_tuples_conversion = tuple(names)
print(names_list_tuples_conversion)
print(list(names_list_tuples_conversion))



## Desctrukturyzacja krotek

krotka = (1, 2, 3, 4)
a, b, c, d = krotka


a, b, *rest = krotka
print(a, b, rest)

a, *rest, b = krotka
print(a, rest, b)








