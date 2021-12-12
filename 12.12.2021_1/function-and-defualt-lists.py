
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