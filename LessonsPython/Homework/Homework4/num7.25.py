# 7.25. Известны оценки по информатике каждого ученика класса. Определить количество пятерок.

# list = []
# list.extend(a)
# print(list.count(5))
# a = int(input("ввести оценки: "))

count_five = 0
marks = int(input("ввести количество оценок: "))

for _ in range(marks):
    current_mark = int(input("ввести оценку: "))
    if current_mark == 5:
        count_five = count_five + 1

print(f"всего пятерок: {count_five}")