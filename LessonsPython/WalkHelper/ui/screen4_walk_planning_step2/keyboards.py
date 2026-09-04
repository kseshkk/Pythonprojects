import telebot


def get_inline_keyboard_for_screen5_walk_planning_step3(count_places: int):
    keyboard = telebot.types.InlineKeyboardMarkup()


    for index in range(0, count_places):
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                f"Выбрать {index+1}",
                callback_data=f"{index}",
            )
        )

    keyboard.add(telebot.types.InlineKeyboardButton("Назад", callback_data="back"))
    return keyboard


