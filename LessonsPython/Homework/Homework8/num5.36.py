x = 2
a = 3
b = 3

for _ in range(5):
    x = x + (x**a)/b
    a += 2
    b += 2

print(x)