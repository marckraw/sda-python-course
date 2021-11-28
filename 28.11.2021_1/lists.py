## Lists

imiona = ['Bartek', 'Ola', 5, True, None, [1, 2, 3, 4]]
print(imiona)

imiona[1] = 'Ferdynand'
print(imiona)

imiona.append(10) # very performant operation, the most performant one
print(imiona)

imiona = imiona + ['Ada', 'Ela', 'Maria']
print(imiona)

imiona.insert(5, 42) # not performant at all
print(imiona)

imiona.remove(10) # removes by element not by index - dosyc mocne, niezle
print(imiona)

imiona.pop(5)
print(imiona)



imiona_do_posortowania = ['bartek', 'ola', 'ela', 'Ola']
imiona_do_posortowania.sort()
print(imiona_do_posortowania)
print(ord('B')) # jaka liczba przyporzadkowana w asci do B

imiona_do_posortowania.sort(key=len)
print(imiona_do_posortowania)

imiona_do_posortowania.sort(key=len, reverse=True)
print(imiona_do_posortowania)



test = ['Bartek', 'Marcin', 'Ola']
print(test)

test[0], test[2] = test[2], test[0]
print(test)

print(test.index('Bartek'))


test2 = test # przypisywanie by reference
test[0] = 'Ada'
print(test2)

# kopiowanie listy

druga_lista = test[:] # kopiowanie
druga_lista2 = test.copy() # kopiowanie przez copy, moze lepsze ? (czytelniejsze) - shallow copy not deep


import copy
deep_copy = copy.deepcopy(druga_lista) # deep copy
