N = 0
M = 0
K = 0

N = int(input("ввести количество шишек: "))
M = int(input("ввести количество орешков: "))
K = int(input("ввести минимум для пропитания: "))

if N * M >= K:
    print("yes")
else:
    print("no")