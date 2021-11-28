list_1 = [1, 'ala', True, None, [1, 2, 3, 4]]

types_list = [ type(x) for x in list_1 ]
print(types_list)


################################

# return indexes of the special value
list_2 = [1, 'a', 'b', 'a', 2, 3, 'a']
index_of_a = [x for x in range(len(list_2))
                if list_2[x] == 'a'
              ]

print(index_of_a)