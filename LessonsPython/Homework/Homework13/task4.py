import os
from dataclasses import dataclass

@dataclass
class film():
    id: int
    name: str
    genre: str
    director:str
    release: int
    duration: int
    rating: float
    price: int
    copy: int

def input_int(message, min_number, max_number):
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

def input_float(message, min_number, max_number):
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

def input_str(message, min_length, max_length):
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


GLOBAL_FILM_ID = 0

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
        name = input_str("Название: ", 1, 25).lower
        genre = input_str("Жанр: ", 1, 15).lower
        director = input_str("Режиссер: ", 1, 20).lower
        release = input_int("Год релиза: ", 1895, 2027)
        duration = input_int("Длительность: ", 1, 10000)
        rating = input_float("Рейтинг: ", 1, 10)
        price = input_int("Цена: ", 0, 10000)
        copy = input_int("Кол-во копий: ", 0, 10000)

        new_film = film(0, name, genre, director, release, duration,rating, price, copy)
        add_film_to_list(films, new_film)

        os.system('cls')
        admin_answer = (input("Хотите добавить еще фильм?(yes/no): "))

    return films


# 1 поиск фильмов
def find_film_release(films):

    print("Введите диапазон годов выпуска фильма, что хотите найти")
    user_find1 = input_int("1ый год: ", 1895, 2027)
    user_find2 = input_int("2ой год: ", 1895, 2027)

    j = 0
    os.system('cls')
    print("РЕЗУЛЬТАТЫ ПОИСКА\n-----------------")
    for i in range(user_find1,user_find2+1):
        for item in films:
            if item.release == i:
                j +=1
                print(j,".",item.name)
                
    if j == 0:
        print("По вашему запросу ничего не нашлось.")

def find_film_genre(films):

    print("Введите жанр фильма, что хотите найти")
    user_find1 = (input("жанр: "))

    j = 0
    os.system('cls')
    print("РЕЗУЛЬТАТЫ ПОИСКА\n-----------------")
    for item in films:
        if item.genre == user_find1:
            j +=1
            print(j,".", item.name)
            
    if j == 0:
        print("По вашему запросу ничего не нашлось.")

# 2 сортировка фильмов
def sorting_movies_duration(films):
    durations = []
    os.system('cls')
    print("ФИЛЬМЫ\n-----------------")
    for item in films:
        durations.append(item.duration)
    for i in range(1,len(durations)+1):
        max_duration = max(durations)
        for item in films:
            if item.duration == max_duration:
                print(f"{i}. Название: {item.name} \nДлительность(мин): {item.duration}")

        index = durations.index(max_duration)
        durations.pop(index)
def sorting_movies_rating(films):
    ratings = []
    os.system('cls')
    print("ФИЛЬМЫ\n-----------------")
    for item in films:
        ratings.append(item.rating)
    for i in range(1,len(ratings)+1):
        max_rating = max(ratings)
        for item in films:
            if item.rating == max_rating:
                print(f"{i}. Название: {item.name} \nРейтинг: {item.rating}")

        index = ratings.index(max_rating)
        ratings.pop(index)



    if len(films) == 0:
        print("Нет фильмов дл яобработки.")

        return

    os.system('cls')
    print("Увеличение цены дл яфильмов до 2000 года\n" + "=" * 50)

    print("Введите процент увеличения цены(пример: 10б 25б 40):")
    try:
        percent = float(input("Процент: "))
    except ValueError:
        print("Ошибка!Введите число.")
        input("\nНажмите Enter для возврата в меню...")
        return

    old_price_films = []
    total_increase = 0

    for film in films:
        if film.release < 2000:
            old_price = film.price
            increase_amount = old_price * (percent / 100)
            film.price = int(old_price + increase_amount)
            total_increase += increase_amount
            old_price_films.apppend({
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
        print("\nНет фильмовб выпущенных до 2000 года.")

    print("\n" + "=" * 50)
    print("ВСЕ ФИЛЬМФ С ЦЕНАМИ:")
    for film in films:
        year_status = "(до 2000 года.)" if film.release < 2000 else "(после 2000 года.)"
        print(f" - {film.name}({film.release} г.) {year_status}: {film.price} рублей.")

    print("\n" + "=" * 50)
    input("\nНажмите Tnter для возврата в меню...")

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

    input("\nНажмите Enter для возврата в меню...")

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

    print("Введите процент увеличения цены(пример: 10б 25б 40):")
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

    print("\n" + "=" * 50)
    input("\nНажмите Tnter для возврата в меню...")

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

# 8 удалить фильмы с рейтингом ниже 5.0
def delete_film_by_rating(films):
    retained_films = []
    for film in films:
        if film.rating >= 5.0:
            retained_films.append(film)
    return retained_films

# дополнительные функции:
# 1. вывести фильмы дороже указанной суммы
def print_films_more_expensive(films):
    user_price = int(input("Введите минимальную цену: "))
    correct_films = []
    for film in films:
        if film.price > user_price:
            correct_films.append(film)
    return correct_films

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
    print(f"Жанр фильма '{films[user_index].name}' изменен на '{new_genre}'")
    
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
    for film in films:  
        if film.director not in unique_director:
            unique_director.append(film.director)
    
    print("УНИКАЛЬНЫЕ РЕЖИССЕРЫ")
    i += 1
    for director in unique_director:
        print(f"{i}. {director}")


def main_screen():

    print("Выберите дейтвие\n----------------")
    print("1. Поиск фильма")
    print("2. Все фильмы")
    print("3. Средняя длительность")
    print("4. ТОП 3 фильма")
    print("5. Жанры фильмов")
    print("6. Вывести всех режиссеров")
    print("7. Админ")

    what_user_want = input_int("Действие: ", 1, 7)
    
    return what_user_want

def cell_input():

    print("-"*40)
    print("НАЖМИТЕ Enter ДЛЯ ВЫХОДА В ГЛАВНОЕ МЕНЮ")
    input("Enter: ")

films = []

while True:
    what_user_want = main_screen() 

    if what_user_want == 1:
        print("Поиск по году выпуска или по жанру")
        print("1. Диапозон годов ")
        print("2. Жанр ")
        what_user_want = input_int("Действие: ", 1, 2)
        if what_user_want == 1:
            find_film_release(films)
            cell_input()
        if what_user_want == 2:
            find_film_genre(films)
            cell_input()

    if what_user_want == 2:
        print("Вывести фильмы по длительности или рейтингу?")
        print("1. Длительности")
        print("2. Рейтингу")
        what_user_want = input_int("Действие: ", 1, 2)
        if what_user_want == 1:
            sorting_movies_duration(films)
            cell_input()
        if what_user_want == 2:
            sorting_movies_rating(films)
            cell_input()

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



        if what_user_want == 1:
            delete_film_by_rating(films)
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
            print_films_more_expensive(films)
            cell_input()
        
        if what_user_want == 7:
            change_genre_by_id(films)
            cell_input()