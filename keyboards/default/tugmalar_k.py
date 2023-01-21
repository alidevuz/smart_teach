from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📚Kurslar'),
        ],
        [
            KeyboardButton(text='📝Kursga yozilish'),
            KeyboardButton(text='👤Shaxsiy kabinet'),

        ],
        [
            KeyboardButton(text='📍 Manzillar'),
            KeyboardButton(text='📞 Aloqa'),

        ],
    ],
    resize_keyboard=True
)

orqaga1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️Orqaga'),
        ],
    ],
    resize_keyboard=True
)

orqaga2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='⬅️Ortaga'),
        ],
    ],
    resize_keyboard=True
)
menu_uquvchi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📃Davomat'),
            KeyboardButton(text='📕Uyga vazifa'),

        ],
        [
            KeyboardButton(text='💳 To\'lov jadvali'),

        ],
        [
            KeyboardButton(text='📝Kursga yozilish'),
            KeyboardButton(text='📚Kurslar'),

        ],
        [
            KeyboardButton(text='📍 Manzillar'),
            KeyboardButton(text='📞 Aloqa'),

        ],
    ],
    resize_keyboard=True
)

menu_uqituvchi = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🧮Davomat'),
            KeyboardButton(text='📕Uyga vazifa berish'),

        ],
        [
            KeyboardButton(text='💳 To\'lov jadvalari'),
            KeyboardButton(text='🔍O\'quvchilar ro\'yxati'),

        ],
        [
            KeyboardButton(text='⚙️O\'quvchi qo\'shish va olib tashlash'),

        ],
        [
            KeyboardButton(text='💸Ish haqi kalkulator'),

        ],
        [
            KeyboardButton(text='📍 Manzillar'),
            KeyboardButton(text='📞 Aloqa'),

        ],
    ],
    resize_keyboard=True
)