user_num = 0
digit1 = 0 
digit2 = 0
digit3 = 0
digit4 = 0

user_num = int( input("ввести четырехзначное число: "))
digit1 = user_num // 1000
digit2 = (user_num // 100) % 10
digit3 = (user_num % 100) // 10
digit4 = user_num % 10

multiplication = digit1 * digit2 * digit3 * digit4
print(f"умножение = {multiplication}")