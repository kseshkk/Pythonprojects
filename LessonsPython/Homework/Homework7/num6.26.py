# 6.26. Дано натуральное число.
# а) Определить его максимальную цифру.
# б) Определить его минимальную цифру.

num = 0
max_digit = 0
min_digit = 9
num = int(input("ввести натуральное число: "))

while num > 0:
    current_digit = num % 10

    if current_digit > max_digit:
        max_digit = current_digit

    if current_digit < min_digit:
        min_digit = current_digit

    # num = num // 10
print(f"максимальная цифра: {max_digit}")
print(f"минимальная цифра: {min_digit}")