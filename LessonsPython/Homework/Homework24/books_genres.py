from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    Float,
    Boolean,
    create_engine,
    select,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    joinedload,
    mapped_column,
    relationship,
    sessionmaker,
)
DATABASE_URL = "postgresql+psycopg://postgres:12345@localhost:5432/db_homework2"


class Base(DeclarativeBase):
    pass

class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String(500), nullable=False)


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    publication_year: Mapped[int] = mapped_column(Integer, nullable=False)
    pages_count: Mapped[int] = mapped_column(Integer, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)
    genre_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("genres.id", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=False,
    )

    genre: Mapped[Genre] = relationship()

    def is_available_to_str(self):
        return "да" if self.is_available == True else "нет"

engine = create_engine(DATABASE_URL, echo=False)

get_session_local = sessionmaker(
    bind=engine,
    expire_on_commit=True,
)

def get_all_books(session: Session) -> list[Book]:
    query = (select(Book).order_by(Book.id))

    return list(session.scalars(query).all())
      
def get_all_books_with_genres(session: Session)-> list[Book]:
    query = (
        select(Book).options(joinedload(Book.genre)).order_by(Book.id)
    )

    return list(session.scalars(query).all())

def get_all_genres(session: Session) -> list[Genre]:
    query = (select(Genre).order_by(Genre.id))

    return list(session.scalars(query).all())

def get_book_by_id(session: Session, id: int) -> Book | None:
    return session.get(Book, id)

def get_genre_by_id(session: Session, id: int)-> Genre | None:
    return session.get(Genre, id)


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



def add_new_book(session: Session, book: Book):
    session.add(book)
    session.commit()


def update_book_by_id(session: Session, update_book: Book) -> bool:
    find_book = get_book_by_id(session, update_book.id)

    if find_book == None:
        return False
    
    find_book.title = update_book.title
    find_book.author = update_book.author
    find_book.publication_year = update_book.publication_year
    find_book.pages_count = update_book.pages_count
    find_book.rating = update_book.rating
    find_book.is_available = update_book.is_available
    find_book.genre_id = update_book.genre_id
    
    session.commit()

    return True
       
def delete_book_by_id(session: Session, id: int) -> bool:
    find_book = get_book_by_id(session, id)

    if find_book == None:
        return False

    session.delete(find_book)
    session.commit()

    return True
 


def add_new_genre(session: Session, genre: Genre):
    session.add(genre)
    session.commit()


def update_genre_by_id(session: Session, update_genre: Genre) -> bool:
    find_genre = get_genre_by_id(session, update_genre.id)

    if find_genre == None:
        return False

    find_genre.name = update_genre.name
    find_genre.description = update_genre.description

    session.commit()

    return True

def delete_genre_by_id(session: Session, id: int) -> bool:
    find_genre = get_genre_by_id(session, id)

    if find_genre == None:
        return False

    session.delete(find_genre)
    session.commit()

    return True



with get_session_local() as session:
    is_run = True


    while is_run == True: 
        try: 
            books_with_genres = get_all_books_with_genres(session)
            print_books_with_genres(books_with_genres) 
            
            print("\n" + "*" * 50 + "\n") 
            genres = get_all_genres(session) 
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
                genre = get_genre_by_id(session, id)
            
                print_genres_table_header()
                if genre == None:
                    print(f"Жанр с id {id} не найден")
                else:
                    print_one_genre(genre)

            elif menu_number == 2: 
                name = input("введите название жанра: ") 
                description = input("введите описание жанра: ") 
            
                add_new_genre( 
                    session, 
                    Genre(name=name, description=description) 
                ) 
                
                print("успешно добавлено")

            elif menu_number == 3: 
                id = int(input("введите id: "))
                is_deleted = delete_genre_by_id(session, id)

                if is_deleted == True:
                    print("успешно удалено")
                else:
                    print(f"жанр с id {id} не найден")

            elif menu_number == 4: 
                id = int(input("введите id жанра: ")) 
                name = input("введите новое название жанра: ") 
                description = input("введите новое описание жанра: ") 
                
                is_update = update_genre_by_id( 
                    session, 
                    Genre(id=id, name=name, description=description) ) 
                
                if is_update == True: 
                    print("успешно обновлено") 
                else: 
                    print(f"жанр c id {id} не найден")
            
            elif menu_number == 5:
                id = int(input("введите id: "))
                book = get_book_by_id(session, id)
            
                print_books_table_header()
                if book == None:
                    print(f"книга с id {id} не найдена")
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
                    session, 
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
                is_deleted = delete_book_by_id(session, id)

                if is_deleted == True:
                    print("успешно удалено")
                else:
                    print(f"книга с id {id} не найдена")

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
                    session, 
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