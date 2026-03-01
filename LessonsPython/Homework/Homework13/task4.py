import os
from dataclasses import dataclass

@dataclass
class FILM:
    id: int
    name: str
    genre: str
    director:str
    release: int
    duration: int
    rating: float
    price: int
    copy: int

def input_int(message: str, min_number: int, max_number: int) -> int:
    is_correct_input = False

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
            print(f"Ошибка ввода. Вы ввели не число")
            is_correct_input = False

    return number

def input_float(message: str, min_number: float, max_number: float) -> float:
    is_correct_input = False

    while is_correct_input == False:
        try:
            number = float(input(message).strip())

            if number < min_number or number > max_number:
                print(
                    f"Ошибка ввода. Значение должно быть в границах от {min_number} до {max_number}"
                )
                is_correct_input = False
            else:
                is_correct_input = True
        except:
            print(f"Ошибка ввода. Вы ввели не число")
            is_correct_input = False

    return number

def input_str(message: str, min_length: int, max_length: int) -> str:
    is_correct_input = False

    while is_correct_input == False:
        str_data = input(message).strip()

        if len(str_data) < min_length or len(str_data) > max_length:
            print(
                f"Ошибка ввода. Количество символов должно быть в границах от {min_length} до {max_length}"
            )
            is_correct_input = False
        else:
            is_correct_input = True

    return str_data

NAME_MIN_LEN = 1
NAME_MAX_LEN = 25

GENRE_MIN_LEN = 1
GENRE_MAX_LEN = 15

DIRECTOR_MIN_LEN = 1
DIRECTOR_MAX_LEN = 20

RELEASE_MIN_LEN = 1895
RELEASE_MAX_LEN = 2027

DURATION_MIN_LEN = 1
DURATION_MAX_LEN = 10000

RATING_MIN_LEN = 1
RATING_MAX_LEN = 10

PRICE_MIN_LEN = 0
PRICE_MAX_LEN = 10000

COPY_MIN_LEN = 1
COPY_MAX_LEN = 10000


GLOBAL_FILM_ID = 0
ASC = "ascending"
DESC = "descending"

def add_film_to_list(films, film):
    global GLOBAL_FILM_ID
    GLOBAL_FILM_ID += 1

    film.id = GLOBAL_FILM_ID
    films.append(film)

def input_film_data():
    admin_answer = "yes"
    films = []
    while admin_answer == "yes":
        print("Введите данные фильма")
        name = input_str("Название: ", NAME_MIN_LEN, NAME_MAX_LEN)
        genre = input_str("Жанр: ", GENRE_MIN_LEN, GENRE_MAX_LEN)
        director = input_str("Режиссер: ", DIRECTOR_MIN_LEN, DIRECTOR_MAX_LEN)
        release = input_int("Год релиза: ", RELEASE_MIN_LEN, RELEASE_MAX_LEN)
        duration = input_int("Длительность: ", DURATION_MIN_LEN, DURATION_MAX_LEN)
        rating = input_float("Рейтинг: ", RATING_MIN_LEN, RATING_MAX_LEN)
        price = input_int("Цена: ", PRICE_MIN_LEN, PRICE_MAX_LEN)
        copy = input_int("Кол-во копий: ", COPY_MIN_LEN, COPY_MAX_LEN)

        new_film = FILM(0, name, genre, director, release, duration,rating, price, copy)
        add_film_to_list(films, new_film)

        os.system('cls')
        admin_answer = input("Хотите добавить еще фильм?(yes/no): ").lower()

    return films


# 1 поиск фильмов
def find_film_release(films: list[FILM]) -> list[FILM]:

    print("Введите диапазон годов выпуска фильма, что хотите найти")
    user_find1 = input_int("1ый год: ", RELEASE_MIN_LEN, RELEASE_MAX_LEN)
    user_find2 = input_int("2ой год: ", RELEASE_MIN_LEN, RELEASE_MAX_LEN)

    return [item for item in films if user_find1 <= item.release <= user_find2]
                

