# 1.Вводится скорость в км/ч и скорость в м/с
# 2.Компьютер переводить вторую скорость в км/ч
# 3.Компьютер сравнивает числа 
# 4.Выводит пользователю ответ

first_num = 0
second_num = 0

first_num = int( input("ввести в м/с: "))
second_num = int( input ("ввести в км/ч: "))

newfirst_num = first_num * 3.6 
# print(f"число = {newfirst_num}")
if newfirst_num > second_num:
    print(f"скорость в м/с больше")
else:
    print(f"скорость в км/ч больше")