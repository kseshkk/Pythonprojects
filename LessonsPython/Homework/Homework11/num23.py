file_in = open("INPUT.txt", "r", encoding="utf-8")
file_out = open("OUTPUT.txt", "w", encoding="utf-8")

n = int(file_in.readline())
sum = 0

for i in range(1,n + 1):
    if n % i == 0:
        sum += i

file_out.write(f"{sum}")

file_in.close()
file_out.close()