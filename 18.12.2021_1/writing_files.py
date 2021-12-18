# f = open('example_file.txt', 'r', encoding='utf-8') # open for READ
f = open('write_file.txt', 'w', encoding='utf-8') # open for WRITE

for i in range(1, 31):
    f.write(f"Line number: {i}\n")

f.close()