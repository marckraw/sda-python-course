# Popros uzytkownika o dwa slowa oddzielone przecinkiem i sprawdz czy z liter jednego z nich mozna ulozyc drugie slowo - wyprintuj True, albo False.
# litery traktujemy pojedynczo - anagram

word_1, word_2 = input("Podaj slowo oddzielone przecinkiem: ").split(",")

word_1_set = set(word_1.strip())
word_2_set = set(word_2.strip())

print(
    word_1_set.issuperset(word_2_set) or word_2_set.issuperset(word_1_set)
)






















