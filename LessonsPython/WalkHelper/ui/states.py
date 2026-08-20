from telebot.states import State, StatesGroup


class BotStates(StatesGroup):
    screen2_main_menu = State()
    screen3_walk_planning_step1 = State()
    screen4_walk_planning_step2 = State()
    screen5_walk_planning_step3 = State()