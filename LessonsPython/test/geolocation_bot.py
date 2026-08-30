# jdhfsfshs_bot
# 8591849971:AAFDoerHgWwgBDQlwu34JgN0lvasHTsoZ1Y

import telebot
from telebot import types

# Замените 'YOUR_BOT_TOKEN' на реальный токен
BOT_TOKEN = "8591849971:AAFDoerHgWwgBDQlwu34JgN0lvasHTsoZ1Y"
bot = telebot.TeleBot(BOT_TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаём клавиатуру с кнопкой для отправки локации
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # request_location=True делает кнопку "умной" — при нажатии Telegram
    # запросит у пользователя разрешение на отправку его геопозиции
    btn_location = types.KeyboardButton('📍 Отправить мою геопозицию', request_location=True)
    markup.add(btn_location)

    bot.reply_to(message, "Привет! Нажми на кнопку, чтобы поделиться своим местоположением.", reply_markup=markup)

# Обработчик сообщений с геолокацией
@bot.message_handler(content_types=['location'])
def handle_location(message):
    # Получаем объект с локацией из сообщения
    user_location = message.location

    if user_location:
        lat = user_location.latitude
        lon = user_location.longitude

        # Бот отвечает координатами
        bot.reply_to(message, f"📍 Получена геопозиция!\nШирота: {lat}\nДолгота: {lon}")
    else:
        bot.reply_to(message, "Не удалось распознать геопозицию.")

# Запускаем бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.infinity_polling()