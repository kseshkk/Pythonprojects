from models.walk import *


def get_text_for_screen3_walk_planning_step1():
    return "Планируем прогулку\n\n 1. Введите город"



def get_text_for_screen7_show_planned_walks(user_walks):

    if user_walks == None:
        return "Ни одной прогулки не запланировано"

    # output_text = "Посмотреть полную информацию о прогулке:\n\n"


    # for current_walk in user_walks:
    #     output_text += (
    #         f"{current_walk.walk_date_to_str()} - {current_walk.get_status()}\n\n"
    #     )

    # return output_text

    text = "Ваши запланированные прогулки:\n\n"

    for index, walk in enumerate(
        user_walks,
        start=1
    ):
        text += (
            f"{index}. "
            f"{walk.walk_date_to_str()}"
            f"({walk.get_status()})\n"
        )

    text += (
        "\n"
        "Выберите номер прогулки, "
        "чтобы посмотреть полную информацию."
    )

    return text