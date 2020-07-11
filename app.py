from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

from sqlighter import SQLighter

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

db = SQLighter('db.db')


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp)
