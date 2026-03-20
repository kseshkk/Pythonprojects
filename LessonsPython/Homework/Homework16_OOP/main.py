from movie import Movie
from session import Session
from cinema import Cinema
import console_services


cinema_name = console_services.input_str("Введите название кинотеатра: ", 1, 20)
cinema: Cinema = Cinema(cinema_name)

is_run = True
run_program = True

while is_run == True:
    answer = console_services.input_str("Добавить сеанс? (да/нет): ", 2, 3)
    if answer == "нет":
        break

    name = console_services.input_str("Название: ", 1, 30)
    duration = console_services.input_int("Длительность (мин): ", 1, 300)
    age_limit = console_services.input_int("Возрастное ограничение: ", 0, 18)

    session_time = console_services.input_str("Время сеанса: ", 1, 10)
    ticket_price = console_services.input_int("Цена билета (руб): ", 0, 10000)
    number_of_seats = console_services.input_int("Количество мест: ", 0, 500)
    console_services.print_devider()

    cinema.add_session(Session(Movie(name, duration, age_limit), session_time, ticket_price, number_of_seats))

while run_program == True:
    console_services.clear_console()
    print(f"кинотеатр {cinema_name}")
    console_services.print_devider()

    print("ДОСТУПНЫЕ ДЕЙСТВИЯ\n")
    print("1. Показать все сеансы")
    print("2. Посмотреть свободные места на сеансе")
    print("3. Забронировать место")
    print("4. Отменить бронь")
    print("0. Выход\n")
    action = console_services.input_int("введите номер действия: ", 0, 5)
    console_services.print_devider()

    if action == 1:
        print(f"Всего сеансов: {cinema.get_sessions_count()}")
        sessions = cinema.show_sessions()
        print(sessions)
        
    elif action == 2:
        session_index = console_services.input_int("Введите номер сеанса: ", 1, cinema.get_sessions_count())
        curent_session = cinema.find_session_by_number(session_index)
        free_seats = curent_session.show_free_seats()
        print(f"Свободные места: {free_seats}")

        
     
    elif action == 3:
        session_index = console_services.input_int("Введите номер сеанса: ", 1, cinema.get_sessions_count())
        current_session = cinema.find_session_by_number(session_index)

        max_seats = current_session.get_total_seats()
        seat_number = console_services.input_int("Введите номер места: ", 1, max_seats)

        cinema.book_ticket(session_index, seat_number)


    elif action == 4:
        session_index = console_services.input_int("Введите номер сеанса: ", 1, cinema.get_sessions_count())
        current_session = cinema.find_session_by_number(session_index)

        max_seats = current_session.get_total_seats()
        seat_number = console_services.input_int("Введите номер места: ", 1, max_seats)

        cinema.cancel_ticket(session_index, seat_number)

    elif action == 0:
        run_program = False

    console_services.check_enter()
    console_services.print_devider()

