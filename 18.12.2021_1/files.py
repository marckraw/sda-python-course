import os
from textwrap import wrap

f = open('example_file.txt', encoding='utf-8')

print('### Oto mój plik ###')
print('Pozycja: ', f.tell()) # w jakim miejscu pliku jestem obecnie ? ilosc bytow - jesli sa polskie znaki to to 1 litera z znakami polskimi = 2

# print(f.readline()) # read first line
# print('Pozycja: ', f.tell()) # w jakim miejscu pliku jestem obecnie ?

# print('Reszta pliku')
# f.seek(0, os.SEEK_SET)
# print(f.read()) # read entire file content

# print(f.readlines()) # read all lines and put in a list

# print(f.readlines()[2:]) # Read starting from third line

# for line in f:
#     print(line, end='')

# for line in f.readlines()[:2]:
#     print(line, end='')



f2 = open('example_file_in_one_line.txt', encoding='utf-8')
full_file = f2.read()
position = 0
while position + 20 < len(full_file):
    line = full_file[position:position + 20]
    position += 20
    print(line)





print('Pozycja: ', f.tell()) # w jakim miejscu pliku jestem obecnie ?
f.close()