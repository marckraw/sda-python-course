import math
import sys

number_to_count = 5

# arguments_list = ['name', 1, 2, 5, 5, 3, 1, 5, 4, 5]
arguments_list = sys.argv

numbers_list = sorted(arguments_list[1:])


counted_number = numbers_list.count('5')

print(f"Sorted list with 5: {numbers_list}")

list_without_five = [x for x in numbers_list if int(x) != number_to_count]


# counted_number = len(numbers_list) - len(list_without_five)

print(f"Number {number_to_count} occurs {counted_number} times.")
print(f"Sorted list without 5: {list_without_five}")

