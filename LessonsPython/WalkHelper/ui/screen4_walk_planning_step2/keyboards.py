import telebot


def get_inline_keyboard_for_screen5_walk_planning_step3():
    keyboard = telebot.types.InlineKeyboardMarkup()
    
    keyboard.add(telebot.types.InlineKeyboardButton("1", callback_data="choose_place"))
    keyboard.add(telebot.types.InlineKeyboardButton("2", callback_data="choose_place"))
    keyboard.add(telebot.types.InlineKeyboardButton("3", callback_data="choose_place"))
    keyboard.add(telebot.types.InlineKeyboardButton("4", callback_data="choose_place"))
    keyboard.add(telebot.types.InlineKeyboardButton("5", callback_data="choose_place"))
    keyboard.add(telebot.types.InlineKeyboardButton("Назад", callback_data="back"))

    return keyboard


