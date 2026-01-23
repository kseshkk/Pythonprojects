# написать программу которая определяет простое число или составное

# number = int(input("введите число: "))

number = 0

while number <= 0:
    number = int(input("введите число: "))


if number % 2 > 0:
    print("простое число")
elif number == 2:
    print("простое число")
else:
    print("составное число")