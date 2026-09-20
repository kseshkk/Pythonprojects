from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen1_start.handlers import show_screen2_main_menu

from ui.screen7_show_planned_walks.handlers import *
from services.work_with_bd import show_walk, mark_walk_as_completed



@bot.callback_query_handler(state=BotStates.screen8_show_walk_info)
def callback_screen8_show_walk_info(call: types.CallbackQuery,state: StateContext):

    bot.answer_callback_query(call.id)

    if call.data == "back":

        show_screen7_show_planned_walks(call.message.chat.id,state)
        return


    if call.data == "mark_as_completed":
        with state.data() as data:

            walk_id = data.get("selected_walk_id")

            tg_user_id = data.get("tg_user_id")

      
        if (walk_id is None or tg_user_id is None):
            show_screen2_main_menu(call.message.chat.id,state)
            return

        try:

            completed = mark_walk_as_completed(walk_id,tg_user_id)

            if not completed:
                bot.send_message(call.message.chat.id,"Прогулка уже завершена")
                show_screen2_main_menu(call.message.chat.id,state)

                return

            show_screen8_show_walk_info(call.message.chat.id,state)

        except Exception as e:

            print(
                "Ошибка при изменении статуса:",
                e
            )

            bot.send_message(
                call.message.chat.id,
                "Ошибка работы с базой данных. "
                "Не удалось изменить статус прогулки."
            )