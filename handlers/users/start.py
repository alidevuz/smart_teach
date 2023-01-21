import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import IsPrivate
from keyboards.default.tugmalar_k import menu
from loader import dp, db

# @dp.my_chat_member_handler(IsPrivate())
# async def close_memeber(message: types.ChatMemberUpdated):
#     noview_coomamands = message['new_chat_member']
#     com_view = str(noview_coomamands['status'])
#     kised_users_id = message['from']
#     kised_users_id_open = kised_users_id['id']
#     if com_view == str('kicked'):
#         await db.delete_users(telegram_id=kised_users_id_open)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    tek16 = await db.select_panel_one(telegram_id=message.from_user.id)
    tek2 = await db.select_panel_teacher(telegram_id3=message.from_user.id)
    if tek16 != None or tek2 != None:
        await message.answer(f"<b>Assalomu alykum !</b> {message.from_user.get_mention(as_html=True)}\n"
                             f"<b><u>Smart Teach</u></b> <i>o'quv markazi \nrasmiy botiga xush kelibsiz </i>👨‍🏫",
                             reply_markup=menu)
        await db.delete_panel_teacher(telegram_id3=message.from_user.id)
        await db.delete_panel_users(telegram_id=message.from_user.id)
        try:
            await db.add_user(full_name=message.from_user.full_name,
                              telegram_id=message.from_user.id, )
        except asyncpg.exceptions.UniqueViolationError:
            print("DATABASE bazada bu foydalanuvchi bor edi")
        except AttributeError:
            pass
    else:
        await message.answer(f"<b>Assalomu alykum !</b> {message.from_user.get_mention(as_html=True)}\n"
                             f"<b><u>Smart Teach</u></b> <i>o'quv markazi \nrasmiy botiga xush kelibsiz </i>👨‍🏫",
                             reply_markup=menu)
        try:
            await db.add_user(full_name=message.from_user.full_name,
                              telegram_id=message.from_user.id, )
        except asyncpg.exceptions.UniqueViolationError:
            print("DATABASE bazada bu foydalanuvchi bor edi")
        except AttributeError:
            pass


