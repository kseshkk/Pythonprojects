# 11.56. Определить сумму второго, четвертого, шестого и т. д. элементов массива.

collection = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = 0

for elements in range(0, len(collection) + 1, 2):
    sum = sum + elements

print(sum)