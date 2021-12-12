
def fun(a, b, c=None):
    print(f"{a=}, {b=}, {c=}")


fun(1, 2, 3)
fun(a=1, b=2, c=3)
fun(a=1, c=3, b=2)

fun(1, b=2)