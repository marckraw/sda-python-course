import string

imie = 'Bartek'


imie.find('r') # 2 position
imie.find('z') # -1

imie.rfind('e') # search from right side
# imie.lfind('e') # search from left side

imie.istitle() # checks if everything is starting with upper letter
imie.isupper() # checks if everything is upper case
imie.swapcase() # changes lower case to uppercase and uppercase to lowercase



title = '123123asd                                        '
title.strip() # remove spaces from both sides, butj can also remove other chars from end and start that we pass

'abracadabra'.replace('a', 'x')



imie = 'Maria'
imie[0]
imie[-1] # last item of string


imie[0:3] # something like slice in javascript
imie[:3] # if i know it will be from 0 to < 3
imie[0:6:2] # bierzemy od 0 do <6 ale co 2 litery
imie[::2] # od poczatku do konca co 2

imie[::-1] # odwraca napis

len('Bartek') # very performant function for getting length of sequence


###
text = "!.#Mam na imie Marcin, mam [31] lat. Chodze do szkoly."
print(text.strip(string.punctuation))

## String conversion
x = 5
repr(x) # '5'
str(x) # '5'
