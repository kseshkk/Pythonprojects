from telebot import custom_filters
from telebot.states.sync.middleware import StateMiddleware

from bot_instance import bot

import ui.screen1_start.handlers
import ui.screen2_main_menu.handlers
import ui.screen3_walk_planning_step1.handlers
import ui.screen4_walk_planning_step2.handlers
import ui.screen5_walk_planning_step3.handlers
import ui.screen6_walk_planning_step4.handlers
import ui.screen7_show_planned_walks.handlers
import ui.screen8_show_planned_walks.handlers


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))

print("бот запущен")

bot.infinity_polling()