
class Cat:
    def __init__(self, name):
        print(f'Tworzenie kota {name}')
        self.name = name
        self.zamialczal = False

    def meow(self):
        self.zamialczal = True
        print('Miau, miau, miau')

    def __str__(self):
        return f'Kot o imieniu {self.name}'


blanunia = Cat('Blanunia')
maks = Cat('Maksio')
feniks = Cat('Fenio')


blanunia.meow()
print(maks.zamialczal)
print(blanunia.zamialczal)

print()

print(f'Imiona kotów: {blanunia.name}, {maks.name}, {feniks.name}')

print()

print(blanunia)
print(maks)
print(feniks)