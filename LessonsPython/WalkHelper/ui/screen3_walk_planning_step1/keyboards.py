import telebot

def get_inline_keyboard_for_screen4_walk_planning_step2():
    keyboard = telebot.types.InlineKeyboardMarkup()
    
    keyboard.add(telebot.types.InlineKeyboardButton("Назад", callback_data="back"))
    return keyboard