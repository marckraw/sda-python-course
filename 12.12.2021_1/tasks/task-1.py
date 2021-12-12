
def print_pretty(caption):
    print(f"+{'-' * len(caption)}+")
    print(f"|{caption}|")
    print(f"+{'-' * len(caption)}+")


text = input("Podaj text: [......]\b\b\b\b\b\b\b")
print_pretty(text)