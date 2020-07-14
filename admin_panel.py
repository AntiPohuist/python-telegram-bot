from asyncio import sleep

from aiogram.types import Message

from config import admin_id, admin_id_2
from app import dp, bot, db


@dp.message_handler(user_id=admin_id, commands=['get_users'])
async def get_users(message: Message):
    await message.answer(db.get_user())


@dp.message_handler(user_id=admin_id)
async def enter_text(message: Message):
    text = message.text
    if text.startswith("рассылка "):
        text = text.replace("рассылка ", "")
        users = db.get_user()
        await sleep(0.3)

        for user in users:
            try:
                await bot.send_message(chat_id=user[0], text=text)
                await sleep(0.3)
            except Exception:
                pass
        await message.answer("Рассылка выполнена!")


@dp.message_handler()
async def send_to_admin(message: Message):
    text = f'Тебе написал: {message.from_user.first_name} {message.from_user.last_name},{message.from_user.username} ' \
           f'{message.text}'
    await bot.send_message(chat_id=admin_id, text=text)
#    await bot.send_message(chat_id=admin_id_2, text=text)
