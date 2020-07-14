from asyncio import sleep

import pandas as pd
from aiogram.types import CallbackQuery, ChatActions

from app import dp, bot
from keyboard import menu


@dp.callback_query_handler(text="info")
async def process_info_command(call: CallbackQuery):
    await bot.send_chat_action(call.from_user.id, ChatActions.TYPING)
    await sleep(1)
    await call.message.answer(text="Пропиши /menu для того, чтобы открыть меню."
                                   "\nПо всем вопросам обращаться в:\nhttps://vk.com/write34076014",
                              reply_markup=menu)


@dp.callback_query_handler(text="help")
async def process_help_command(call: CallbackQuery):
    await bot.send_chat_action(call.from_user.id, ChatActions.TYPING)
    await sleep(1)
    await call.message.answer(text="Для того чтобы сделать заказ необходимо, написать мне(боту) сообщение в формате:"
                                   "\n'Номер телефона: 88005553535\nЗаказ: "
                                   "\nMust Have - Pinkman - 125 g - 1\nMust Have - Berry holls - 125 g - 1'"
                                   "\nТабак доступен самовывозом от ст. метро Рыбацкое",
                              reply_markup=menu)


@dp.callback_query_handler(text="price")
async def process_price_command(call: CallbackQuery):
    await bot.send_chat_action(call.from_user.id, ChatActions.TYPING)
    await sleep(1)
    await call.message.answer("Табак - Цена\n"
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
                              "Kaleidoscope 50 g  -   195Руб.",
                              reply_markup=menu)


@dp.callback_query_handler(text='remains')
async def send_remains(call: CallbackQuery):
    await bot.send_chat_action(call.from_user.id, ChatActions.UPLOAD_DOCUMENT)
    from remains import df
    import os
    pd.DataFrame(df).to_excel('./result.xlsx', index=False)
    file = open('./result.xlsx', 'rb')
    await call.message.answer('Остатки :')
    await bot.send_chat_action(call.from_user.id, ChatActions.UPLOAD_DOCUMENT)
    await sleep(1)
    await bot.send_document(call.from_user.id, file, caption='Этот файл специально для тебя!',
                            reply_markup=menu)
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), './result.xlsx')
    os.remove(path)


@dp.callback_query_handler(text="cancel")
async def cancel_command(call: CallbackQuery):
    await call.answer("Для того, что бы заново открыть меню, пропиши /menu", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
