from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen5_walk_planning_step3.texts import *
from ui.screen5_walk_planning_step3.keyboards import *
from ui.screen3_walk_planning_step1.handlers import show_screen4_walk_planning_step2

def show_screen6_walk_planning_step4(chat_id: int, state: StateContext):
    state.delete()
    state.set(BotStates.screen6_walk_planning_step4)
    bot.send_message(chat_id, get_text_for_screen6_walk_planning_step4())

@bot.callback_query_handler(state=BotStates.screen5_walk_planning_step3)
def callback_screen5_walk_planning_step3(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)

    if call.data == "choose_place":
        show_screen6_walk_planning_step4(call.message.chat.id, state)

    if call.data == "back":
        show_screen4_walk_planning_step2(call.message.chat.id, state)