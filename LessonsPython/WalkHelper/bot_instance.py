# 8918209640:AAHN52NlydqGdYg0RrK10rH9nxwOo8gcgn4
# @walkhelper_bot

import telebot
from telebot.storage import StateMemoryStorage

BOT_TOKEN = "8918209640:AAHN52NlydqGdYg0RrK10rH9nxwOo8gcgn4"

bot = telebot.TeleBot(
    BOT_TOKEN,
    state_storage=StateMemoryStorage(),
    use_class_middlewares=True,
)