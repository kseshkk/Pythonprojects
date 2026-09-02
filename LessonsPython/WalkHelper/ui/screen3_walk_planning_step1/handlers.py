from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot
from ui.states import BotStates

from api.geonames_api import *
from ui.screen3_walk_planning_step1.texts import *
from ui.screen3_walk_planning_step1.keyboards import *
from ui.screen1_start.handlers import show_screen2_main_menu

def show_screen4_walk_planning_step2(chat_id: int, state: StateContext):
    
    state.set(BotStates.screen4_walk_planning_step2)
    bot.send_message(chat_id, 
                     get_text_for_screen4_walk_planning_step2(),
                     reply_markup=get_inline_keyboard_for_screen4_walk_planning_step2())

@bot.message_handler(state=BotStates.screen3_walk_planning_step1, content_types=["text"])
def message_handler_screen3_walk_planning_step1(message: types.Message, state: StateContext):
    city = message.text.strip()

    if len(city) < 2 or len(city) > 50:
        bot.send_message(message.chat.id, 
                         get_error_text_for_screen3_walk_planning_step1()
                    )
        return

    if city == "":
        bot.send_message(
            message.chat.id,
            get_error_text_for_screen3_walk_planning_step1(),
        )
        return

    try:
        find_city = is_city_exist(city)

        if find_city == False:
            bot.send_message(
                message.chat.id,
                "Ошибка. Такого города в России не существует.\nВведите корректное название города.",
            )
            return
        
        state.add_data(city=city)

        show_screen4_walk_planning_step2(message.chat.id, state)

    except:
        bot.send_message(
            message.chat.id,
            "Ошибка работы с сервером.\nПопробуйте повторить запрос ещё раз через минуту",
        )
        

@bot.callback_query_handler(state=BotStates.screen3_walk_planning_step1)
def callback_handler_screen3_walk_planning_step1(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)

    if call.data == "back":
        show_screen2_main_menu(call.message.chat.id, state)
