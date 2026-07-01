import psycopg
from psycopg.rows import dict_row

from dataclasses import dataclass

DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "dbname": "db_homework2",
    "user": "postgres",
    "password": "12345",
}

@dataclass
class Book:
    id: int
    title: str
    author: str
    publication_year: int
    pages_count: int
    rating: float
    is_available: bool
    genre_id: int

@dataclass
class BookWithGenre:
    id: int
    title: str
    author: str
    publication_year: int
    pages_count: int
    rating: float
    is_available: bool
    genre_name: str

def get_connection():
    return psycopg.connect(**DB_CONFIG)

def get_books(conn) -> list[Book]:
    books_list = []
    books_from_db = None

    with conn.cursor(row_factory=dict_row) as cur:

        cur.execute("SELECT * FROM books ORDER BY id ASC")

        books_from_db = cur.fetchall()

    for book in books_from_db:
        new_book = Book(
            id=book["id"],
            title=book["title"],
            author=book["author"],
            publication_year=book["publication_year"],
            pages_count=book["pages_count"],
            rating=book["rating"],
            is_available=book["is_available"],
            genre_id=book["genre_id"]
        )

        books_list.append(new_book)

    return books_list

def get_book_with_genre(conn)-> list[BookWithGenre]:
    books_list = []
    books_from_db = None

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
    g.name AS genre_name
    FROM books AS b
    JOIN genres AS g
    ON b.genre_id = g.id
    ORDER BY b.id ASC
""")

        books_from_db = cur.fetchall()

    for book in books_from_db:
        new_book = BookWithGenre(
            id=book["id"],
            title=book["title"],
            author=book["author"],
            publication_year=book["publication_year"],
            pages_count=book["pages_count"],
            rating=book["rating"],
            is_available=book["is_available"],
            genre_name=book["genre_name"]
        )

        books_list.append(new_book)

    return books_list




def print_books(books: list[Book]):
    print("Книги:")

    print(f"{'ID':<5}{'TITLE':<40}{'AUTHORS':<30}{'PUBLICATION YEAR':<20}{'PAGES':<10}{'RATING':<10}{'IS AVAILABLE':<20}{'GENRE ID':<10}")

    for book in books:
        if book.is_available == True:
           available = "да" 
        else:
            available = "нет"

        print(
            f"{book.id:<5}"
            f"{book.title:<40}"
            f"{book.author:<30}"
            f"{book.publication_year:<20}"
            f"{book.pages_count:<10}"
            f"{book.rating:<10}"
            f"{available:<20}"
            f"{book.genre_id:<10}"
        )

def print_books_with_genre(books: list[BookWithGenre]):
    print("Книги:")

    print(f"{'ID':<5}{'TITLE':<40}{'AUTHORS':<30}{'PUBLICATION YEAR':<20}{'PAGES':<10}{'RATING':<10}{'IS AVAILABLE':<20}{'GENRE NAME':<20}")

    for book in books:
        if book.is_available == True:
           available = "да" 
        else:
            available = "нет"

        print(
            f"{book.id:<5}"
            f"{book.title:<40}"
            f"{book.author:<30}"
            f"{book.publication_year:<20}"
            f"{book.pages_count:<10}"
            f"{book.rating:<10}"
            f"{available:<20}"
            f"{book.genre_name:<20}"
        )


conn = get_connection()


books = get_books(conn)
books_with_genre = get_book_with_genre(conn)
# print_books(books)

print_books_with_genre(books_with_genre)

conn.close()