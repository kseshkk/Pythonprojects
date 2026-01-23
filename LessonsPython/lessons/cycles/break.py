is_complex = False
num = 100

for devider in range(2, num):
    if num % devider == 0:
        is_complex = True
        break

if is_complex == True:
    print(f"число {num} составное")
else:
    print(f"число {num} простое")