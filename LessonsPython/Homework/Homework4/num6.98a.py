# 6.98. Гражданин 1 марта открыл счет в банке, вложив 1000 руб. Через каждый месяц размер вклада увеличивается на 2% от имеющейся суммы. Определить:
# а) за какой месяц величина ежемесячного увеличения вклада превысит 30 руб.;

sum = 1000
month_num = 1
deposit = 0

while deposit < 30:
    deposit = (sum * 2) // 100
    if deposit > 30:
        break
    sum = sum + (sum * 2) // 100
    month_num = month_num + 1

print(sum)
print(deposit)
print(month_num)