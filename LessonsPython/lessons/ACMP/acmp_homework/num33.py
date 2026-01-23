numbers = input()
numbers_list = numbers.split()

Garry = int(numbers_list[0])
Larry = int(numbers_list[1])

count_cans = Garry + Larry - 1
print(f"{count_cans - Garry} {count_cans - Larry}")