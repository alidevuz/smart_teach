import aiogram
import pytz
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove
from data.config import ADMINS
from keyboards.default.tugmalar_k import menu, orqaga1, menu_uquvchi, menu_uqituvchi
from keyboards.tugmalar_i import lokatsiya, surovnoma_user, tartib_fan
from loader import dp, db, bot
import datetime
import re
from datetime import datetime

from states.personalData import LOGIN_staeta

timeNow = datetime.now(pytz.timezone('Asia/Tashkent')).strftime("%d.%m.%Y")

print(timeNow)

@dp.message_handler(text='📃Davomat')
async def davomat_handler(message: types.Message):
    yuklanmoqada1 = await message.answer("⏳", reply_markup=ReplyKeyboardRemove())

    try:
        id_datt3 = await db.select_panel_one(telegram_id=message.from_user.id)
        ajratib_oldim3 = id_datt3[0]
        recaptcha3 = await db.select_login_two()
        status_login3 = 0
        for inza3 in recaptcha3:
            if str(inza3['familya'].lower()) == str(ajratib_oldim3['full_name'].lower()) and str(inza3['ism'].lower()) == str(ajratib_oldim3['namename'].lower()):
                damoat_jad = InlineKeyboardMarkup(row_width=1)
                zse3 = 0
                for sh in range(3):
                    zse3 += 1
                    if str(inza3[f'fan{str(zse3)}']) != '0':
                        damoat_jad.add(InlineKeyboardButton(text=f"{(inza3[f'fan{str(zse3)}']).title()}", callback_data=f"d{zse3}"))
                damoat_jad.add(InlineKeyboardButton(text="⬅️Orqaga", callback_data="nazat"))
                await yuklanmoqada1.delete()
                await message.answer("<i>📝Qaysi kursizni davomat jadvali kerak ?</i>", reply_markup=damoat_jad)
                status_login3 += 1
                break;
            if status_login3 == 1:
                break;
    except IndexError:
        await message.answer("<b>Hech qanday ma'lumot topilmadi</b>")

cal_filter_back2 = ["d1", "d2", "d3"]
@dp.callback_query_handler(text=cal_filter_back2)
async def davomat_statik(call: CallbackQuery):
    try:
        await call.answer(cache_time=30)
        id_datt4 = await db.select_panel_one(telegram_id=call.from_user.id)
        ajratib_oldim4 = id_datt4[0]
        recaptcha4 = await db.select_login_two()
        status_login4 = 0
        try:
            for inza4 in recaptcha4:
                if str(inza4['familya'].lower()) == str(ajratib_oldim4['full_name'].lower()) and str(
                        inza4['ism'].lower()) == str(ajratib_oldim4['namename'].lower()):
                    davomat_y = inza4[f'davomat{call.data[1:]}']
                    result = re.split(r'[/\s]', str(davomat_y))
                    msg_dav = f"<b>Shu oy bo'yicha <u>{inza4['ism']}  {inza4['familya']}</u> o'quvchi kelmagan dars kunlari jadvali :\n\n</b>"
                    sanoq_ro = 0
                    for adin in result:
                        sanoq_ro += 1
                        msg_dav += f"{sanoq_ro})  ❌  <i>{adin}-yil</i>\n"
                    await call.message.answer(msg_dav, reply_markup=menu_uquvchi)
                    await call.message.delete()

                    status_login4 += 1
                    break;
                if status_login4 == 1:
                    break;
        except ValueError:
            await call.message.answer("Sizning davomat jadvalingizda xatolik", reply_markup=menu_uquvchi)
    except aiogram.utils.exceptions.MessageToDeleteNotFound:
        pass

