from loader import bot

import handlers  # noqa
from telebot.custom_filters import StateFilter
from utils.set_bot_commands import set_default_commands
from database.common.models import db, User, Currency, History

if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    db.create_tables([User, Currency, History])
    set_default_commands(bot)
    bot.infinity_polling()
