# б) через сколько месяцев размер вклада превысит 1200 руб.

sum = 1000
month_num = 1
deposit = 0

while sum < 1200:
    deposit = (sum * 2) // 100
    sum = sum + (sum * 2) // 100
    month_num = month_num + 1

# print(sum)
# print(month_num)

print(f"размер вклада превысит 1200 руб через {month_num} месяцев")