@dp.message_handler(text='📚Kurslar')
async def kurslar_handler(message: types.Message):
    photo_id = 'https://telegra.ph/kurslar-09-20-2'
    await message.answer_photo(photo=photo_id, caption="❗️Kattaqõrg'on shahridagi va tumanlardagi <b>Smart Teach</b> õquv markazlarida 2022-2023 yil uchun <u>Abituriyent</u> va <u>Prezident maktabiga</u> tayyorlov kurslariga start berildi. 🤩\n\n"
                                                       "<b>■ Bizda mavjud kurslar:</b>\n"
                                                       "<i>✔️ Matematika\n"
                                                       "✔️ Rus tili\n"
                                                       "✔️ Kimyo\n"
                                                       "✔️ Kores tili\n"
                                                       "✔️ Fizika\n"
                                                       "✔️ Tarix\n"
                                                       "✔️ Biologiya\n"
                                                       "✔️ Geografiya\n"
                                                       "✔️ Ingiliz tili\n"
                                                       "✔️ Ona tili\n"
                                                       "✔️ Mental arifmetika\n"
                                                       "✔️ Prezident maktabiga tayyorlov</i>\n\n"
                                                       "📢 Shoshiling! Joylar chegaralangan.\n(Kam ta'minlanganlar uchun 50%-100% gacha chegirmalar bor)\n<b>Smart Teach </b> bilan sifatli ta'lim oling  va talaba bõling.🤫\n"
                                                       "<u>🗺Manzil:</u>\n"
                                                       "<i>1) Kattaqo'rg'on sh. bozor NBU bank qarshisida\n"
                                                       "2) Narpay tuman 1-umumiy o'rta ta'lim maktab.\n"
                                                       "3) Narpay tuman 71-umumiy o'rta ta'lim maktab (Eski sanoat kolleji binosi )</i>", protect_content=True, reply_markup=orqaga1)

@dp.message_handler(text='⬅️Orqaga')
async def kurslar_ortga(message: types.Message):
    tek3 = str(await db.select_panel_one(telegram_id=message.from_user.id))
    tek4 = str(await db.select_panel_teacher(telegram_id3=message.from_user.id))

    if tek3[0:4] == "[<Re":
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu_uquvchi)
    elif tek4[0:4] == "[<Re":
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu_uqituvchi)
    elif tek3[0:4] != "[<Re" and tek4[0:4] != "[<Re":
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu)


@dp.callback_query_handler(text='nazat')
async def kurslar_ortga2(call: CallbackQuery):
    await call.message.delete()
    tek5 = str(await db.select_panel_one(telegram_id=call.message.from_user.id))
    tek6 = str(await db.select_panel_teacher(telegram_id3=call.message.from_user.id))

    if tek5[0:4] == "[<Re":
        await call.message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu_uquvchi)
    elif tek6[0:4] == "[<Re":
        await call.message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu_uqituvchi)
    elif tek5[0:4] != "[<Re" and tek6[0:4] != "[<Re":
        await call.message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu)

@dp.message_handler(text="💳 To'lov jadvali")
async def payme_statik(message: types.Message):
    oldin_daleta = await message.answer("⏳", reply_markup=ReplyKeyboardRemove())

    try:
        id_datt = await db.select_panel_one(telegram_id=message.from_user.id)
        ajratib_oldim = id_datt[0]
        recaptcha2 = await db.select_login_two()
        status_login = 0
        for inza2 in recaptcha2:
            if str(inza2['familya'].lower()) == str(ajratib_oldim['full_name'].lower()) and str(inza2['ism'].lower()) == str(ajratib_oldim['namename'].lower()):
                payme_buttons = InlineKeyboardMarkup(row_width=1)
                zse = 0
                for sh in range(3):
                    zse += 1
                    if str(inza2[f'fan{str(zse)}']) != '0':
                        payme_buttons.add(InlineKeyboardButton(text=f"{(inza2[f'fan{str(zse)}']).title()}", callback_data=zse))
                payme_buttons.add(InlineKeyboardButton(text="⬅️Orqaga", callback_data="nazat"))
                await oldin_daleta.delete()
                await message.answer("<i>Qaysi kursizni to'lov jadvali kerak ?</i>", reply_markup=payme_buttons)
                status_login += 1
                break;
            if status_login == 1:
                break;
    except IndexError:
        await message.answer("<b>Hech qanday ma'lumot topilmadi</b>")

