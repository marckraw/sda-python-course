# create a tuple of 5 numbers in random order and sort it

import random

this_it_list = [random.randint(0, 100) for x in range(5)]
this_is_tuple = tuple(sorted(this_it_list))

print(this_is_tuple)