def find_film_genre(films: list[FILM], genre: str) -> list[FILM]:
        print("Результаты поиска:")
        return [item for item in films if item.genre.lower() == genre.lower()]


# 2 сортировка фильмов
def sorting_movies_duration(films: list[FILM], order) -> None:
    if order == ASC:
        films.sort(key=lambda item: item.duration, reverse = False)
    else:
        films.sort(key=lambda item: item.duration, reverse = True)
    print("Список фильмов по длительности отсортирован")

def sorting_movies_rating(films: list[FILM], order) -> None:
    films.sort(key=lambda item: item.rating, reverse = order)
    print("Список фильмов по рейтингу отсортирован")


# 3 подсчитать среднюю длительность фильмов
def average_film_duration(films):
    if len(films) == 0:
        print("Нет фильмов для расчета средней длительности.")

        return

    os.system('cls')
    print("Средняя длительность фильмов\n" + "-" * 40)

    total_duration = 0
    for movie in films:
        total_duration += movie.duration

    average = total_duration / len(films)

    print(f"Кол-во фильмов:{len(films)}")
    print(f"Суммарная длительность:{total_duration} минут")
    print(f"Средняя длительность:{average:2f} минут")

    print("\nВсе фильмы:")
    for movie in films:
        print(f" - {movie.name}: {movie.duration} минут")


# 4 вывести топ-3 фильма по рейтингу
def top_3_by_raiting(films):
    if len(films) == 0:
        print("Нет фильмов для отображения.")

        return

    os.system('cls')
    print("Топ 3 фильма по рейтингу\n" + "=" * 40)

    sorted_films = sorted(films, key=lambda film: film.rating, reverse=True)
    coun = min(3, len(sorted_films))

    print(f"Рейтинг основан на оценке от 0.0 до 10.0\n")

    for i in range(coun):
        film = sorted_films[i]
        print(f"{i+1}. {film.name}")
        print(f"Рейтинг:{film.rating}")
        print(f"Жанр:{film.genre}")
        print(f"Год:{film.release}")
        print(f"Длительность:{film.duration} мин")

    if len(films) < 3:
        print(f"Всего доступно фильмов {len(films)}")
        print("=" * 40)

    print("\nВсе фильмы с рейтингами:")
    for film in sorted_films:
        print(f" - {film.name}: {film.rating}")



# 5. увеличить цену фильмов, выпущенных до 2000 года
def increase_price_for_old_films(films):

    if len(films) == 0:
        print("Нет фильмов для обработки.")

        return

    os.system('cls')
    print("Увеличение цены для фильмов до 2000 года\n" + "=" * 50)

    print("Введите процент увеличения цены(пример: 10 25 40):")
    try:
        percent = float(input("Процент: "))
    except ValueError:
        print("Ошибка!Введите число.")
        return

    old_price_films = []
    total_increase = 0

    for film in films:
        if film.release < 2000:
            old_price = film.price
            increase_amount = old_price * (percent / 100)
            film.price = int(old_price + increase_amount)
            total_increase += increase_amount
            old_price_films.append({
                'film': film,
                'old_price': old_price,
                'increase': increase_amount
                })
    
    if old_price_films:
        print(f"\nЦены увеличены на {percent}% для {len(old_price_films)} фильмов: ")
        print("-" * 50)

        for i, item in enumerate(old_price_films, 1):
            film = item['film']
            print(f"{i}. {film.name}({film.release} г.)")
            print(f"Было: {item['old_price']} рублей - Стало:{film.price} рублей")
            print(f"Увеличение: + {int(item['increase'])} рублей.")
            print()
        
        print(f"Общая сумма увеличения: + {int(total_increase)} рублей.")
    else:
        print("\nНет фильмов выпущенных до 2000 года.")

    print("\n" + "=" * 50)
    print("ВСЕ ФИЛЬМЫ С ЦЕНАМИ:")
    for film in films:
        year_status = "(до 2000 года.)" if film.release < 2000 else "(после 2000 года.)"
        print(f" - {film.name}({film.release} г.) {year_status}: {film.price} рублей.")


