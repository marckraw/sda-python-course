word = input("Podaj slowo: ")

word_letters = list(word)

print(word_letters)

i = 0
while i < len(word_letters):
    print(f"Literka {word_letters[i]} ma indesk {ord(word_letters[i])}")
    i += 1
