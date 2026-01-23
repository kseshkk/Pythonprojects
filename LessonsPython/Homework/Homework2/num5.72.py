distance = 10

sum = distance

for i in range(2, 10 + 1):
    distance = distance + distance * 0.1
    print(f"день номер {i} дистанция = {distance:.1f} км")

    if i <= 7:
        sum = sum + distance

print(f"за 7 дней суммарная дистанция = {sum:.1f} км")