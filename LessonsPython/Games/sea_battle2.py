import random

ALIVE_SHIP = "K"
DEAD_SHIP = "X"
MISS_CELL = "O"
EMPTY_CELL = "."

COLS = 10
ROWS = 10

COUNT_SHIPS = 10

USER_STEP = "USER"
COMP_STEP = "COMP"

USER_WINNER = "USER"
COMP_WINNER = "COMP"

def input_number(message):
    is_good_number = False
    number = 0

    while is_good_number == False:
        temp = input(message)

        if temp.isdigit() == True:
            number = int(temp)
            is_good_number = True
        else:
            print("Ошибка. Вы ввели не число")

    return number

def create_user_field(user_field):
    for i in range(ROWS):
        user_field.append([])
        for j in range(COLS):
            user_field[i].append(EMPTY_CELL)

    return user_field

def create_comp_field(comp_field):
    for i in range(ROWS):
        comp_field.append([])
        for j in range(COLS):
            comp_field[i].append(EMPTY_CELL)

def fill_user_field(user_field):
    for _ in range(COUNT_SHIPS):
        continue_random = True
        i_rand = 0
        j_rand = 0
        while continue_random == True:
            i_rand = random.randint(0, ROWS - 1)
            j_rand = random.randint(0, COLS - 1)

            if user_field[i_rand][j_rand] == EMPTY_CELL:
                user_field[i_rand][j_rand] = ALIVE_SHIP
                continue_random = False

def fill_comp_field(comp_field):
    for _ in range(COUNT_SHIPS):
        continue_random = True
        i_rand = 0
        j_rand = 0
        while continue_random == True:
            i_rand = random.randint(0, ROWS - 1)
            j_rand = random.randint(0, COLS - 1)

            if comp_field[i_rand][j_rand] == EMPTY_CELL:
                comp_field[i_rand][j_rand] = ALIVE_SHIP
                continue_random = False

def get_current_step():
    current_step = ""

    if random.randint(1, 1000) < 500:
        current_step = USER_STEP
    else:
        current_step = COMP_STEP

    return current_step

def print_current_step(game_step):
    game_step += 1

    print()
    print("====================")
    print()
    print(f"Раунд {game_step}")
    print()

    return game_step
    
def print_user_field(user_field):
    print("Поле человека: ")
    for i in range(ROWS):
        for j in range(COLS):
            print(user_field[i][j], end=" ")
        print()

def print_comp_field(comp_field):
    print("Поле компьютера: ")
    for i in range(ROWS):
        for j in range(COLS):
            if comp_field[i][j] == ALIVE_SHIP:
                print(EMPTY_CELL, end=" ")
            else:
                print(comp_field[i][j], end=" ")
        print()

    print()

def make_user_step(comp_field, comp_alive_ships):
    print("Ход человека:")
    i_input = 0
    j_input = 0

    continue_input = True

    while continue_input == True:
        i_input = input_number("введите номер строки: ") - 1
        j_input = input_number("введите номер столбца: ") - 1

        if (
            i_input >= 0
            and i_input <= ROWS - 1
            and j_input >= 0
            and j_input <= COLS - 1
        ):
            if (
                comp_field[i_input][j_input] == ALIVE_SHIP
                or comp_field[i_input][j_input] == EMPTY_CELL
            ):
                continue_input = False
            else:
                print("Ошибка. Вы уже стреляли в эту клетку. Повторите снова")
        else:
            print("Ошибка ввода координат. Повторите снова")

    if comp_field[i_input][j_input] == ALIVE_SHIP:
        comp_field[i_input][j_input] = DEAD_SHIP
        comp_alive_ships -= 1
        print(f"Выстрел по координатам ({i_input+1};{j_input+1}) - убит")
        print(f"У противника осталось кораблей: {comp_alive_ships}")

    elif comp_field[i_input][j_input] == EMPTY_CELL:
        comp_field[i_input][j_input] = MISS_CELL
        

        print(f"Выстрел по координатам ({i_input+1};{j_input+1}) - промах")
        print(f"У противника осталось кораблей: {comp_alive_ships}")
    return comp_alive_ships

def make_comp_step(user_field, user_alive_ships):
    input("Ход компьютера (нажмите Enter для продолжения):")

    i_input = 0
    j_input = 0

    continue_input = True

    while continue_input == True:
        i_input = random.randint(0, ROWS - 1)
        j_input = random.randint(0, COLS - 1)

        if (
            user_field[i_input][j_input] == ALIVE_SHIP
            or user_field[i_input][j_input] == EMPTY_CELL
        ):
            continue_input = False

    if user_field[i_input][j_input] == ALIVE_SHIP:
        user_field[i_input][j_input] = DEAD_SHIP
        user_alive_ships -= 1

        print(f"Выстрел по координатам ({i_input+1};{j_input+1}) - убит")
        print(f"У человека осталось кораблей: {user_alive_ships}")
        input("Нажмите Enter для продолжения")

    elif user_field[i_input][j_input] == EMPTY_CELL:
        user_field[i_input][j_input] = MISS_CELL
        
        print(f"Выстрел по координатам ({i_input+1};{j_input+1}) - промах")
        print(f"У человека осталось кораблей: {user_alive_ships}")
        input("Нажмите Enter для продолжения")
    return user_alive_ships


def is_user_win(comp_alive_ships):
    
    if comp_alive_ships == 0:
        winner = USER_WINNER
    return winner

def is_comp_win(user_alive_ships):
    
    if user_alive_ships == 0:
        winner = COMP_WINNER
    return winner

def print_winner(winner):
    if winner == USER_WINNER:
        print("Победил пользователь")
    elif winner == COMP_WINNER:
        print("Победил компьютер")

def is_repeat_game():
    repeat_game = True
    print()
    repeat_answer = input("Хотите сыграть ещё раз? Введите y - для повтора, n - для отказа: ")

    if repeat_answer == "n":
        repeat_game = False

    return repeat_game

repeat_game = True

while repeat_game == True:
    user_field = []
    comp_field = []

    current_step = get_current_step()
    create_user_field(user_field)
    fill_user_field(user_field)

    create_comp_field(comp_field)
    fill_comp_field(comp_field)

    user_alive_ships = COUNT_SHIPS
    comp_alive_ships = COUNT_SHIPS
    winner = ""
    game_step = 0

    game_is_running = True

    while game_is_running == True:
        game_step = print_current_step(game_step)

        print_user_field(user_field)
        print_comp_field(comp_field)
        

        if current_step == USER_STEP:
            comp_alive_ships = make_user_step(comp_field, comp_alive_ships)
            current_step = COMP_STEP

        elif current_step == COMP_STEP:
            user_alive_ships = make_comp_step(user_field, user_alive_ships)
            current_step = USER_STEP

        winner_user = is_user_win(comp_alive_ships)
        winner_comp = is_comp_win(user_alive_ships)

        if winner_user == USER_WINNER:
            winner = USER_WINNER 
            game_is_running = False
        elif winner_comp == COMP_WINNER:
            winner = COMP_WINNER
            game_is_running = False

    print_current_step(game_step)
    print_winner(winner)

    repeat_game = is_repeat_game()