year = 0
year = int(input("ввести год: "))

if year % 400 == 0:
    print(f"12/09/{year}")
elif year // 4 and year % 100 != 0:
    print(f"12/09/{year}")
else:
    print(f"13/09/{year}")