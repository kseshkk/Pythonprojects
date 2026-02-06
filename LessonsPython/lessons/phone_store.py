from dataclasses import dataclass

@dataclass
class MobilePhone:
    id: int
    brand: str
    model: str
    weight: int
    screen_diagonal: float
    battery: int
    status: str
    price: int
    amount: int

GLOBAL_MOBILE_PHONE_ID = 0

# функциональные требования:

# сущность:
#     мобильныйтелефон
# поля:
#     ид - целое уникальное число
#     марка - строка (максимум 10 символов)
#     модель - строка (максимум 15 символов)
#     вес - целое число
#     диагональ экрана - дробное число
#     емкость аккумулятора - целое число
#     состояние - строка (макс 10 символов)
#     цена - целое число
#     количество на складе - целое число

# действия в программе:

# 1) Поиск мобильных телефонов по:
#     ид
#     марка
#     цена

# 2) Сортировка мобильных телефонов по:
#     ид
#     цена
#     диагональ экрана
#     ёмкость аккумулятора
#     вес

# 3) Добавлять новые мобильные телефоны в список
def input_phone_data():
    print("введите данные телефона")
    brand = input("марку: ")
    model = input("модель: ")
    weight = int(input("вес: "))
    screen_diagonal = float(input("диагональ экрана: "))
    battery = int(input("ёмкость аккумулятора: "))
    status = input("статус (поддержанный, новый): ")
    price = int(input("цена: "))
    amount = int(input("количество на складе: "))

    return MobilePhone(0, brand, model, weight, screen_diagonal, battery, status, price, amount)

def add_phone_to_list(phones, phone):
    global GLOBAL_MOBILE_PHONE_ID
    GLOBAL_MOBILE_PHONE_ID += 1

    phone.id = GLOBAL_MOBILE_PHONE_ID

    phones.append(phone)


# 4) Удалять мобильные телефоны из списка по ИД
def find_phone_index_by_id(phones, id):
    for i in range(len(phones)):
        if phones[i].id == id:
            return i
        
    return -1

def delete_phone_by_id(phones, id):
    delete_index = find_phone_index_by_id(phones, id)

    if delete_index != 1:
        phones.pop(delete_index)
        return True

    return False

# 5) Изменить поле "количество на складе" в сущности мобильный телефон
# 6) изменить всю информацию о мобильном телефоне, кроме поля ид, предварительно найдя его по ид
# 7) Вывести список всех мобильных телефонов

def print_phones(phones):
    print(
        f"{'ИД':<10}{'Марка':<15}{'Модель':<16}{'Вес':<10}{'Диаг(inch)':<15}{'Аккум(мАч)':<15}{'Состояние':<15}{'Цена(руб)':<15}{'В наличии':<15}"
    )

    for item in phones:
        print(
            f"{item.id:<10}{item.brand:<15}{item.model:<16}{item.weight:<10}{item.screen_diagonal:<15.1f}{item.battery:<15}{item.status:<15}{item.price:<15}{item.amount:<15}"
        )


# 8) Вывести мобильный телефон по ид
def print_phone_by_id(phones, id):
    print_index = find_phone_index_by_id(phones, id)

    if print_index != -1:
        print(
            f"{'ИД':<10}{'Марка':<15}{'Модель':<16}{'Вес':<10}{'Диаг(inch)':<15}{'Аккум(мАч)':<15}{'Состояние':<15}{'Цена(руб)':<15}{'В наличии':<15}"
    )
        item = phones[print_index]
        print(
                f"{item.id:<10}{item.brand:<15}{item.model:<16}{item.weight:<10}{item.screen_diagonal:<15.1f}{item.battery:<15}{item.status:<15}{item.price:<15}{item.amount:<15}"
        )
    else:
        print(f"телефон с id = {id} не найден")


# 9) Сохранить список мобильных телефонов в текстовый файл в 2 вариантах:
#     для удобного чтения человеком
#     для последующей удобной загрузки компьютером в эту программу (по одному полю на строку)
# 10) Загрузить список мобильных телефонов из текстового файла


phones = []

# add_phone_to_list(phones, input_phone_data())
# add_phone_to_list(phones, input_phone_data())

add_phone_to_list(
    phones, MobilePhone(1, "brand1", "model1", 10, 3.4, 228, "status1", 123, 10)
)
add_phone_to_list(
    phones, MobilePhone(2, "brand2", "model2", 10, 3, 228, "status2", 123, 10)
)

print_phones(phones)