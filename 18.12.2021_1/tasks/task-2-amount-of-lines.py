f = open('../example_file.txt', encoding='utf-8')

whole_file = f.readlines()

amount_of_lines = len(whole_file)

amount_of_chars = 0
for line  in whole_file:
    amount_of_chars += len(line)

print("Amount of lines in a file: ", amount_of_lines)
print("Amount of chars in a file: ", amount_of_chars)

f.close()





