from repositories.walks_repository import *

def save_current_walk(tg_user_id, city_name, place_name, walk_date):
    insert_walk(tg_user_id, city_name, place_name, walk_date)


def show_all_walks(tg_user_id):
    select_all_walks(tg_user_id)