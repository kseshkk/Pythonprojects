count_workers = 0
salary = 0
result = 0
list = []

while count_workers < 3:
    count_workers = count_workers + 1
    salary = int(input(f"ввести зарплату {count_workers} работника: "))
    list.append(salary)

# print(list)
result = max(list) - min(list)
print(result)