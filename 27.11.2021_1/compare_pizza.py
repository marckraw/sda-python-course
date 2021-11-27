import math
pizza1_srednica = 42
pizza1_cena = 36

pizza2_srednica = 56
pizza2_cena = 42.5

p1 = (pizza1_srednica / 2) ** 2 * math.pi  # pole 1
p2 = (pizza2_srednica / 2) ** 2 * math.pi    # pole 2

s1 = p1 / pizza1_cena  # stosunek 1
s2 = p2 / pizza2_cena    # stosunek 2

print(f'Stosunek pierwszej pizzy wynosi: {s1:.2f}.\nStosunek drugiej pizzy: {s2:.2f}')