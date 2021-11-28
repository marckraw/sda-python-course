import math
import sys


arguments_list = sys.argv

a = float(arguments_list[1])
b = float(arguments_list[2])
c = float(arguments_list[3])

p = (a + b + c) / 2
result = math.sqrt(p * (p - a) * (p - b) * (p - c))

print(result)