cal_filter_back = [1, 2, 3]
@dp.callback_query_handler(text=cal_filter_back)
async def done_statik(call: CallbackQuery):
    await call.answer(cache_time=30)
    id_datt2 = await db.select_panel_one(telegram_id=call.from_user.id)
    ajratib_oldim2 = id_datt2[0]
    recaptcha22 = await db.select_login_two()
    status_login2 = 0
    for inza22 in recaptcha22:
        if str(inza22['familya'].lower()) == str(ajratib_oldim2['full_name'].lower()) and str(
                inza22['ism'].lower()) == str(ajratib_oldim2['namename'].lower()):
            oxitgi_payme = inza22[f'payme{call.data}']
            fan_nomi = inza22[f'fan{call.data}'].lower()
            kurs_narxi = await db.select_kassa_one(fan_nomi=fan_nomi)
            money = kurs_narxi[0]
            await call.message.delete()
            try:
                kun = oxitgi_payme[0:2]
                oy = int(oxitgi_payme[3:5]) + 1
                yil = int(oxitgi_payme[6:10])
                if int(oxitgi_payme[3:5]) == 12:
                    await call.message.answer(f"<b>✅Oxirgi to'langan sana:</b> <i>{oxitgi_payme}-yil</i>\n"
                                              f"<b>⏳Keyingi to'lov sanasi:</b> <i>{kun}.01.{yil + 1}-yil</i>\n\n"
                                              f" (<i>ESLATMA:  kurs narxi-{money['narxi']} so'm)</i>",
                                              reply_markup=menu_uquvchi)
                else:
                    await call.message.answer(f"<b>✅Oxirgi to'langan sana:</b> <i>{oxitgi_payme}-yil</i>\n"
                                              f"<b>⏳Keyingi to'lov sanasi:</b> <i>{kun}.{oy}.{yil}-yil</i>\n\n"
                                              f" (<i>ESLATMA:  kurs narxi-{money['narxi']} so'm)</i>",
                                              reply_markup=menu_uquvchi)

                status_login2 += 1
                break;
            except ValueError:
                await call.message.answer("Sizning to'lov jadvalingizda xatolik", reply_markup=menu_uquvchi)
        if status_login2 == 1:
            break;


@dp.message_handler(text='📍 Manzillar')
async def manzillar(message: types.Message):
    logo_id = 'https://telegra.ph/Logo-09-22'
    await message.answer_photo(photo=logo_id, caption="<u>🗺Manzil:</u>\n"
                                                       "<i>1) Kattaqo'rg'on sh. bozor NBU bank qarshisida\n"
                                                       "2) Narpay tuman 1-umumiy o'rta ta'lim maktab.\n"
                                                       "3) Narpay tuman 71-umumiy o'rta ta'lim maktab (Eski sanoat kolleji binosi )</i>", reply_markup=lokatsiya)

@dp.message_handler(text='📞 Aloqa')
async def aloqa_handler(message: types.Message):
    admin_logo = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHavAqEKhY8MRX7NntKRnkGqFTk42uJT_TuA&usqp=CAU'
    await message.answer_photo(photo=admin_logo, caption="<b>☎️ Aloqa uchun tel</b>:\n"
                                                         "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b<code><u>+998993111803</u></code>\n"
                                                         "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b<code><u>+998933583834</u></code>\n"
                                                         "📱 <b>Telegram manzil:</b>\n"
                                                         "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b@smart_teachuz\n"
                                                         "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b@smart_teachbot\n"
                                                         "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b@smart_teach_admin")

@dp.message_handler(text='🧮Davomat')
async def daxxxomat_handler(message: types.Message):
    kutish = await message.answer(".", reply_markup=orqaga1)
    mualim_izlash = await db.select_panel_teacher(telegram_id3=message.from_user.id)
    guruhlar_search = await db.select_teachers_search(ism=mualim_izlash[0]['namename3'], familya=mualim_izlash[0]['full_name3'])
    msg_search_key = InlineKeyboardMarkup(row_width=2)
    for one_indinficat in guruhlar_search[0]:
        if one_indinficat != "0":
            msg_search_key.add(InlineKeyboardButton(text=f"{one_indinficat}", callback_data=one_indinficat))

    await message.answer("<i>Qaysi guruh davomati kerak ?</i>", reply_markup=msg_search_key)

    await LOGIN_staeta.guruh.set()

@dp.message_handler(text='⬅️Orqaga', state='*')
async def kurslar_ortga2(message: types.Message, state: FSMContext):
    await state.finish()
    tek41 = str(await db.select_panel_teacher(telegram_id3=message.from_user.id))
    if tek41[0:4] == "[<Re":
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu_uqituvchi)
    elif tek41[0:4] != "[<Re":
        await message.answer("<i>⚡️Oyna ochildi</i>", reply_markup=menu)

