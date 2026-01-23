def input_number(message):
    is_good_number = False
    number = 0

    while is_good_number == False:
        temp = input(message)

        if temp.isdigit() == True:
            number = int(temp)
            is_good_number = True
        else:
            print("вы ввели не число")

    return number

def find_p():
    return a + b + c

a = input_number("ввести длину первой стороны: ")
b = input_number("ввести длину второй стороны: ")
c = input_number("ввести длину третьей стороны: ")

result = find_p()
print(result)