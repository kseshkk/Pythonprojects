file = open("file.txt", encoding="utf-8")
file.seek(0)
file.read(4)
print(file.read(1))