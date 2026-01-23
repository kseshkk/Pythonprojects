# Напечатать таблицу умножения на 7

a = 1
b = 1
while a < 8:
    while b < 8:
        print(a * b, end="\t")
        b += 1
    print("\n")
    b = 1
    a += 1