# 11.36. Дан массив. Напечатать:
# а) все неотрицательные элементы;
# б) все элементы, не превышающие число 100.

collection = [3, 102, -4, 0, 73, 11, -18, 459]

for elements in collection:
    if elements > 0:
        print(elements)