# ИД — целое уникальное число
# Название — строка (макс 25 символов)
# Жанр — строка (макс 15 символов)
# Режиссёр — строка (макс 20 символов)
# Год выпуска — целое число
# Длительность (мин) — целое число
# Рейтинг — дробное число
# Цена — целое число
# Количество копий — целое число

import os
from dataclasses import dataclass

@dataclass
class Films: 
    ID: int
    name: str
    genre: str
    director: str
    release: int
    duration: int
    rating: float
    price: int
    copies: int

GLOBAL_ID = 0

def input_new_film():
    print("Введите данные о фильме")
    name = input("Название: ")
    genre = input("Жанр: ")
    director = input("Режиссёр: ")
    release = int(input("Год выпуска: "))
    duration = float(input("Длительность: "))
    rating = int(input("Рейтинг: "))
    price = int(input("Цена: "))
    copies = int(input("Количество копий: "))

    return Films(0, name, genre, director, release, duration, rating, price, copies)

def add_film_to_list(films, film):
    global GLOBAL_ID
    GLOBAL_ID += 1

    film.ID = GLOBAL_ID

    films.append(film)


# 1. поиск фильмов
#   по диапазону годов выпуска
def find_film_release(films):

    print("Введите диапозон годов выпуска фильма, что хотите найти")
    user_find1 = int(input("1ый год: "))
    user_find2 = int(input("2ой год: "))

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



#   по жанру
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



# 2. сортировка фильмов
#   по длительности
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

#   по рейтингу (по убыванию)
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


# 3. подсчитать среднюю длительность фильмов
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


# 4. вывести топ-3 фильма по рейтингу
def top_3_by_raiting(films):
    if len(films) == 0:
        print("Нет фильмов для отображения.")

        return

    os.system('cls')
    print("Топ 3 фильма по рейтингу\n" + "=" * 40)

    sorted_films = sorted(films, key=lambda film: film.rating, reverse=True)
    count = min(3, len(sorted_films))

    print(f"Рейтинг основан на оценке от 0.0 до 10.0\n")

    for i in range(count):
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

    input("\nНажмите Enter для возврата в меню...")



# 5. увеличить цену фильмов, выпущенных до 2000 года
def increase_price_for_old_films(films):

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



# 6. пометить фильмы длительностью более 150 минут как «эпик»
def tag_duration_more_150_minutes(films, film):
    result = []
    for film in films:
        if film.duration > 150:
            result.append(f"{film.name} - эпик")
    return result


# 7. сгруппировать фильмы по жанрам и вывести результат
def group_by_genre(films):
    films_by_genre = {}

    for film in  films:
        current_film_genre = film.genre

        if current_film_genre not in films_by_genre:
            films_by_genre[current_film_genre] = []
        films_by_genre[current_film_genre].append(film)

    return films_by_genre

def print_grouped_films(films):
    grouped = group_by_genre(films)

    for genre, films_list in grouped.items():
        print(f"Жанр: {genre}")
        for film in films_list:
            print(f"Название: {film.name}")



# 8. удалить фильмы с рейтингом ниже 5.0
def delete_film_by_rating(films, film):
    retained_films = []
    for film in films:
        if film.rating >= 5.0:
            retained_films.append(film)
    return retained_films

films = []

add_film_to_list(films, input_new_film())
add_film_to_list(films, input_new_film())
add_film_to_list(films, input_new_film())

# print_grouped_films(films)
