import telebot
import telebot.types
from datetime import datetime

# 7996761407:AAHG5BI3kON2XS7RTbb1vJHi6rtoRpdnCwk

bot = telebot.TeleBot("7996761407:AAHG5BI3kON2XS7RTbb1vJHi6rtoRpdnCwk")

@bot.message_handler(commands=["start"])
def command_start_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, "обработано сообщение старт")


@bot.message_handler(commands=["reply"])
def command_reply_handler(message: telebot.types.Message):
    reply_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    button_add_task = telebot.types.KeyboardButton("Добавить задачу")
    button_show_my_tasks = telebot.types.KeyboardButton("Мои задачи")

    reply_keyboard.add(button_add_task)
    reply_keyboard.add(button_show_my_tasks)

    bot.send_message(message.chat.id, "выбери действие:", reply_markup=reply_keyboard)


@bot.message_handler(func=lambda message: message.text == "Добавить задачу")
def message_bb_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, "обработал кнопку Добавить задачу")


@bot.message_handler(func=lambda message: message.text == "Мои задачи")
def message_aa_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, "обработал кнопку Мои задачи")


@bot.message_handler(commands=["inline"])
def command_start_handler(message: telebot.types.Message):

    bot.send_message(message.chat.id, "обработано сообщение старт")


@bot.message_handler(func=lambda message: message.text.lower() == "пока")
def message_text_poka_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, "я поймал сообщение пока")


@bot.message_handler(func=lambda message: True)
def message_text_all_handler(message: telebot.types.Message):
    input_text = message.text.lower()
    output_text = ""

    if input_text == "привет":
        output_text = "привет!"
    elif input_text == "время":
        output_text = str(datetime.now())
    elif input_text == "как тебя зовут":
        output_text = "Я бот 1"
    else:
        output_text = "неизвестное сообщение"

    bot.send_message(message.chat.id, output_text)


bot.infinity_polling()
# print("бот запущен")
