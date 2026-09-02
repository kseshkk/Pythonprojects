import telebot


def get_inline_keyboard_for_screen6_walk_planning_step4():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton("Вернуться в главное меню", callback_data="to_main_menu"))

    return keyboard