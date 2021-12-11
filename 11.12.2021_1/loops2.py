word = input("Podaj slowo: ")

i = 0

while i < len(word):
    print(f"Sprawdzam litere {word[i]}")
    if 'p' == word[i]:
        break
    i += 1
else: # wykonuje sie jak jak wykona sie petla i nie natrafimy w niej na instrukcje break, continue
    print("Nie znalazlem literki 'p' w slowie")
