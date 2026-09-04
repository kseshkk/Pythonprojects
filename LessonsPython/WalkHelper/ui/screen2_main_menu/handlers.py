from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen2_main_menu.texts import *
from ui.screen2_main_menu.keyboards import *
from services.work_with_bd import *

def show_screen3_walk_planning_step1(chat_id: int, state: StateContext):
    state.delete()
    state.set(BotStates.screen3_walk_planning_step1)
    bot.send_message(chat_id, get_text_for_screen3_walk_planning_step1(), reply_markup=get_inline_keyboard_for_screen3_walk_planning_step1())


def show_screen7_show_planned_walks(chat_id: int, state: StateContext):

    try:
        with state.data() as data:
            tg_user_id = data["tg_user_id"]

        user_walks = show_all_walks(tg_user_id)

        state.set(BotStates.screen7_show_planned_walks)

        bot.send_message(
            chat_id,
            get_text_for_screen7_show_planned_walks(user_walks),
            # reply_markup=get_inline_keyboard_for_screen7_show_planned_walks()
        )
    except:
        bot.send_message(
            chat_id,
            "Ошибка работы с базой данных. Не удалось загрузить ваши прогулки. Попробуйте ещё раз позже.",
        )


@bot.callback_query_handler(state=BotStates.screen2_main_menu)
def callback_handler_screen2_main_menu(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)

    if call.data == "plan_walk":
        show_screen3_walk_planning_step1(call.message.chat.id, state)


    elif call.data == "show_planned_walks":
        state.add_data(tg_user_id=call.from_user.id)
        show_screen7_show_planned_walks(call.message.chat.id, state)