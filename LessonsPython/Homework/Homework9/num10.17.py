def find_factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i

    return result


result = (2 * find_factorial(5) + 3 * find_factorial(8)) / (find_factorial(6) + find_factorial(4))
print(result)