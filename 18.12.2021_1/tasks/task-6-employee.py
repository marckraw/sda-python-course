class Employee:
    raise_amount = 1.12

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = f'{self.firstname}.{self.lastname}@codepride.pl'

    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    def __str__(self):
        return f'{self.fullname()}'



maria = Employee('Maria', 'Db', 9200)
ela = Employee('Ela', 'Słodowa', 8700)


print(f'Maria zarabia {maria.salary}')
print(f'Ela zarabia {ela.salary}')

print()
print('Nastaly podwyzki')
print()

maria.raise_amount = 1.3

maria.apply_raise()
ela.apply_raise()

print(f'Maria zarabia {maria.salary}')
print(f'Ela zarabia {ela.salary}')