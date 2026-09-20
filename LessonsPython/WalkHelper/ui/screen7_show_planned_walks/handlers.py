from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen1_start.handlers import show_screen2_main_menu

from ui.screen7_show_planned_walks.texts import *
from ui.screen7_show_planned_walks.keyboards import *
from ui.screen2_main_menu.texts import *
from ui.screen2_main_menu.keyboards import *
from services.work_with_bd import *


from services.places_service import *

def show_screen7_show_planned_walks(chat_id: int, state: StateContext):

    try:
        with state.data() as data:
            tg_user_id = data["tg_user_id"]


        user_walks = show_all_walks(tg_user_id)
        state.add_data(walks=user_walks)

        state.set(BotStates.screen7_show_planned_walks)

        bot.send_message(
            chat_id,
            get_text_for_screen7_show_planned_walks(user_walks),
            reply_markup=get_inline_keyboard_for_screen7_show_planned_walks(user_walks)
        )
    except Exception as e: 
        print(e)
        bot.send_message(
            chat_id,
            "Ошибка работы с базой данных. Не удалось загрузить ваши прогулки. Попробуйте ещё раз позже.",
        )





def show_screen8_show_walk_info(chat_id: int, state: StateContext):
    state.set(BotStates.screen8_show_walk_info)

    with state.data() as data:
        walk_id = data.get("selected_walk_id")
        tg_user_id = data.get("tg_user_id")

    try:
        walk = show_walk(walk_id,tg_user_id)
    
        if walk is None:
            bot.send_message(
                chat_id,
                "Прогулка не найдена."
            )

            show_screen7_show_planned_walks(chat_id, state)

            return

        bot.send_message(
            chat_id, 
            get_text_for_screen8_show_walk_info(walk),
            reply_markup=get_inline_keyboard_for_screen8_show_walk_info()
            )
        
    except Exception as e:
        print(e)

        bot.send_message(
            chat_id,
            "Ошибка работы с базой данных. "
            "Попробуйте ещё раз позже."
        )




@bot.callback_query_handler(state=BotStates.screen7_show_planned_walks)
def callback_screen7_show_planned_walks(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)

    if call.data == "back":
        show_screen2_main_menu(call.message.chat.id, state)
        return

    try:
        index = int(call.data.split("_",1)[1])

        with state.data() as data:
            walks = data.get("walks",[])

        # if (index < 0 or index >= len(walks)):

        #     bot.send_message(
        #         call.message.chat.id,
        #         "Прогулка не найдена.")

            return

        selected_walk = walks[index]

        state.add_data(selected_walk_id=selected_walk.id)

        show_screen8_show_walk_info(call.message.chat.id,state)

    except Exception as e:

            bot.send_message(
                call.message.chat.id,
                "Не удалось открыть прогулку. "
                "Попробуйте ещё раз."
            )