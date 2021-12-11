import string
# Scrabble lite

text = input("Podaj slowo: ")


i = 1

letters_dict = { val: idx for idx, val in enumerate(string.ascii_letters, 1) }

print(letters_dict)

text_list = list(text)

result = 0
for x in text_list:
    result = result + letters_dict[x]

print("Your result: ", result)

