from modulos.Bot_instance import create_bot
from modulos.Bot_handle import setup

bot = create_bot()
setup(bot)

bot.infinity_polling() 