# Compregensive list - wyrazenia listowe


print(
    list(range(10))
)


list_1 = [ x for x in range(30) ]
print(list_1)

list_2 = [ x**2 for x in range(30) ]
print(list_2)

list_3 = [ x*4 for x in range(30) if x % 3 == 0 ] # performant stuff, because its implemented in C underneath
print(list_3)



