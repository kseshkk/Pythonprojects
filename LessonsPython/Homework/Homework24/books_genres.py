import psycopg
from psycopg.rows import dict_row, class_row
from dataclasses import dataclass

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "db_homework2",
    "user": "postgres",
    "password": "12345",
}


@dataclass(slots=True)
class Genre:
    name: str
    description: str
    id: int | None = None

@dataclass(slots=True)
class Book:
    title: str
    author: str
    publication_year: int
    pages_count: int
    rating: float
    is_available: bool
    genre_id: int
    id: int | None = None 

    genre: Genre | None = None

    def is_available_to_str(self):
        return "да" if self.is_available == True else "нет"

def get_connection():
    return psycopg.connect(**DB_CONFIG)

def get_all_books(conn) -> list[Book]:
    with conn.cursor(row_factory=class_row(Book)) as cur:

        cur.execute("""
            SELECT
            id,
            title,
            author,
            publication_year,
            pages_count,
            rating,
            is_available,
            genre_id
            FROM books
            ORDER BY id ASC;
        """)

    return list(cur.fetchall())
      
def get_all_books_with_genres(conn)-> list[Book]:
    books_list = []
    with conn.cursor(row_factory=dict_row) as cur:

        cur.execute("""
            SELECT
            b.id,
            b.title,
            b.author,
            b.publication_year,
            b.pages_count,
            b.rating,
            b.is_available,
            b.genre_id,
                    
            g.id AS g_id,
            g.name,
            g.description
            FROM books AS b
            JOIN genres AS g
            ON b.genre_id = g.id
            ORDER BY b.id ASC;
        """)

        rows = cur.fetchall()

    for row in rows:
        new_genre = Genre(
            id=row["g_id"],
            name=row["name"],
            description=row["description"]
            )

        new_book = Book(
            id=row["id"],
            title=row["title"],
            author=row["author"],
            publication_year=row["publication_year"],
            pages_count=row["pages_count"],
            rating=row["rating"],
            is_available=row["is_available"],
            genre_id=row["genre_id"],
            genre=new_genre
            )

        books_list.append(new_book)

    return books_list

def get_all_genres(conn) -> list[Genre]:
    with conn.cursor(row_factory=class_row(Genre)) as cur:
        cur.execute("""
            SELECT
            id,
            name,
            description
            FROM genres
            ORDER BY id ASC;
        """)
        return list(cur.fetchall())

def get_book_by_id(conn, id: int) -> Book | None:
    with conn.cursor(row_factory=class_row(Book)) as cur:
        cur.execute("""
                    SELECT id, 
                    title, 
                    author, 
                    publication_year, 
                    pages_count, 
                    rating,
                    is_available, 
                    genre_id
                    FROM books
                    WHERE id = %s;
                """,
                (id,),
                )
        
        return cur.fetchone()

def get_genre_by_id(conn, id: int)-> Genre | None:
    with conn.cursor(row_factory=class_row(Genre)) as cur:
        cur.execute("""
                SELECT
                id, 
                name, 
                description
                FROM genres
                WHERE id = %s
""",
(id,),        
                    )
        return cur.fetchone()



def print_books_table_header():
    print("Книги:")

    print(f"{'ID':<5}{'TITLE':<40}{'AUTHORS':<30}{'PUBLICATION YEAR':<20}{'PAGES':<10}{'RATING':<10}{'IS AVAILABLE':<20}{'GENRE ID':<10}")

def print_one_book(book: Book):
        print(
            f"{book.id:<5}"
            f"{book.title:<40}"
            f"{book.author:<30}"
            f"{book.publication_year:<20}"
            f"{book.pages_count:<10}"
            f"{book.rating:<10}"
            f"{book.is_available_to_str():<20}"
            f"{book.genre_id:<10}"
        )

def print_books(books: list[Book]):
    print_books_table_header()

    for book in books:
        print_one_book(book)


