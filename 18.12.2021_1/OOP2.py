
class Cat:
    color = 'black'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'My name is {self.name}. I am {self.age} years old.'


cats = [Cat('Blanunia', 7), Cat('Maks', 5)]

cats[1].color = 'white' # instance of a Cat class
# Cat.color = 'white' # Cat class

for cat in cats:
    print(cat, f'Kolor: {cat.color}')