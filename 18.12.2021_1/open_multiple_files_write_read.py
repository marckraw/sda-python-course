with open('write_file.txt', 'w', encoding='utf-8') as f, open('write_file_2.txt', 'w', encoding='utf-8') as g:
    for i in range(1, 31):
        f.write(f"Line number: {i}\n")
        g.write(f"Line in another file, number: {i}\n")




# open('write_file.txt', 'a', encoding='utf-8') # appening to the end of file, doesnt overwrite previous content
# open('write_file.txt', 'r+', encoding='utf-8') # read + write - if file not exsits, it will raise error
# open('write_file.txt', 'w+', encoding='utf-8') # write + read  - if file not exist, it will create file
# open('write_file.txt', 'x', encoding='utf-8') # write if file not exist, it will create file