import telebot
from telebot import custom_filters, types
from telebot.states import State, StatesGroup
from telebot.states.sync.context import StateContext
from telebot.states.sync.middleware import StateMiddleware
from telebot.storage import StateMemoryStorage

TOKEN = "YOUR_TOKEN"

state_storage = StateMemoryStorage()

bot = telebot.TeleBot(TOKEN, state_storage=state_storage, use_class_middlewares=True)

schedule_data = {
    "Понедельник": "Математика, Русский, Информатика, История",
    "Вторник": "Литература, Физика, Английский, Биология",
    "Среда": "Алгебра, География, Информатика, Физкультура",
}

homework_data = {
    "Математика": "Решить № 245, 246",
    "Русский": "Выучить правило на стр. 56",
    "Информатика": "Повторить циклы for и while",
}

teachers_data = {
    "Математика": "Иванова Мария Сергеевна",
    "Информатика": "Петров Алексей Николаевич",
    "Русский": "Сидорова Анна Викторовна",
}


class MenuStates(StatesGroup):
    main_menu = State()
    schedule_menu = State()
    homework_menu = State()
    teachers_menu = State()


def show_main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton("Расписание"),
        types.KeyboardButton("Домашка"),
        types.KeyboardButton("Учителя"),
    )

    bot.send_message(chat_id, "Главное меню. Выберите раздел:", reply_markup=markup)


def show_schedule_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton("Понедельник"),
        types.KeyboardButton("Вторник"),
        types.KeyboardButton("Среда"),
    )
    markup.add(types.KeyboardButton("Назад в главное меню"))

    bot.send_message(chat_id, "Меню расписания. Выберите день:", reply_markup=markup)


def show_homework_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton("Математика"),
        types.KeyboardButton("Русский"),
        types.KeyboardButton("Информатика"),
    )
    markup.add(types.KeyboardButton("Назад в главное меню"))

    bot.send_message(chat_id, "Меню домашки. Выберите предмет:", reply_markup=markup)


def show_teachers_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton("Математика"),
        types.KeyboardButton("Информатика"),
        types.KeyboardButton("Русский"),
    )
    markup.add(types.KeyboardButton("Назад в главное меню"))

    bot.send_message(chat_id, "Меню учителей. Выберите предмет:", reply_markup=markup)


@bot.message_handler(commands=["start"])
def start_handler(message: types.Message, state: StateContext):
    state.set(MenuStates.main_menu)
    show_main_menu(message.chat.id)


@bot.message_handler(state=MenuStates.main_menu)
def main_menu_handler(message: types.Message, state: StateContext):
    text = message.text.strip()

    if text == "Расписание":
        state.set(MenuStates.schedule_menu)
        show_schedule_menu(message.chat.id)

    elif text == "Домашка":
        state.set(MenuStates.homework_menu)
        show_homework_menu(message.chat.id)

    elif text == "Учителя":
        state.set(MenuStates.teachers_menu)
        show_teachers_menu(message.chat.id)

    else:
        bot.send_message(message.chat.id, "Выберите кнопку из главного меню.")


@bot.message_handler(state=MenuStates.schedule_menu)
def schedule_menu_handler(message: types.Message, state: StateContext):
    text = message.text.strip()

    if text == "Назад в главное меню":
        state.set(MenuStates.main_menu)
        show_main_menu(message.chat.id)
        return

    if text in schedule_data:
        bot.send_message(
            message.chat.id, f"Расписание на {text}:\n{schedule_data[text]}"
        )
    else:
        bot.send_message(message.chat.id, "Выберите день кнопкой.")


@bot.message_handler(state=MenuStates.homework_menu)
def homework_menu_handler(message: types.Message, state: StateContext):
    text = message.text.strip()

    if text == "Назад в главное меню":
        state.set(MenuStates.main_menu)
        show_main_menu(message.chat.id)
        return

    if text in homework_data:
        bot.send_message(
            message.chat.id,
            f"Домашнее задание по предмету {text}:\n{homework_data[text]}",
        )
    else:
        bot.send_message(message.chat.id, "Выберите предмет кнопкой.")


@bot.message_handler(state=MenuStates.teachers_menu)
def teachers_menu_handler(message: types.Message, state: StateContext):
    text = message.text.strip()

    if text == "Назад в главное меню":
        state.set(MenuStates.main_menu)
        show_main_menu(message.chat.id)
        return

    if text in teachers_data:
        bot.send_message(
            message.chat.id, f"Учитель по предмету {text}:\n{teachers_data[text]}"
        )
    else:
        bot.send_message(message.chat.id, "Выберите предмет кнопкой.")


@bot.message_handler(commands=["cancel"], state="*")
def cancel_handler(message: types.Message, state: StateContext):
    state.delete()

    markup = types.ReplyKeyboardRemove()
    bot.send_message(
        message.chat.id,
        "Состояние очищено. Напишите /start, чтобы открыть меню заново.",
        reply_markup=markup,
    )


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))

bot.infinity_polling()