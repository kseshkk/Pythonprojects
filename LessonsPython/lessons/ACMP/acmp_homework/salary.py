numbers = input()
numbers_list = numbers.split()

First_worker = int(numbers_list[0])
Second_worker = int(numbers_list[1])
Third_worker = int(numbers_list[2])

max = First_worker
if Second_worker > First_worker:
    max = Second_worker
if Third_worker > max:
    max = Third_worker

min = First_worker
if Second_worker < First_worker:
    min = Second_worker
if Third_worker < min:
    min = Third_worker

print(max - min)