from aiogram.utils import executor
import buttons
from config import bot, dp, admin
from db import db_main
from handlers import (start, commands, quiz, game,
                      FSM_store, FSM_reg, webapp,
                      admin_group, send_products, send_delete_product,
                      echo)

start.register_start(dp=dp)
commands.register_commands(dp=dp)
quiz.register_quiz(dp=dp)
game.register_game(dp=dp)
FSM_store.register_store(dp=dp)
FSM_reg.register_fsm_reg(dp=dp)
webapp.register_handlers_webapp(dp=dp)
send_products.register_send_products_handler(dp=dp)
send_delete_product.register_send_delete_product(dp=dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
