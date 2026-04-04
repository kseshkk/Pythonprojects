# 8254160311:AAH4gTwgtXH_MY5Gm4l9FDLC1vivkZdM3q4

import telebot
import telebot.types

bot = telebot.TeleBot("8254160311:AAH4gTwgtXH_MY5Gm4l9FDLC1vivkZdM3q4")

@bot.message_handler(commands=["start"])
def command_start_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id,
                    "Привет! Это бот 'настроение дня'"
                    "\nИспользуй команду /mood, чтобы выбрать настроение"
                    "\nМожешь получить совет с помощью команды /advice")


@bot.message_handler(commands=["advice"])
def command_advice_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Что бы не случилось, в скором времени все обязательно наладится! В крайнем случае можешь послушать музыку :)")


@bot.message_handler(commands=["mood"])
def command_mood_handler(message: telebot.types.Message):
    reply_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    button_happy = telebot.types.KeyboardButton("Веселое")
    button_normal = telebot.types.KeyboardButton("Нормальное")
    button_sad = telebot.types.KeyboardButton("Грустное")


    reply_keyboard.add(button_happy)
    reply_keyboard.add(button_normal)
    reply_keyboard.add(button_sad)


    bot.send_message(message.chat.id, "Какое у тебя сегодня настроение?", reply_markup=reply_keyboard)


@bot.message_handler(func=lambda message: True)
def message_text_all_handler(message: telebot.types.Message):
    input_text = message.text.lower()
    output_text = ""

    if input_text == "веселое":
        output_text = "Отлично! Значит будет хороший день :)"
    elif input_text == "нормальное":
        output_text = "Нормально - это тоже хорошо!"
    elif input_text == "грустное":
        output_text = "Не расстраивайся!\nМожешь попросить совет с помощью команды /advice"
    else:
        output_text = "Неизвестное сообщение. Попробуй ввести что-то другое или воспользуйся подсказками в меню"

    bot.send_message(message.chat.id, output_text)





bot.infinity_polling()