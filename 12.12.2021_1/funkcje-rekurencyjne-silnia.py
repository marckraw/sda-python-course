# Funkcje rekurencyjne - funkcja wywolujaca sama siebie

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

for liczba in range(10):
    print(f"silnia {liczba}: {silnia(liczba)}")
