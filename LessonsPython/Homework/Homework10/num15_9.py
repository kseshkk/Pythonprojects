file = open("file.txt", encoding="utf-8")
count_symbols = 0

for string in file:
    for symbols in string:
        count_symbols += 1

print(f"кол-во символов: {count_symbols}")