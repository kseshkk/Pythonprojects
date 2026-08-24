from telebot import custom_filters
from telebot.states.sync.middleware import StateMiddleware

from bot_instance import bot

import ui.screen1_start.handlers
import ui.screen2_main_menu.handlers
import ui.screen3_walk_planning_step1.handlers
import ui.screen4_walk_planning_step2.handlers




bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))

print("бот запущен")

bot.infinity_polling()