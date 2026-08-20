from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen1_start.texts import *
from ui.screen1_start.keyboards import *



def show_screen2_main_menu(chat_id: int, state: StateContext):
    state.delete()
    state.set(BotStates.screen2_main_menu)

    bot.send_message(
        chat_id,
        get_text_for_screen2_main_menu(),
        reply_markup=get_inline_keyboard_for_screen2_main_menu(),
    )


@bot.message_handler(commands=["start"])
def command_handler_screen_1_start(message: types.Message, state: StateContext):
    show_screen2_main_menu(message.chat.id, state)




