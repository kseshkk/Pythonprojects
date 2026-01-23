file = open("file.txt", encoding="utf-8")
count_symbols = 0
count_str = 0

for string in file:
    count_str += 1
    count_symbols = len(string)
    print(f"в строке: {count_str} кол-во символов: {count_symbols}")