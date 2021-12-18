from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]

reduced = reduce(operator.mul, numbers)
print(reduced)
