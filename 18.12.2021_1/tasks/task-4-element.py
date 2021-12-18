
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'{self.name=}: {self.symbol=}{self.number=}'


elem = {
    'name': 'wodór',
    'symbol': 'H',
    'number': '1'
}


# hydrogen = Element(elem['name'], elem['symbol'], elem['number'])
hydrogen = Element(**elem) # krocej
wodor = Element('srebro', 'ag', 7)
print(wodor)
print(hydrogen)