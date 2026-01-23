# 11.13. Составить программу вывода на экран любого элемента массива по его индексу.

count_elements = 0
collection = []
count_elements = int(input("ввести кол-во элементов: "))

for _ in range(count_elements):
    collection.append(int(input("ввести элемент: ")))

# print(collection)

i = int(input("ввести индекс: "))
print(collection[i])