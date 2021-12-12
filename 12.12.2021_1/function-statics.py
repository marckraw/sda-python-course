
def fun():
    print("Zwyklty napis")
    fun.call_amounts += 1


fun.call_amounts = 0

fun()
fun()
fun()

print(fun.call_amounts)

#################################################


def print_only_once(value):
    if print_only_once.printed: return
    else:
        print_only_once.printed = True
        print(value)

print_only_once.printed = False
print_only_once("Hello World")
print_only_once("Hello World")
print_only_once("Hello World")