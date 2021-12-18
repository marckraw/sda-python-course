with open('file_to_open.txt', 'r', encoding='utf-8') as f, open('file_to_write.txt', 'w', encoding='utf-8') as g:
    whole_file = f.readlines()
    for idx, line in enumerate(whole_file, 1):
        transformed_line = f"{idx:03}: {line.upper()}"
        g.write(transformed_line)