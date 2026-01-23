year = int(input())

normal_year = ""
if year >= 1000:
    normal_year = str(year)
elif year >= 100 and year <= 999:
    normal_year = "0" + str(year)
elif year >= 10 and year <= 99:
    normal_year = "00" + str(year)
elif year >= 0 and year <= 9:
    normal_year = "000" + str(year)

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"12/09/{normal_year}")
else:
    print(f"13/09/{normal_year}")