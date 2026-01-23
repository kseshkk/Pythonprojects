import random

comp_number = random.randint(1,100)
user_number = 0
is_guess = False

print("загадано число от 1 до 100")

while is_guess == False:
    user_number = int(input("ввести число: "))
    
    if user_number > comp_number:
        print("ввести число меньше")
    elif user_number < comp_number: 
        print("ввести число больше")
    else: 
        print("победа")
        is_guess = True