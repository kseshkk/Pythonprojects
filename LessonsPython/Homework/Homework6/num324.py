number = 0
number = int(input("ввести четырехзначное число: "))

digit1 = number // 1000
digit2 = number // 100 % 10
digit3 = number % 100 // 10
digit4 = number % 10

if digit1 == digit4 and digit2 == digit3:
    print("yes")
else:
    print("no")