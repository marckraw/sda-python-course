
def draw_triangle(height):
    amount_of_stars = 1
    width = 2 * height
    for i in range(height):
        print(f"{'*' * amount_of_stars}".center(width, " "))
        amount_of_stars += 2


draw_triangle(5)

print()
print()

draw_triangle(10)

print()
print()

draw_triangle(20)