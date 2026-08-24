from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen4_walk_planning_step2.texts import *
from ui.screen4_walk_planning_step2.keyboards import *

def show_screen5_walk_planning_step3(chat_id: int, state: StateContext):
    state.delete()
    state.set(BotStates.screen5_walk_planning_step3)
    bot.send_message(chat_id, get_text_for_screen5_walk_planning_step3(), reply_markup=get_inline_keyboard_for_screen5_walk_planning_step3())


@bot.message_handler(state=BotStates.screen4_walk_planning_step2, content_types=["text"])
def message_handler_screen5_walk_planning_step3(message: types.Message, state: StateContext):
    data = message.text.strip()

    state.add_data(data=data)

    show_screen5_walk_planning_step3(message.chat.id, state)