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


def select_all_walks(tg_user_id: int) -> list[Walk]:
    with get_session() as session:
        query = (
            select(Walk)
            .where(Walk.tg_user_id == tg_user_id)
            .order_by(Walk.walk_date.desc())
        )
        return list(session.scalars(query))