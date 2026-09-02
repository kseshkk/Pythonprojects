import telebot


def get_inline_keyboard_for_screen8_show_walk_info():
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton("Пометить завершенной", callback_data="mark_as_completed"))
    keyboard.add(telebot.types.InlineKeyboardButton("Вернуться назад", callback_data="back"))

    return keyboard