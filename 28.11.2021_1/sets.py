## Sets - wyszukiwanie w zbiorach jest zajebiste


# Set / frozenset
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b = {20, 30, 40, 50, 60, 70, 80, 90}


print(
    1 in a,
    11 not in a,
    a & b,
    a | b,
    a < b,
    a.issubset(b),
)



empty_list = list()
empty_tuple = tuple()
empty_set = set()


{7, 8}.add(9)