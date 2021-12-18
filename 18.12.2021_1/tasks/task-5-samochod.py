
class Kierownica():
    def does(self):
        return 'skreca'

    def __str__(self):
        return 'kierownica'

class Hamulec():
    def does(self):
        return 'hamuje'

    def __str__(self):
        return 'hamulec'

class Alternator():
    def does(self):
        return 'laduje akumulator'

    def __str__(self):
        return 'alternator'


class Samochod():
    def __init__(self):
        self.kierownica = Kierownica()
        self.hamulec = Hamulec()
        self.alternator = Alternator()

    def does(self):
        return f'''
Elementy ktore mam to: 
{self.kierownica}, która {self.kierownica.does()}
{self.hamulec}, która {self.hamulec.does()}
{self.alternator}, która {self.alternator.does()}
        '''

auto = Samochod()

print(auto.does())