# 6. пометить фильмы длительностью более 150 минут как «эпик»
def tag_duration_more_150_minutes(films):
    result = []
    for film in films:
        if film.duration > 150:
            result.append(f"{film.name} - эпик")
    return result

# 7. сгруппировать фильмы по жанрам и вывести результат
def group_by_genre(films):
    all_genres = []

    for film in films:
        if film.genre not in all_genres:
            all_genres.append(film.genre)

    films_by_genre = []
    for genre in all_genres:
        genre_films = []
        for film in films:
            if film.genre == genre:
                genre_films.append(film)
        films_by_genre.append([genre, genre_films])    

    return films_by_genre
    
def print_grouped_films(films):
    grouped = group_by_genre(films)

    for i in grouped:
        genre = i[0]
        films_list = i[1]
        print(f"Жанр: {genre}")
        for film in films_list:
            print(f"Название: {film.name}")
            print("-" * 50)

# 8 удалить фильмы с рейтингом ниже 5.0
def delete_film_by_rating(films: list[FILM]) -> list[FILM]:
    return [item for item in films if item.rating >= 5]

    # retained_films = []
    # for film in films:
    #     if film.rating >= 5.0:
    #         retained_films.append(film)
    # return retained_films

# дополнительные функции:
# 1. вывести фильмы дороже указанной суммы
def print_films_more_expensive(films: list[FILM], user_price) -> list[FILM]:
    print("Результаты поиска:")
    return [item for item in films if item.price > user_price]


    # user_price = int(input("Введите минимальную цену: "))
    # correct_films = []
    # for film in films:
    #     if film.price > user_price:
    #         correct_films.append(film)
    # return correct_films

# 2. изменить жанр фильма по ИД
def find_film_by_id(films, id):
    for i in range(len(films)):
        if films[i].id == id:
            return i

    return -1

def change_genre_by_id(films):
    id = int(input("Введите id фильма: "))
    user_index = find_film_by_id(films, id)

    if user_index == -1:
        print(f"Фильм с id = {id} не найден")
        return
    
    new_genre = input("Введите новый жанр: ").strip()
    films[user_index].genre = new_genre
    print(f"Жанр фильма изменен на '{new_genre}'")
    
# 3. подсчитать общее кол-во копий всех фильмов
def count_total_copies(films):
    total_copies = 0

    for film in films:
        total_copies += film.copy

    print(f"Общее количество копий всех фильмов: {total_copies}")

    print("\nДетализация по фильмам: ")
    for film in films:
        print("f {film.name}: {film.copy} копий")

    return total_copies

# 4. определить самый старый фильм
def find_old_movie(film):
    if len(films) == 0:
        print("Список пуст.Нельзя найти самый старый фильм.)")

        return 

    years = []
    for film in films:
        years.append(film.release)

    min_year = min(years)

    for film in films:
        if film.release == min_year:
            oldest_film = film
            break

    print(f"Самый старый фильм:{oldest_film.name} - {oldest_film.release} год.")

    return oldest_film

# 5. Вывести уникальных режиссеров
def find_unique_director(films):
    unique_director = []
    i = 0
    for film in films:  
        if film.director not in unique_director:
            unique_director.append(film.director)
    
    print("УНИКАЛЬНЫЕ РЕЖИССЕРЫ")
    for director in unique_director:
        i += 1
        print(f"{i}. {director}")

# вывести все фильмы
def print_all_films(films: list[FILM]) -> None:
    if len(films) == 0:
        print("Список фильмов пуст")
        return
    
    print("ВСЕ ФИЛЬМЫ\n----------------")
    for item in films:
        print(f"ИД - {item.id}")
        print(f"Название - {item.name}")
        print(f"Жанр - {item.genre}")
        print(f"Режиссёр - {item.director}")
        print(f"Год релиза - {item.release}")
        print(f"Длительность - {item.duration}")
        print(f"Рейтинг - {item.rating}")
        print(f"Цена - {item.price}")
        print(f"Кол-во копий - {item.copy}")
        print("\n" + "=" * 50)

