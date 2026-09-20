import telebot

def get_inline_keyboard_for_screen3_walk_planning_step1():
    keyboard = telebot.types.InlineKeyboardMarkup()
    
    keyboard.add(telebot.types.InlineKeyboardButton("Назад", callback_data="back"))
    return keyboard


# def get_inline_keyboard_for_screen7_show_planned_walks(user_walks):
#     keyboard = telebot.types.InlineKeyboardMarkup()


#     for index in range(0, 5):
#         keyboard.add(
#             telebot.types.InlineKeyboardButton(
#                 f"Выбрать {index+1}",
#                 callback_data=f"{index}",
#             )
#         )

#     keyboard.row(
#     telebot.types.InlineKeyboardButton(
#         "Назад", callback_data="screen_7_previous_page"
#     ),
#     telebot.types.InlineKeyboardButton(
#         "Вперёд", callback_data="screen_7_next_page"
#     ),
#     )

#     keyboard.add(telebot.types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back"))
#     return keyboard


def get_inline_keyboard_for_screen7_show_planned_walks(
    user_walks
):
    keyboard = telebot.types.InlineKeyboardMarkup()

    for index, walk in enumerate(user_walks):

        keyboard.add(
            telebot.types.InlineKeyboardButton(
                f"Выбрать {index + 1}",
                callback_data=f"walk_{index}"
            )
        )

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            "Вернуться в главное меню",
            callback_data="back"
        )
    )

    return keyboard