def print_books_with_genres(books: list[Book]):
    print("Книги:")

    print(f"{'ID':<5}{'TITLE':<40}{'AUTHORS':<20}{'PUBLICATION YEAR':<20}{'PAGES':<10}{'RATING':<10}{'IS AVAILABLE':<20}{'GENRE NAME':<25}{'DESCRIPTION':<30}")

    for book in books:
        print(
            f"{book.id:<5}"
            f"{book.title:<40}"
            f"{book.author:<20}"
            f"{book.publication_year:<20}"
            f"{book.pages_count:<10}"
            f"{book.rating:<10}"
            f"{book.is_available_to_str():<20}"
            f"{book.genre.name:<25}"
            f"{book.genre.description:<30}"
        )


def print_genres_table_header():
    print(f"{'ID':<5}{'NAME':<30}{'DESCRIPTION':<30}")

def print_one_genre(genre: Genre):
    print(f"{genre.id:<5}"
        f"{genre.name:<30}"
        f"{genre.description:<30}")

def print_genres(genres: list[Genre]):
    print("Жанры:")
    print_genres_table_header()

    for genre in genres:
        print_one_genre(genre)



def add_new_book(conn, book: Book):
    with conn.cursor() as cur:
        cur.execute("""
                    INSERT INTO books 
                    (title, 
                    author, 
                    publication_year, 
                    pages_count, 
                    rating, 
                    is_available, 
                    genre_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                """,
                (book.title,
                 book.author,
                 book.publication_year,
                 book.pages_count,
                 book.rating,
                 book.is_available,
                 book.genre_id,
                ),) 

    conn.commit()   

def update_book_by_id(conn, book: Book) -> bool:
    with conn.cursor() as cur:
        cur.execute("""
                    UPDATE books
                    SET 
                    title = %s, 
                    author = %s, 
                    publication_year = %s, 
                    pages_count = %s, 
                    rating = %s, 
                    is_available = %s, 
                    genre_id = %s
                    WHERE id = %s;
                """,
                (book.title,
                 book.author,
                 book.publication_year,
                 book.pages_count,
                 book.rating,
                 book.is_available,
                 book.genre_id,
                book.id,),) 
        updated_rows = cur.rowcount

    conn.commit()
    return updated_rows != 0
       
def delete_book_by_id(conn, id: int):
    with conn.cursor() as cur:
        cur.execute("""
                    DELETE FROM books
                    WHERE id = %s;
                 """,
                (id,),
                ) 

        deleted_rows = cur.rowcount

    conn.commit()

    return deleted_rows != 0
 


def add_new_genre(conn, genre: Genre):
    with conn.cursor() as cur:
        cur.execute("""
                INSERT INTO genres (name, description)
                VALUES (%s, %s)
                """,
            (
                genre.name,
                genre.description,
            ),
        )
    conn.commit()

def update_genre_by_id(conn, genre: Genre) -> bool:
    with conn.cursor() as cur:
        cur.execute("""
                    UPDATE genres
                    SET name = %s, 
                    description = %s
                    WHERE id = %s;
                """,
                (
                    genre.name,
                    genre.description,
                    genre.id,
                ),
                )
        updated_rows = cur.rowcount

    conn.commit()
    return updated_rows != 0

def delete_genre_by_id(conn, id: int):
    with conn.cursor() as cur:
        cur.execute("""
                    DELETE FROM genres
                    WHERE id = %s;
                """,
                (id,),
                )  

        deleted_rows = cur.rowcount

    conn.commit()

    return deleted_rows != 0



