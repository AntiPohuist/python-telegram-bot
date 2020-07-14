from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Информация", callback_data="info"),
            InlineKeyboardButton(text="Как делать заказ", callback_data="help"),
        ],
        [
            InlineKeyboardButton(text="Цены", callback_data="price"),
            InlineKeyboardButton(text="Остатки", callback_data="remains"),
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ]
)

