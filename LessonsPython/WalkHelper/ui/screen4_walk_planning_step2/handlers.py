from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen4_walk_planning_step2.texts import *
from ui.screen4_walk_planning_step2.keyboards import *

def show_screen4_walk_planning_step2(chat_id: int, state: StateContext):
    state.delete()
    state.set(BotStates.screen5_walk_planning_step3)
    bot.send_message(chat_id, get_text_for_screen5_walk_planning_step3())


@bot.message_handler(state=BotStates.screen3_walk_planning_step1, content_types=["text"])
def message_handler_screen3_walk_planning_step1(message: types.Message, state: StateContext):
    data = message.text.strip()

    state.add_data(data=data)

    show_screen4_walk_planning_step2(message.chat.id, state)