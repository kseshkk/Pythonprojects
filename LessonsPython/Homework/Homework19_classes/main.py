from participant import Participant
from captain import Captain
from tournament import Tournament
from decorators import log_action
import console_services

tournament = Tournament()

while True:
    print("=== Школьный турнир знаний ===")
    console_services.print_devider()
    print("1. Добавить обычного участника")
    print("2. Добавить капитана команды")
    print("3. Просмотр всех участников")
    print("4. Начислить баллы")
    print("5. Снять баллы")
    print("6. Показать рейтинг")
    print("7. Показать __dict__ участников")
    print("8. Удалить участника")
    print("9. Определить победителя")
    print("0. Выход")
    console_services.print_devider()
    user_choice = console_services.input_int("Выберите действие: ", 0, 9)
    console_services.clear_console()


    if user_choice == 0:
        break

    elif user_choice == 1:
        print("Добавление участника")
        console_services.print_devider()

        while True:
            choice = input("Добавить участника? (да/нет): ")

            if choice == "нет":
                break

            elif choice == "да":
                name = console_services.input_str("Имя: ",1 , 20)
                school_class = console_services.input_str("Класс: ", 1, 20)

                current_participant = Participant(name, school_class)
                tournament.add_participant(current_participant)
                print("Участник добавлен")

            else:
                print("неизвестное сообщение. попробуйте еще раз")
    

    elif user_choice == 2:
        print("Добавление капитана")
        console_services.print_devider()
    
        while True:
            choice = input("Добавить капитана? (да/нет): ")

            if choice == "нет":
                break

            elif choice == "да":
                name = console_services.input_str("Имя: ",1,20)
                school_class = console_services.input_str("Класс: ",1,3)
                team_name = console_services.input_str("Название команды: ",1,30)

                current_captain = Captain(name, school_class, team_name)
                tournament.add_participant(current_captain)
                print("Капитан добавлен")

            else:
                print("неизвестное сообщение. попробуйте еще раз")

    elif user_choice == 3:
        tournament.show_participants()

    elif user_choice == 4:
        print("Добавление баллов участнику")

        name = console_services.input_str("введите имя участника: ", 1, 20)
        points = console_services.input_int("Введите количество баллов: ", 1, 100) 

        if tournament.find_participant(name):
            tournament.add_points_to_participant(name, points)
            print(f"Участнику {name} начислено {points} баллов")
        else:
            print("Участник не найден")

    elif user_choice == 5:
        print("Снятие баллов с участника")

        name = console_services.input_str("введите имя участника: ", 1, 20)
        points = console_services.input_int("Введите количество баллов: ", 1, 100) 
    
        participant = tournament.find_participant(name)
        if participant:
            old_score = participant._score
            tournament.remove_points_from_participant(name, points)
            new_score = participant._score
            print(f"Было: {old_score}\nСнимаем: {points}\nСтало: {new_score}")
        else:
            print("Участник не найден")



    elif user_choice == 6:
        tournament.show_rating()

    elif user_choice == 7:
        tournament.show_debug_info()

    elif user_choice == 8:
        name = console_services.input_str("Введите имя: ", 1, 20)
        tournament.remove_participant(name)

    elif user_choice == 9:
        winner = tournament.get_winner()
        if winner:
            print(f"Победитель турнира: {winner._name}, {winner._school_class} класс – {winner._score} баллов")

    elif user_choice == 0:
        break


    console_services.check_enter()
    console_services.clear_console()