from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.states import BotStates

from ui.screen3_walk_planning_step1.texts import *
from ui.screen3_walk_planning_step1.keyboards import *

def show_screen4_walk_planning_step2(chat_id: int, state: StateContext):
    state.delete()
    state.set(BotStates.screen4_walk_planning_step2)
    bot.send_message(chat_id, get_text_for_screen4_walk_planning_step2())

@bot.message_handler(state=BotStates.screen3_walk_planning_step1, content_types=["text"])
def message_handler_screen3_walk_planning_step1(message: types.Message, state: StateContext):
    city = message.text.strip()

    if len(city) < 2 or len(city) > 50:
        bot.send_message(message.chat.id, get_error_text_for_screen3_walk_planning_step1())
        return

    state.add_data(city=city)

    show_screen4_walk_planning_step2(message.chat.id, state)