with get_connection() as conn:
    is_run = True


    while is_run == True: 
        try: 
            books_with_genres = get_all_books_with_genres(conn)
            print_books_with_genres(books_with_genres) 
            
            print("\n" + "*" * 50 + "\n") 
            genres = get_all_genres(conn) 
            print_genres(genres)

            print("\n" + "=" * 100 + "\n")

            print("Меню:") 
            print("1. Вывести жанр по id") 
            print("2. Добавить новый жанр") 
            print("3. Удалить жанр по id") 
            print("4. Обновить жанр по id") 
            print("5. Вывести книгу по id") 
            print("6. Добавить новую книгу") 
            print("7. Удалить книгу по id") 
            print("8. Обновить книгу по id") 
            print("0. Выход")

            menu_number = int(input("выберите пункт меню: "))

            if menu_number == 1:
                id = int(input("введите id: "))
                genre = get_genre_by_id(conn, id)
            
                print_genres_table_header()
                if genre == None:
                    print(f"Роль с id {id} не найдена")
                else:
                    print_one_genre(genre)

            elif menu_number == 2: 
                name = input("введите название жанра: ") 
                description = input("введите описание жанра: ") 
            
                add_new_genre( 
                    conn, 
                    Genre(name=name, description=description) 
                ) 
                
                print("успешно добавлено")

            elif menu_number == 3: 
                id = int(input("введите id: "))
                genre = get_genre_by_id(conn, id) 
                
                delete_genre_by_id(conn, id)

            elif menu_number == 4: 
                id = int(input("введите id жанра: ")) 
                name = input("введите новое название жанра: ") 
                description = input("введите новое описание жанра: ") 
                
                is_update = update_genre_by_id( 
                    conn, 
                    Genre(id=id, name=name, description=description) ) 
                
                if is_update == True: 
                    print("успешно обновлено") 
                else: 
                    print(f"жанр c id {id} не найден")
            
            elif menu_number == 5:
                id = int(input("введите id: "))
                book = get_book_by_id(conn, id)
            
                print_books_table_header()
                if book == None:
                    print(f"Роль с id {id} не найдена")
                else:
                    print_one_book(book)
            
            elif menu_number == 6:
                title = input("Название книги: ") 
                author = input("Автор: ") 
                publication_year = int(input("Год публикации: ")) 
                pages_count = int(input("Количество страниц: ")) 
                rating = float(input("Рейтинг: "))
                is_available = bool( input("Есть в наличии? Нажмите Enter если нет, введите любой символ если да: ") ) 
                genre_id = int(input("ID жанра: "))
            
                add_new_book( 
                    conn, 
                    Book(
                        title=title, 
                        author=author, 
                        publication_year=publication_year, 
                        pages_count=pages_count, 
                        rating=rating, 
                        is_available=is_available, 
                        genre_id=genre_id,))                
                print("успешно добавлено")

            elif menu_number == 7:
                id = int(input("введите id: "))
                book = get_book_by_id(conn, id)

                delete_book_by_id(conn, id)

            elif menu_number == 8:
                id = int(input("введите id книги: ")) 
                title = input("Название книги: ") 
                author = input("Автор: ") 
                publication_year = int(input("Год публикации: ")) 
                pages_count = int(input("Количество страниц: ")) 
                rating = float(input("Рейтинг: "))
                is_available = bool( input("Есть в наличии? Нажмите Enter если нет, введите любой символ если да: ") ) 
                genre_id = int(input("ID жанра: "))

                is_update = update_book_by_id( 
                    conn, 
                    Book(id=id, 
                        title=title, 
                        author=author, 
                        publication_year=publication_year, 
                        pages_count=pages_count, 
                        rating=rating, 
                        is_available=is_available, 
                        genre_id=genre_id,) ) 
                
                if is_update == True: 
                    print("успешно обновлено") 
                else: 
                    print(f"книга c id {id} не найдена")

            
            elif menu_number == 0:
                is_run = False
                
            input("\nдля продолжения нажмите <Enter>\n")

        except Exception as e: 
            print( 
                f"Ошибка в работе с программой. " 
                f"Кратко: {str(e)}. Подробно: {repr(e)}" ) 
            
            is_run = False