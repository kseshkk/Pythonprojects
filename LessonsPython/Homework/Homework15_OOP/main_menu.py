from robot import Robot
import os

def clear_console() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def input_int(message: str, min_number: int, max_number: int) -> int:
    is_correct_input = False
    number = 0

    while is_correct_input == False:
        try:
            number = int(input(message).strip())

            if number < min_number or number > max_number:
                print(
                    f"Ошибка ввода. Значение должно быть в границах от {min_number} до {max_number}"
                )
                is_correct_input = False
            else:
                is_correct_input = True
        except:
            print(f"Ошибка ввода. вы ввели не число")
            is_correct_input = False

    return number

robot = Robot(50, 50, True)

while robot.is_alive():
    robot.check_status()

    print("Выберите действие")
    print("1. Зарядить робота")
    print("2. Починить робота")
    print("3. Отправить работать")

    action = input_int("введите действие: ", 1, 3)
    
    if action == 1:
        robot.charge()
    elif action == 2:
        robot.repair()
    elif action == 3:
        robot.work()

    robot.normalized_parameters()