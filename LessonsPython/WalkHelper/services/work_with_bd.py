from repositories.walks_repository import *

def save_current_walk(tg_user_id, city_name, place_name, walk_date):
    insert_walk(tg_user_id, city_name, place_name, walk_date)


def show_all_walks(tg_user_id):
    select_all_walks(tg_user_id)


def show_walk(walk_id: int, tg_user_id: int):
    return select_walk_by_id(
        walk_id=walk_id,
        tg_user_id=tg_user_id
    )


def mark_walk_as_completed(walk_id: int, tg_user_id: int):
    return complete_walk(
        walk_id=walk_id,
        tg_user_id=tg_user_id
    )