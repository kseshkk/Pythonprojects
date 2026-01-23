import random

collection = []

count_elements = 10

for _ in range(count_elements):
    collection.append(random.randint(1, 100))

# print(collection)

for i in range(count_elements):
     print(f"{i}: {collection[i]}")

collection[0] = 999

print(collection)

print(collection[1])

collection.pop(1)
# collection.clear()
# print(collection)

# collection(1, 777)
# print(collection)