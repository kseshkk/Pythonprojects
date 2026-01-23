file = open("file.txt", encoding="utf-8")
count_str = 0

for strings in file:
    count_str += 1

print(count_str)