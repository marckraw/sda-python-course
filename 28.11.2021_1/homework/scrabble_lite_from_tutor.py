import string
# Scrabble lite from tutor

letters = string.ascii_lowercase + "ąężćśłóń"
points = list(range(1, len(letters) + 1))

# scores = {k: v for k in letters for v in points}
# tuple_scores = [(k, v) for k in letters for v in points]
scores_with_zip = {k: v for k, v in zip(letters, points)}

# print(scores)
# print(tuple_scores)
print(scores_with_zip)

word = input("Podaj słowo: ").lower()
word_filtered = [letter for letter in word if letter in letters]

result = sum(scores_with_zip[letter] for letter in word_filtered)
print(result)



