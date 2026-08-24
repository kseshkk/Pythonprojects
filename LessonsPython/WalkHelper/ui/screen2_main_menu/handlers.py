from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen2_main_menu.texts import *
from ui.screen2_main_menu.keyboards import *

def show_screen3_walk_planning_step1(chat_id: int, state: StateContext):
    state.delete()
    state.set(BotStates.screen3_walk_planning_step1)
    bot.send_message(chat_id, get_text_for_screen3_walk_planning_step1())


@bot.callback_query_handler(state=BotStates.screen2_main_menu)
def callback_handler_screen3_walk_planning_step1(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)

    if call.data == "plan_walk":
        show_screen3_walk_planning_step1(call.message.chat.id, state)


    elif call.data == "show_planned_walks":
        output_text = get_text_for_screen7_show_planned_walks()

        bot.send_message(call.message.chat.id, output_text)