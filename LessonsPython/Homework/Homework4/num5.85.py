# 5.85. Дано пятизначное число. Найти число, получаемое при прочтении его цифр
# справа налево.

number = 0
number = int(input("ввести пятизначное число: "))

while number > 0:
    print(number % 10)
    number = number // 10

# for i in range(5):
#     print(number % 10)
#     number = number // 10