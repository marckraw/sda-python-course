
def fun(a, b, c=None):
    print(f"{a=}, {b=}, {c=}")


fun(1, 2, 3)
fun(a=1, b=2, c=3)
fun(a=1, c=3, b=2)

fun(1, b=2)



###########################################3
def fun2(a, b, c, *, d, e): # w taki sposob mozemy zmusic uzytkownika zeby d i e przekazal jako named
    print(a, b, c, d, e)


fun2(1, 2, 3, d=4, e=5)