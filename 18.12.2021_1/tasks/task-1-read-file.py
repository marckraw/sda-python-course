f = open('../example_file.txt', encoding='utf-8')
print(f.read())
print("Czy zamkniety ?", f.closed)
f.close()



# With this, we don't need to care about closing file. Context Manager doesnt add special scope!
with open('../example_file.txt', encoding='utf-8') as f:
    print(f.read())
print("Czy zamkniety ?", f.closed)
# print("############")
# print(f.read()) # this will not work, becasue file is not opened





