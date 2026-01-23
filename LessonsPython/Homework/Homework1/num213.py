# 1.вывести подсказку написать трехзначное число
# 2.компьютер читает число справа налево
# 3.компьютер выводит результат

user_number = 0

user_number = int( input("ввести трехзначное число: "))

digit1 = user_number // 100
digit2 = (user_number % 100) // 10
digit3 = user_number % 10

new_number = digit3 * 100 + digit2 * 10 + digit1 

# print(f"полученное число: {new_number}")

if 100 < user_number < 999:
   print(f"полученное число: {new_number}")
else:
   print("ошибка")