@dp.callback_query_handler(state=LOGIN_staeta.guruh)
async def done_davomat2(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    sdas = await db.select_login_search1(guruh1=f"{call.data}")
    people_list = InlineKeyboardMarkup(row_width=1)
    sanoqchi = 0
    for exx in sdas:
        if sanoqchi == 50:
            break
        sanoqchi += 1
        people_list.add(InlineKeyboardButton(text=f"{exx['ism']}  {exx['familya']}", callback_data=f"{exx['ism']}_{exx['familya']}"))
    await call.message.answer(f"<b>{call.data}</b> <i>guruh o'quvchilar:</i>", reply_markup=people_list)
    await LOGIN_staeta.one_time.set()

@dp.callback_query_handler(state=LOGIN_staeta.one_time)
async def done_davomat4(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=10)
    call_edithion = re.sub(r'[_]','  ', call.data)
    call_klass = re.findall(r'\w+', call.message.text)
    fam_is = re.split(r'[_]', call.data)
    recaptcha2e2 = await db.select_login_two()
    guruh_n0 = re.findall(r'\w+', call.message.text)
    tugash_time = 0
    for inza2e2 in recaptcha2e2:
        if str(inza2e2['familya']) == str(fam_is[1]) and str(inza2e2['ism']) == str(fam_is[0]):
            tugash_time += 1
            if guruh_n0[0] == inza2e2['guruh1']:
                copy_nb1 = inza2e2['davomat1']
                timeNow = datetime.now(pytz.timezone('Asia/Tashkent')).strftime("%d.%m.%Y")
                await db.update_user_logins1(ism=str(fam_is[0]), familya=str(fam_is[1]),
                                             davomat1=f"{copy_nb1}/{timeNow}")
            elif guruh_n0[0] == inza2e2['guruh2']:
                copy_nb2 = inza2e2['davomat2']
                timeNow2 = datetime.now(pytz.timezone('Asia/Tashkent')).strftime("%d.%m.%Y")
                await db.update_user_logins2(ism=str(fam_is[0]), familya=str(fam_is[1]),
                                             davomat1=f"{copy_nb2}/{timeNow2}")
            elif guruh_n0[0] == inza2e2['guruh3']:
                copy_nb3 = inza2e2['davomat3']
                timeNow3 = datetime.now(pytz.timezone('Asia/Tashkent')).strftime("%d.%m.%Y")
                await db.update_user_logins2(ism=str(fam_is[0]), familya=str(fam_is[1]),
                                             davomat1=f"{copy_nb3}/{timeNow3}")
            people_list2 = InlineKeyboardMarkup(row_width=1)
            yeyr = call.message.reply_markup.inline_keyboard
            for o in yeyr:
                if o[0].text == call_edithion:
                    people_list2.add(
                        InlineKeyboardButton(text=f"❌{o[0].text}", callback_data=f"o{fam_is[0]}_{fam_is[1]}"))
                else:
                    people_list2.add(
                        InlineKeyboardButton(text=f"{o[0].text}", callback_data=f"{o[0].callback_data}"))
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=people_list2)
            nb_egasi = await db.select_login_panel()
            for nb in nb_egasi:
                fan_search = await db.select_teachers_search_fan()
                if str(nb['full_name'].lower()) == str(fam_is[1].lower()) and str(nb['namename'].lower()) == str(fam_is[0].lower()):
                    for fan_clab in fan_search:
                        if fan_clab['guruhi0']==call_klass[0] or fan_clab['guruhi1']==call_klass[0] or fan_clab['guruhi2']==call_klass[0] or fan_clab['guruhi3']==call_klass[0] or fan_clab['guruhi4']==call_klass[0] or fan_clab['guruhi5']==call_klass[0] or fan_clab['guruhi6']==call_klass[0] or fan_clab['guruhi7']==call_klass[0]:
                            await bot.send_message(chat_id=int(nb['telegram_id']), text=f"<i><u>Smart Teaach</u> o'quv markazi o'quvchisi \n</i><b>{nb['full_name'].title()} {nb['namename'].title()}</b> <i> {fan_clab['fan_edu']} fanidan bugungi({timeNow}) o'quv kursiga kelmaganini ma'lum qilamiz !</i>\n\n<b>©️Administrator</b>", disable_notification=False)
                            break


            if tugash_time == 1:
                tugash_time = 0
                break
@dp.message_handler(content_types='photo')
async def album_filtir(message: types.Message):
    if message.media_group_id == None:
        print('Albumsiz media')
    elif message.media_group_id != None:
        print("Album ko'rinishidagi media")






