class Cat:
    __kind_of_private_variable = 2312 # with __ in front

    def __init__(self, name, age):
        print(f'Tworzenie kota {name}')
        self.name = name
        self.zamialczal = False
        self.age = age

    def meow(self):
        self.zamialczal = True
        print('Miau, miau, miau')

    def __str__(self):
        return f'Kot o imieniu {self.name}, wiek {self.age}'


class Pers(Cat):
    def __init__(self, name, age, hair_length):
        super().__init__(name, age)
        self.hair_length = hair_length

    def __str__(self):
        return f'Kot o imieniu {self.name}, wiek {self.age}. dlugosc siersci {self.hair_length}'


blanunia = Cat('Blanunia', 7)
maks = Cat('Maksio', 5)
feniks = Cat('Fenio', 3)
filemon = Pers('Filemon', 8, 8.5)

print()

print(blanunia)
print(maks)
print(feniks)
print(filemon)

