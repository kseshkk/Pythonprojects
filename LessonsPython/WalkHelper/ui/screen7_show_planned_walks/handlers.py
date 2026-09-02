from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen1_start.handlers import show_screen2_main_menu

from ui.screen7_show_planned_walks.texts import *
from ui.screen7_show_planned_walks.keyboards import *

from services.places_service import *

def show_screen8_show_walk_info(chat_id: int, state: StateContext):
    state.set(BotStates.screen8_show_walk_info)

    bot.send_message(
        chat_id, 
        get_text_for_screen8_show_walk_info(),

        reply_markup=get_inline_keyboard_for_screen8_show_walk_info()
        )



@bot.callback_query_handler(state=BotStates.screen7_show_planned_walks)
def callback_screen7_show_planned_walks(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)

    if call.data == "back":
        show_screen2_main_menu(call.message.chat.id, state)