def fact(number):
    if number == 0:
        return 1

    result = 1
    for i in range(1, number + 1):
        result *= i

    return result


result = (fact(2) + fact(5)) / fact(7)


print(f"результат выражения = {result}")