def main_screen():
    print_all_films(films)

    print("Выберите действие\n----------------")
    print("1. Поиск фильма")
    print("2. Сортировка фильмов")
    print("3. Средняя длительность")
    print("4. ТОП 3 фильма")
    print("5. Жанры фильмов")
    print("6. Вывести всех режиссеров")
    print("7. Админ")
    print("0. Выйти из программы")

    what_user_want = input_int("Действие: ", 0, 7)
    
    return what_user_want

def cell_input():

    print("-"*40)
    print("НАЖМИТЕ Enter ДЛЯ ВЫХОДА В ГЛАВНОЕ МЕНЮ")
    input("Enter: ")

films = []
is_run = True

while is_run == True:
    what_user_want = main_screen() 

    if what_user_want == 0:
        is_run = False

    if what_user_want == 1:
        finded_films: list[FILM] = []
        print("Поиск по году выпуска или по жанру")
        print("1. Диапазон годов ")
        print("2. Жанр ")
        what_user_want = input_int("Действие: ", 1, 2)
        if what_user_want == 1:
            print("Результаты поиска")
            finded_films = find_film_release(films)
            
        if what_user_want == 2:
            print("Введите жанр фильма, что хотите найти")
            genre = input("жанр: ")
            finded_films = find_film_genre(films, genre)
        print(finded_films)
        cell_input()

    if what_user_want == 2:
        print("Вывести фильмы по длительности или рейтингу?")
        print("1. Длительности")
        print("2. Рейтингу")
        what_user_want = input_int("Действие: ", 1, 2)
        print("Выберите параметр сортировки")

        print("1. По возрастанию")
        print("2. По убыванию")

        order_point = input_int("Выберите пункт меню: ", 1, 2)

        order = ""
        if order_point == 1:
            order = ASC
        elif order_point == 2:
            order = DESC

        if what_user_want == 1:
            sorting_movies_duration(films, order)
            
        if what_user_want == 2:
            sorting_movies_rating(films, order)
            

    if what_user_want == 3:
        average_film_duration(films)
        cell_input()

    if what_user_want == 4:
        top_3_by_raiting(films)
        cell_input()

    if what_user_want == 5:
        increase_price_for_old_films(films)
        cell_input()

    if what_user_want == 6:
        find_unique_director(films)
        cell_input()


    if what_user_want == 7:
        print("Выберите дейтвие\n----------------")
        print("1. Удалить фильмы с рейтингом ниже 5 ")
        print("2. Сгрупировать фильмы по жанрам")
        print("3. Пометить фильмы длительностью более 150 минут как «эпик»")
        print("4. Увеличить цену фильмов, выпущенных до 2000 года")
        print("5. Добавить фильм")
        print("6. Вывести фильмы дороже указанной суммы")
        print("7. Изменить жанр фильма по ИД")
        what_user_want = input_int("Действие: ", 1, 7)

        finded_films: list[FILM] = []

        if what_user_want == 1:
            finded_films = delete_film_by_rating(films)
            print(finded_films)
            cell_input()

        if what_user_want == 2:
            print_grouped_films(films)
            cell_input()

        if what_user_want == 3:
            tag_duration_more_150_minutes(films)
            cell_input()

        if what_user_want == 4:
            increase_price_for_old_films(films)
            cell_input()
        
        if what_user_want == 5:
            films = input_film_data()
            cell_input()

        if what_user_want == 6:
            user_price = input_int("Введите мин цену: ", 0, 10000)
            finded_films = print_films_more_expensive(films, user_price)
            print(finded_films)
            cell_input()
        
        if what_user_want == 7:
            change_genre_by_id(films)
            cell_input()