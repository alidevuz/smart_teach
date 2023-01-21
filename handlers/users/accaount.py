import aiogram
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.config import ADMINS
from keyboards.default.tugmalar_k import menu, orqaga1, menu_uquvchi
from keyboards.tugmalar_i import lokatsiya, surovnoma_user
from loader import dp, db, bot
from states.personalData import LOGIN_USERS


@dp.message_handler(text='👤Shaxsiy kabinet')
async def shaxsiy_kabinet(message: types.Message):
    ortiqchasi = await message.answer("...", reply_markup=orqaga1)
    await message.answer("<b>Siz o'quvchimisiz yoki o'qituvchi ?</b>", reply_markup=surovnoma_user)
    await ortiqchasi.delete()

@dp.callback_query_handler(text='talaba')
async def login_talaba(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Ismingizni kiriting :</b>\n"
                              "<i>(Lotin harflarda)</i>", reply_markup=orqaga1)

    await LOGIN_USERS.log.set()

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=LOGIN_USERS.log)
async def login_talaba1(message: types.Message, state: FSMContext):
    await message.answer("<b>Familyangiz kiriting :</b>\n"
                         "<i>(Lotin harflarda)</i>", reply_markup=orqaga1)
    ism_kes = message.text
    await state.update_data(
        {"ism": ism_kes}
    )
    await LOGIN_USERS.password.set()

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=LOGIN_USERS.password)
async def login_talaba2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("ism")
    recaptcha = await db.select_login_two()
    status_login = 0
    for inza in recaptcha:
        if str(inza['familya'].lower()) == str(message.text.lower()):
            if str(inza['ism'].lower()) == str(name.lower()):
                await message.answer(f"🧑‍🎓<b>{message.text.title()} {name.title()}</b>\nShaxsiy kabinetingizga xush kelibsiz", reply_markup=menu_uquvchi)
                for login in ADMINS:
                    try:
                        await bot.send_message(chat_id=login,
                                               text=f"🔔,, {message.text.title()} {name.title()} '' <b>o'quvchi shaxsiy kabinetiga kirish aniqlandi !</b>\nTashrif buyuruvchi: {message.from_user.get_mention(as_html=True)}")
                        await db.add_panel_user(namename=f"{name.lower()}",
                                                full_name=f"{message.text.lower()}",
                                                telegram_id=message.from_user.id)
                    except aiogram.utils.exceptions.ChatNotFound:
                        pass

                status_login += 1
                break;
        if status_login == 1:
            break;
    if status_login == 0:
        await message.answer("<b>✖️ Bunday login va parol topilmadi</b>❗️", reply_markup=menu)

    await state.finish()


