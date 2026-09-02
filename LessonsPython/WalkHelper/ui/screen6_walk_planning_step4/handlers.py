from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen1_start.handlers import show_screen2_main_menu


@bot.callback_query_handler(state=BotStates.screen6_walk_planning_step4)
def callback_screen6_walk_planning_step4(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)

    if call.data == "to_main_menu":
        show_screen2_main_menu(call.message.chat.id, state)
        