from foot_courier import FootCourier
from bike_courier import BikeCourier
from car_courier import CarCourier
import console_services
from decimal import Decimal

couriers_list = []

def create_foot_courier() -> FootCourier:
    print("\nСоздание пешего курьера")
    console_services.print_devider()

    name = console_services.input_str("Введите имя: ", 2, 30)
    experience = console_services.input_int("Опыт работы (мес): ", 0, 100)
    rating = console_services.input_float("Рейтинг (0-5): ", 0, 5)
    completed_orders = console_services.input_int("Кол-во выполненных заказов: ", 0, 10000)
    balance = Decimal(str(input("Баланс: ")))
    max_distance = console_services.input_float("Макс. дистанция (км): ", 0, 100)
    speed = console_services.input_float("Скорость (км/ч): ", 0, 10)
    
    return FootCourier(name, experience, rating, completed_orders, balance, False, max_distance, speed)

def create_bike_courier() -> BikeCourier:
    print("\nСоздание велокурьера")
    console_services.print_devider()

    name = console_services.input_str("Введите имя: ", 2, 30)
    experience = console_services.input_int("Опыт работы (мес): ", 0, 100)
    rating = console_services.input_float("Рейтинг (0-5): ", 0, 5)
    completed_orders = console_services.input_int("Кол-во выполненных заказов: ", 0, 10000)
    balance = Decimal(str(input("Баланс: ")))
    bike_type = console_services.input_str("Тип велосипеда: ", 2, 30)
    stamina = console_services.input_int("Выносливость: ", 0, 100)

    return BikeCourier(name, experience, rating, completed_orders, balance, False, bike_type, stamina)


def create_car_courier() -> CarCourier:
    print("\nСоздание автокурьера")
    console_services.print_devider()

    name = console_services.input_str("Введите имя: ", 2, 30)
    experience = console_services.input_int("Опыт работы (мес): ", 0, 100)
    rating = console_services.input_float("Рейтинг (0-5): ", 0, 5)
    completed_orders = console_services.input_int("Кол-во выполненных заказов: ", 0, 10000)
    balance = Decimal(str(input("Баланс: ")))
    car_model = console_services.input_str("Модель машины: ", 2, 30)
    fuel = console_services.input_float("Остаток топлива (л): ", 0, 100)
    fuel_consumption = console_services.input_float("Расход топлива (л/100км): ", 0, 100)
    
    return CarCourier(name, experience, rating, completed_orders, balance, False, car_model, fuel, fuel_consumption)

def add_courier() -> None:
    
    print("\nВыберите тип курьера:")
    print("1. Пеший")
    print("2. Велокурьер")
    print("3. Автокурьер")
    print("0. Назад")
    console_services.print_devider()

    choice = console_services.input_int("Введите действие: ", 0, 3)
    console_services.clear_console()

    if choice == 1:
        courier = create_foot_courier()
    elif choice == 2:
        courier = create_bike_courier()
    elif choice == 3:
        courier = create_car_courier()
    else:
        return
    
    courier_id = len(couriers_list) + 1
    couriers_list.append(courier)
    console_services.print_devider()

    print(f"Курьер добавлен. Его номер - {courier_id}")
    

def find_courier_by_id(courier_id) -> None:
    index = courier_id - 1
    if 0 <= index < len(couriers_list):
        return couriers_list[index]

def select_courier():
    courier_id = console_services.input_int("Выберите номер курьера: ", 1, len(couriers_list))
    return find_courier_by_id(courier_id) 

def show_all_couriers():
    print("Список доступных курьеров")
    for i in range(len(couriers_list)):
        courier = couriers_list[i]
        courier_id = i + 1

        courier_type = type(courier).__name__

        if courier_type == "FootCourier":
            type_name = "Пеший курьер"
        elif courier_type == "BikeCourier":
            type_name = "Велокурьер"
        elif courier_type == "CarCourier":
            type_name = "Автокурьер"


        print(f"{courier_id}. {type_name}")
        

def open_courier_menu():
    if len(couriers_list) == 0:
        print("Курьеров нет")
    else:
        courier = select_courier()
        while True:
            console_services.clear_console()
            console_services.print_devider()
            print(f"МЕНЮ КУРЬЕРА")
            print("1. Показать информацию")
            print("2. Выдать заказ")
            print("3. Завершить смену")

            max_choice = 3

            if type(courier).__name__ == "CarCourier":
                max_choice = 4
                print("4. Заправить автомобиль")

            print("0. Вернуться в главное меню")
            console_services.print_devider()
            user_choice = console_services.input_int("Выберите действие: ", 0, max_choice)
            console_services.clear_console()

            if user_choice == 0:
                break
            elif user_choice == 1:          
                courier.print_info()

            elif user_choice == 2:
                distance = console_services.input_float("Введите дистанцию (км): ", 0, 100)
                courier.deliver_order(distance)

            elif user_choice == 3:
                courier.finish_shift()

            elif user_choice == 4:
                liters = console_services.input_float("Введите кол-во литров для заправки: ", 0, 100)
                courier.refuel(liters)

            console_services.check_enter()


while True:
    console_services.clear_console()
    console_services.print_devider()

    print("ГЛАВНОЕ МЕНЮ")
    print("1. Добавить курьера")
    print("2. Вывести всех курьеров")
    print("3. Управлять конкретным курьером")
    print("0. Выход")
    console_services.print_devider()

    user_choice = console_services.input_int("Выберите действие: ", 0, 3)
    console_services.clear_console()

    if user_choice == 0:
        break
    elif user_choice == 1:
        add_courier()
    elif user_choice == 2:
        show_all_couriers()
    elif user_choice == 3:
        open_courier_menu()

    console_services.check_enter()