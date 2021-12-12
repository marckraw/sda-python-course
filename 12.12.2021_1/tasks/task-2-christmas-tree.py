
def draw_triangle(height):
    amount_of_stars = 1
    amount_of_spaces = height + 1
    for i in range(height):
        print(' ' * amount_of_spaces, '*' * amount_of_stars)
        amount_of_stars += 2
        amount_of_spaces = height - i


draw_triangle(5)

print()
print()

draw_triangle(10)

print()
print()

draw_triangle(20)