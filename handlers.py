from asyncio import sleep

import pandas as pd
from aiogram.types import Message, ChatActions
from app import bot, dp, db
from keyboard import menu


@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    if not db.subscriber_exists(message.from_user.id):
        db.add_subscriber(message.from_user.id)
    else:
        db.update_subscription(message.from_user.id, True)
    await message.answer("Привет!\nТы попал в 21 hookah market!\nПропиши /menu для того, чтобы открыть меню.",
                         reply_markup=menu)


@dp.message_handler(commands=["menu"])
async def send_menu(message: Message):
    await bot.send_chat_action(message.from_user.id, ChatActions.TYPING)
    await sleep(1)
    await message.answer(text="Основное меню", reply_markup=menu)

"""
@dp.message_handler(commands=['info'])
async def process_info_command(message: Message):
    await message.answer(text="Для того чтобы сделать заказ необходимо, написать мне(боту) сообщение в формате:"
                                   "\n'Номер телефона: 88005553535\nЗаказ: "
                                   "\nMust Have - Pinkman - 125 g - 1\nMust Have - Berry holls - 125 g - 1'"
                                   "\nТабак доступен самовывозом от ст. метро Рыбацкое")


@dp.message_handler(commands=['help'])
async def process_help_command(message: Message):
    msg = 'Я могу ответить на следующие команды:\n/start\n/help\n/info\n/price\n/remains'
    await message.answer(msg)


@dp.message_handler(commands=['price'])
async def process_price_command(message: Message):
    await bot.send_chat_action(message.from_user.id, ChatActions.TYPING)
    await sleep(1)
    await message.answer("Табак - Цена\n"
                         "Alfakher 50 g  -   190Руб.\n"
                         "B3 50 g  -   190Руб.\n"
                         "Black Burn 100 g  -   550Руб.\n"
                         "Black Burn 200 g  -   945Руб.\n"
                         "Black Burn 20 g  -   190Руб.\n"
                         "Bonche 80 g  -   1170Руб.\n"
                         "Burn 100 g  -   475Руб.\n"
                         "Burn 20 g  -   170Руб.\n"
                         "Daily Hookah 250 g  -   900Руб.\n"
                         "Daly Code 20 g  -   160Руб.\n"
                         "Darkside Base ( Soft ) 250 g  -   1450Руб.\n"
                         "Darkside Core ( Medium ) 100 g  -   625Руб.\n"
                         "Darkside Core ( Medium ) 250 g  -   1450Руб.\n"
                         "Darkside Core (Medium) 30 g  -   210Руб.\n"
                         "Do You Tobacco 50 g  -   260Руб.\n"
                         "Duft 100 g  -   680Руб.\n"
                         "Duft All-in 25 g  -   230Руб.\n"
                         "Element 100 g - Earth - 100 g  -   580Руб.\n"
                         "Element 100 g - Water - 100 g  -   570Руб.\n"
                         "Element 200 g - Air - 200 g  -   735Руб.\n"
                         "Element 200 g - Earth - 200 g  -   1155Руб.\n"
                         "Element 200 g - Water - 200 g  -   1155Руб.\n"
                         "Element 40 g - Air - 40 g  -   200Руб.\n"
                         "Element 40 g - Earth - 40 g  -   350Руб.\n"
                         "Element 40 g - Water - 40 g  -   280Руб.\n"
                         "Matt Pear 250 g  -   1565Руб.\n"
                         "Matt Pear 50 g  -   370Руб.\n"
                         "Must Have 125 g  -   680Руб.\n"
                         "NAШ 40 g  -   215Руб.\n"
                         "Satyr 100 g  -   650Руб.\n"
                         "Satyr 25 g  -   210Руб.\n"
                         "Sebero 100 g  -   450Руб.\n"
                         "Sebero 200 g  -   750Руб.\n"
                         "Sebero 20 g  -   140Руб.\n"
                         "Sebero 40 g  -   195Руб.\n"
                         "Sebero LE 75 g  -   550Руб.\n"
                         "Smoke Angels 100 g  -   680Руб.\n"
                         "Spectrum 100 g  -   570Руб.\n"
                         "Spectrum 250 g  -   1390Руб.\n"
                         "Tangiers 100 g  -   1260Руб.\n"
                         "Tangiers 250 g  -   2360Руб.\n"
                         "World Tobacco Original 200 g  -   5145Руб.\n"
                         "World Tobacco Original 20 g  -   580Руб.\n"
                         "X Tobacco  50 g  -   170Руб.\n"
                         "Zomo 50 g  -   230Руб.\n"
                         "Северный 100 g  -   610Руб.\n"
                         "Северный 25  g  -   185Руб.\n"
                         "Chabacco Medium 100 g  -   360Руб.\n"
                         "Chabacco Medium 200 g  -   695Руб.\n"
                         "Chabacco Medium 50 g  -   210Руб.\n"
                         "Chabacco Strong 50 g  -   210Руб.\n"
                         "Dali 250 g  -   735Руб.\n"
                         "Dali 50 g  -   210Руб.\n"
                         "Do You 50 g  -   190Руб.\n"
                         "Eleon  -   190Руб.\n"
                         "Kaleidoscope 50 g  -   195Руб.")


@dp.message_handler(commands=['remains'])
async def send_remains(message: Message):
    from remains import df
    import os
    pd.DataFrame(df).to_excel('./result.xlsx', index=False)
    file = open('./result.xlsx', 'rb')
    await message.answer('Остатки :')
    await bot.send_chat_action(message.from_user.id, ChatActions.UPLOAD_DOCUMENT)
    await sleep(1)
    await bot.send_document(message.from_user.id, file, caption='Этот файл специально для тебя!')
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), './result.xlsx')
    os.remove(path)
"""