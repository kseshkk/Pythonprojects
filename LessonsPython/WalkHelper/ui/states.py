from telebot.states import State, StatesGroup

class BotStates(StatesGroup):
    screen2_main_menu = State()
    screen3_walk_planning_step1 = State()
    screen4_walk_planning_step2 = State()
    screen5_walk_planning_step3 = State()
    screen6_walk_planning_step4 = State()
    screen7_show_planned_walks = State()
    screen8_show_planned_walks = State()