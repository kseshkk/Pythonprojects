def find_simple(number):
    if number % 2 == 0:
        return False
    
    for i in range(3, number, 2):
        if number % i == 0:
            return False
        
    return True



for number in range(100, 999 + 1):
    if find_simple(number) == True:
        print(number)