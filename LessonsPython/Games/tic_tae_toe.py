import random

ZERO = "o"
CROSS = "x"
EMPTY_CELL = "."
user_choice = 0
comp_choice = 0
field = []

COLS = 3
ROWS = 3

winner = ""

for i in range(ROWS):
    field.append([])
    for j in range(COLS):
        field[i].append(EMPTY_CELL)

    
print("Добро пожаловать в игру крестики-нолики!")

while True:
    user_choice = input("Введите каким символом будете играть х или о: ")
    if user_choice == ZERO:
        comp_choice = CROSS
        break
    elif user_choice == CROSS:
        comp_choice = ZERO
        break
    else:
        user_choice = input("Неверный символ. Введите еще раз: ")
        if user_choice == ZERO:
            comp_choice = CROSS
            break
        elif user_choice == CROSS:
            comp_choice = ZERO
            break

print(f"Ваш выбор - {user_choice}. Приятной игры!")

User_step = ""
Comp_step = ""
current_step = ""
count_steps = 0


if random.randint(1, 10) < 5:
    current_step = User_step
else:
    current_step = Comp_step

game_is_running = True

while game_is_running == True:

    if current_step == User_step:
        while current_step == User_step:
            for i in range(ROWS):
                for j in range(COLS):
                    print(field[i][j], end="")
                print()
            print("ход пользователя")
            i_input = int(input("введите номер строки: ")) - 1
            j_input = int(input("введите номер столбца: ")) - 1
        
            if i_input > 3:
                i_input = int(input("ошибка. введите номер строки от 1 до 3!: ")) - 1
            if j_input > 3:
                j_input = int(input("ошибка. введите номер столбца от 1 до 3!: ")) - 1

            if field[i_input][j_input] == EMPTY_CELL:
                field[i_input][j_input] = user_choice
                count_steps += 1
                current_step = Comp_step
                break
            else:
                i_input = int(input("На этом месте уже стоит символ. Попробуйте другой вариант! введите номер строки: ")) - 1
                j_input = int(input("введите номер столбца: ")) - 1
                field[i_input][j_input] = user_choice
            
    
        if field[0][0] == user_choice and field[0][1] == user_choice and field[0][2] == user_choice:
            winner = "user"
        elif field[1][0] == user_choice and field[1][1] == user_choice and field[1][2] == user_choice:
            winner = "user"
        elif field[2][0] == user_choice and field[2][1] == user_choice and field[2][2] == user_choice:
            winner = "user"
        elif field[0][0] == user_choice and field[1][0] == user_choice and field[2][0] == user_choice:
            winner = "user"
        elif field[0][1] == user_choice and field[1][1] == user_choice and field[2][1] == user_choice:
            winner = "user"
        elif field[0][2] == user_choice and field[1][2] == user_choice and field[2][2] == user_choice:
            winner = "user"
        elif field[0][0] == user_choice and field[1][1] == user_choice and field[2][2] == user_choice:
            winner = "user"
        elif field[0][2] == user_choice and field[1][1] == user_choice and field[2][0] == user_choice:
            winner = "user"

        if winner == "user":
            print("победил пользователь!")
            game_is_running = False
            break
        if count_steps == 9:
            print("ничья")
            game_is_running = False
            break
        
        

    if current_step == Comp_step:
        while current_step == Comp_step:
            for i in range(ROWS):
                for j in range(COLS):
                    print(field[i][j], end="")
                print()
            print("ход компьютера (нажмите Enter): ")
            input()

            i_input = random.randint(0, ROWS - 1)
            j_input = random.randint(0, COLS - 1)
            
            if field[i_input][j_input] == EMPTY_CELL:
                field[i_input][j_input] = comp_choice
                count_steps += 1
                current_step = User_step
                break
            

        if field[0][0] == comp_choice and field[0][1] == comp_choice and field[0][2] == comp_choice:
            winner = "comp"
        elif field[1][0] == comp_choice and field[1][1] == comp_choice and field[1][2] == comp_choice:
            winner = "comp"
        elif field[2][0] == comp_choice and field[2][1] == comp_choice and field[2][2] == comp_choice:
            winner = "comp"
        elif field[0][0] == comp_choice and field[1][0] == comp_choice and field[2][0] == comp_choice:
            winner = "comp"
        elif field[0][1] == comp_choice and field[1][1] == comp_choice and field[2][1] == comp_choice:
            winner = "comp"
        elif field[0][2] == comp_choice and field[1][2] == comp_choice and field[2][2] == comp_choice:
            winner = "comp"
        elif field[0][0] == comp_choice and field[1][1] == comp_choice and field[2][2] == comp_choice:
            winner = "comp"
        elif field[0][2] == comp_choice and field[1][1] == comp_choice and field[2][0] == comp_choice:
            winner = "comp"

        
        if winner == "comp":
            print("победил компьютер!")
            game_is_running = False
            break
        if count_steps == 9:
            print("ничья")
            game_is_running = False
            break

for i in range(ROWS):
    for j in range(COLS):
        print(field[i][j], end="")
    print()

print("Спасибо за игру!")
    