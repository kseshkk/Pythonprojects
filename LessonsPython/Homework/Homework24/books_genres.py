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
    id: int
    title: str
    author: str
    publication_year: int
    pages_count: int
    rating: float
    is_available: bool
    genre_id: int
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

def print_books(books: list[Book]):
    print("Книги:")

    print(f"{'ID':<5}{'TITLE':<40}{'AUTHORS':<30}{'PUBLICATION YEAR':<20}{'PAGES':<10}{'RATING':<10}{'IS AVAILABLE':<20}{'GENRE ID':<10}")

    for book in books:
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

def print_genres(genres: list[Genre]):
    print("Жанры:")

    print(f"{'ID':<5}{'NAME':<30}{'DESCRIPTION':<30}")

    for genre in genres:
        print(f"{genre.id:<5}"
            f"{genre.name:<30}"
            f"{genre.description:<30}")

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


with get_connection() as conn:
    books_with_genres = get_all_books_with_genres(conn)
    print_books_with_genres(books_with_genres)
    print("\n" + "*" * 50 + "\n")
    # add_new_genre(conn, Genre(name="новое название", description="новое описание"))

    genres = get_all_genres(conn)
    print_genres(genres)