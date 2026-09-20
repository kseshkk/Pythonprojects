from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from ui.states import BotStates

from ui.screen5_walk_planning_step3.texts import *
from ui.screen5_walk_planning_step3.keyboards import *
from ui.screen3_walk_planning_step1.handlers import show_screen4_walk_planning_step2

from services.work_with_bd import *

def show_screen6_walk_planning_step4(chat_id: int, state: StateContext):

    state.set(BotStates.screen6_walk_planning_step4)


    with state.data() as data:
        city_name = data["city"]
        date = data["date"]
        place_name = data["place"]
        

    bot.send_message(chat_id, 
                     get_text_for_screen6_walk_planning_step4(city_name, date, place_name),
                     reply_markup=get_inline_keyboard_for_screen6_walk_planning_step4()
                     )

@bot.callback_query_handler(state=BotStates.screen5_walk_planning_step3)
def callback_screen5_walk_planning_step3(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)


    if call.data == "back":
        show_screen4_walk_planning_step2(call.message.chat.id, state)
        return


    place_index = int(call.data)

    with state.data() as data:
        places = data["places"]
        city_name = data["city"]
        date = data["date"]

    place_name = places[place_index].name


    state.add_data(place=place_name)

    try:
        save_current_walk(call.from_user.id,city_name,place_name,date)

        show_screen6_walk_planning_step4(
            call.message.chat.id,
            state
        )
    
    except Exception as e:
        print(e)
        bot.send_message(
            call.message.chat.id,
            "Ошибка при работе с Базой Данных. "
            "Не удалось сохранить прогулку. "
            "Попробуйте ещё раз позже."
        )


