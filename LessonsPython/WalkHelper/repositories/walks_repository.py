from sqlalchemy import select

from models.walk import Walk
from repositories.database import get_session


def insert_walk(tg_user_id: int, city_name: str, place_name, walk_date):

    with get_session() as session:
        walk = Walk(
            tg_user_id=tg_user_id,
            city_name=city_name,
            place_name = place_name,
            walk_date=walk_date,
            status=True,
        )
        session.add(walk)
        session.commit()

        return walk


def select_all_walks(tg_user_id: int) -> list[Walk]:
    with get_session() as session:
        query = (
            select(Walk)
            .where(Walk.tg_user_id == tg_user_id)
            .order_by(Walk.walk_date.desc())
        )
        return list(session.scalars(query))

def select_walk_by_id(walk_id: int, tg_user_id: int) -> Walk | None:

    with get_session() as session:

        query = (
            select(Walk)
            .where(
                Walk.id == walk_id,
                Walk.tg_user_id == tg_user_id
            )
        )

        return session.scalar(query)

def complete_walk(walk_id: int, tg_user_id: int) -> bool:

    with get_session() as session:

        query = (
            select(Walk)
            .where(
                Walk.id == walk_id,
                Walk.tg_user_id == tg_user_id
            )
        )

        walk = session.scalar(query)

        if walk is None:
            return False

        if walk.status == "завершено":
            return False

        # walk.status = "завершено"

        session.commit()

        return True