number = int(input("Wprowadz liczbe: "))


while number != 1:
    if number % 2 == 0:
        number //= 2
    else:
        number = number * 3 + 1

    print(number)
