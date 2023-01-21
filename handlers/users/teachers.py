import aiogram
import asyncpg
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.config import ADMINS
from keyboards.default.tugmalar_k import menu, orqaga1, menu_uqituvchi
from keyboards.tugmalar_i import lokatsiya, surovnoma_user
from loader import dp, db, bot
from states.personalData import LOGIN_USERS, LOGIN_teachers


@dp.callback_query_handler(text='domla')
async def login_domla(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Ismingizni kiriting :</b>\n"
                              "<i>(Lotin harflarda)</i>", reply_markup=orqaga1)

    await LOGIN_teachers.name.set()

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=LOGIN_teachers.name)
async def login_domla1(message: types.Message, state: FSMContext):
    await message.answer("<b>Familyangiz kiriting :</b>\n"
                         "<i>(Lotin harflarda)</i>", reply_markup=orqaga1)
    ism_kes2 = message.text
    await state.update_data(
        {"ism2": ism_kes2}
    )
    await LOGIN_teachers.full.set()

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=LOGIN_teachers.full)
async def login_talaba2(message: types.Message, state: FSMContext):
    await message.answer("<b>Parolni kiriting :</b>\n"
                         "<i>(Lotin harflarda)</i>", reply_markup=orqaga1)
    familya_kes = message.text
    await state.update_data(
        {"familya2": familya_kes}
    )
    await LOGIN_teachers.parol.set()

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=LOGIN_teachers.parol)
async def login_talaba3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("ism2")
    full = data.get("familya2")
    passwww = message.text
    recaptcha4 = await db.select_teacher_two()
    status_login4 = 0
    if passwww.lower() == "smedu2022":
        for inza4 in recaptcha4:
            if str(inza4['familya'].lower()) == str(full.lower()) and str(inza4['ism'].lower()) == str(name.lower()):
                await message.answer(
                    f"🧑‍🎓<b>{full.title()} {name.title()}</b>\nShaxsiy kabinetingizga xush kelibsiz",
                    reply_markup=menu_uqituvchi)
                for login in ADMINS:
                    try:
                        await bot.send_message(chat_id=login,
                                               text=f"🔔,, {full.title()} {name.title()} '' <b>o'qituvchi shaxsiy kabinetiga kirish aniqlandi !</b>\nTashrif buyuruvchi: {message.from_user.get_mention(as_html=True)}")
                        await db.add_panel_teacher(namename3=f"{name.lower()}",
                                                   full_name3=f"{full.lower()}",
                                                   telegram_id3=message.from_user.id)
                    except aiogram.utils.exceptions.ChatNotFound:
                        pass
                    except asyncpg.exceptions.UniqueViolationError:
                        pass

                status_login4 += 1
                break;
            if status_login4 == 1:
                break;
    if status_login4 == 0:
        await message.answer("<b>✖️ Bunday login yoki parol topilmadi</b>❗️", reply_markup=menu)
    await state.finish()


