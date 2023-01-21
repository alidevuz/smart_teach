from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, message, ReplyKeyboardRemove
from data.config import ADMINS
from keyboards.default.tugmalar_k import orqaga1, menu, menu_uquvchi, menu_uqituvchi
from keyboards.tugmalar_i import startInlaine
from loader import dp, db
from states.personalData import PersonalData




@dp.message_handler(text="📝Kursga yozilish")
async def buy_courses(message: types.Message, state: FSMContext):
    await message.answer("<i>Iltimos pastdagi so'rovnomalarni to'ldiring !</i>", reply_markup=orqaga1)
    await message.answer("<b>Kurs turini tanlang👇 :</b>", reply_markup=startInlaine)
    await PersonalData.day.set()

state_filtir = ['prezident_maktabi','mental_arifmetika','ona_tili','ingiliz_tili','geografiya','biologiya','tarix','fizika','kores_tili','kimyo','rus_tili','matematika']
@dp.callback_query_handler(text=state_filtir, state=PersonalData.day)
async def awer_manil(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    kurs_turi = call.data
    await state.update_data(
        {"data1": kurs_turi}
    )
    await call.message.answer("<b>Ism va Familyangiz yozing</b>", reply_markup=orqaga1)
    await PersonalData.fullname.set()



@dp.message_handler(text='⬅️Orqaga', state=PersonalData.fullname)
async def state_stop(message: types.Message, state: FSMContext):
    await state.finish()
    tek13 = await db.select_panel_one(telegram_id=message.from_user.id)
    tek8 = await db.select_panel_teacher(telegram_id3=message.from_user.id)

    if tek13 != None:
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu_uquvchi)
    elif tek8 != None:
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu_uqituvchi)

    elif tek13 == None:
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu)
@dp.message_handler(text='⬅️Orqaga', state=PersonalData.phoneNum)
async def state_stop(message: types.Message, state: FSMContext):
    await state.finish()
    tek12 = await db.select_panel_one(telegram_id=message.from_user.id)
    tek9 = await db.select_panel_teacher(telegram_id3=message.from_user.id)

    if tek12 != None:
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu_uquvchi)
    elif tek9 != None:
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu_uqituvchi)
    elif tek12 == None:
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu)
@dp.message_handler(text='⬅️Orqaga', state=PersonalData.day)
async def state_stop(message: types.Message, state: FSMContext):
    await state.finish()
    tek11 = await db.select_panel_one(telegram_id=message.from_user.id)
    tek10 = await db.select_panel_teacher(telegram_id3=message.from_user.id)

    if tek11 != None:
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu_uquvchi)
    elif tek10 != None:
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu_uqituvchi)
    elif tek11 == None:
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu)
@dp.message_handler(state=PersonalData.fullname)
async def anser_fullname(message: types.Message, state: FSMContext):

    fullname=message.text
    await state.update_data(
        {"name": fullname}
    )



    # Telefon nomer uchun
    await message.answer("<b>📞Telefon raqam :</b>\n\n<i>🚧Namuna👉 :</i> +998901234567", reply_markup=orqaga1)
   # await PersonalData.next()
    await PersonalData.phoneNum.set()



@dp.message_handler(state=PersonalData.phoneNum)
async def answr_gmail(message: types.Message, state: FSMContext):

    #Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get("name")
    kurs = data.get("data1")




    msg = "<b>🗂Kursga ro'yxatdan o'tish:</b>\n\n"
    msg += f"<u><b>F.I.O :</b></u><em> {name}</em>\n"
    msg += f"<u><b>Telefon :</b></u><em> {message.text}</em>\n"
    msg += f"<u><b>Kurs turi :</b></u><em> {kurs}</em>\n"
    msg += f"<u><b>Yubordi :</b></u> {message.from_user.get_mention(as_html=True)}\n"
    for i in ADMINS:
        await dp.bot.send_message(chat_id=i, text=msg)
    await message.answer("<i>Arizangiz qabul qilindi\n⏳ Tez orada operatorlar siz bilan bog'lanishadi </i>", reply_markup=menu)
    await state.finish()
    await state.reset_state(with_data=True)


