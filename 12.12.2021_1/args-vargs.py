def sum(title, *args, ending):
    result = 0
    for value in args:
        result += value
    return title + str(result) + " - "+ ending


print(sum("suma 1: ", 1, 2, 3, 4, 5, 6, ending="inny tytul"))
print(sum("suma 2: ", 1, 2, 3, 4, 5, 6, 5, 6, 7, 2, 3, 5, 6, ending="inny tytul"))


###########################################3
def fun2(a, b, c, *, d, e, **kwargs): # kwargs - multiple NAMED args
    print(a, b, c, d, e, kwargs)


fun2(1, 2, 3, d=4, e=5, imie="Marcin", nazwisko="Krawczyk")