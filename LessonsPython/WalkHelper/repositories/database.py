from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_USER = "postgres"
DATABASE_PASSWORD = "12345"
DATABASE_HOST = "localhost"
DATABASE_PORT = 5432
DATABASE_NAME = "walk_helper_db"

DATABASE_URL = (
    f"postgresql+psycopg://{DATABASE_USER}:{DATABASE_PASSWORD}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)


class Base(DeclarativeBase):
    pass

engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)

get_session = sessionmaker(
    bind=engine,
    expire_on_commit=True,
)