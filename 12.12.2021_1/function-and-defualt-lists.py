
def fun(animal_list=[]):
    animal_list.append("Monkey")
    print(animal_list)


fun()
fun()
fun()





#########################################
# protection against
def fun2(animal_list=None):
    if animal_list is None:
        animal_list = []
    animal_list.append("Monkey")
    print(animal_list)


fun2()
fun2()
fun2()

#####################################3

a = [5, 2, 3]


def fun3(x):
    """
    Ta funkcja jest zajebista
    :param x:
    :return: ta funkcja niczego nie zwraca
    """
    x *= 2


fun3(a[:])
fun3(a[:])

help(fun3)

print(a)