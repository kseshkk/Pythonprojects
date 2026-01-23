numbers = input()
numbers_list = numbers.split()

X = int(numbers_list[0])
Y = int(numbers_list[1])
Z = int(numbers_list[2])

if Z <= X + Y:
    print(X + Y - Z)
else:
    print("Impossible")