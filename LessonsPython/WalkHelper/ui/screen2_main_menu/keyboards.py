import telebot

def get_inline_keyboard_for_screen3_walk_planning_step1():
    keyboard = telebot.types.InlineKeyboardMarkup()
    
    keyboard.add(telebot.types.InlineKeyboardButton("Назад", callback_data="back"))
    return keyboard