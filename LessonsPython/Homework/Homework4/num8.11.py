count_workers = 12
count_months = 3
current_salary = 0
sum_salaries = 0

for num_worker in range(1, count_workers + 1):
    for number_month in range(1, count_months + 1):
        current_salary = int(input(f"ввести зарплату {num_worker} работника за {number_month} месяц: "))
        sum_salaries += current_salary

print(f"")