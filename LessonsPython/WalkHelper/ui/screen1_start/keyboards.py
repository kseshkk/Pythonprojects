import telebot


def get_inline_keyboard_for_screen2_main_menu():
    keyboard = telebot.types.InlineKeyboardMarkup()
    
    keyboard.add(telebot.types.InlineKeyboardButton("Запланировать прогулку", callback_data="plan_walk"))
    keyboard.add(telebot.types.InlineKeyboardButton("Посмотреть запланированные прогулки", callback_data="show_planned_walks"))

    return keyboard