# 28.11.2021 - Sunday - #2
- Typy bool
- Konwersja typów
- Lists
- Dicts
- Tuples
- Comprehensive Lists / Dicts

## Przydatne linki
- http://pythontutor.com/

## Przydatne z z tego dnia
- String nie sa modyfikowalne w pythonie !! (wszystkie funkcje na stringach zwracaja nowy string)
- Python opiuje listy podobnie jak w JS - jest to shallow copy, zeby skopiowac liste deep, trzbea uzyc dodatkowego modulu "copy"
- Comprehensive list - uzywac, bardzo wydajne, python way

```python
any(['s', '', 'p']) # True
all(['s', '', 'p']) # False
```

```python
a = 42 
b = 42

a == b # True
a is b # True

but
>>> lista_imion = ['Bartek', 'Ola']
>>> druga = ['Bartek', 'Ola']

lista_imion is druga # False

import sys
sys.getrefcount(a) # amount of references to this object
id(a) # id of the address of thie variable

```

## Przydatne moduly
```python
import this
import math
import sys
import random
import string
import copy
```
