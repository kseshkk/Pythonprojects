from telebot import types
from telebot.states.sync.context import StateContext

from bot_instance import bot

from datetime import datetime
from ui.states import BotStates

from ui.screen4_walk_planning_step2.texts import *
from ui.screen4_walk_planning_step2.keyboards import *
from ui.screen2_main_menu.handlers import show_screen3_walk_planning_step1
from ui.screen3_walk_planning_step1.handlers import *

from services.places_service import *

def show_screen5_walk_planning_step3(chat_id: int, state: StateContext):
    state.set(BotStates.screen5_walk_planning_step3)

    with state.data() as data:
        city_name = data["city"]

    try:
        places = get_places(city_name)

        bot.send_message(
            chat_id, 
            get_text_for_screen5_walk_planning_step3(places),

            reply_markup=get_inline_keyboard_for_screen5_walk_planning_step3(len(places))
            )

    except:
        bot.send_message(
            chat_id,
            "Ошибка в получении мест\nПопробуйте повторить запрос ещё раз через минуту"
        )

    # except Exception as e:
    #     print("ОШИБКА:", e)
    #     raise

  



@bot.message_handler(state=BotStates.screen4_walk_planning_step2, content_types=["text"])
def message_handler_screen5_walk_planning_step3(message: types.Message, state: StateContext):
    date = message.text.strip()

    try:
        user_date = datetime.strptime(date, "%d.%m.%Y").date()

        if user_date < datetime.today().date():
            bot.send_message(
                message.chat.id,
                "Невозможно запланировать прогулку на прошлое))\n"
                "Введите дату в формате ДД.ММ.ГГГГ:"
            )
            return

        state.add_data(date=date)

        show_screen5_walk_planning_step3(message.chat.id, state)

    except:
        bot.send_message(
            message.chat.id,
            "Некорректная дата.\n"
            "Введите дату в формате ДД.ММ.ГГГГ:"
        )


@bot.callback_query_handler(state=BotStates.screen4_walk_planning_step2)
def callback_handler_screen4_walk_planning_step2(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)

    if call.data == "back":
        show_screen3_walk_planning_step1(call.message.chat.id, state)