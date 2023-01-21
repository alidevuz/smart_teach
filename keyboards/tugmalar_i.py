from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

#startni bosgandan keyin chiqsdigan inline tugmalar

startInlaine = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Matematika", callback_data="matematika"),
            InlineKeyboardButton(text="Rus tili", callback_data="rus_tili"),
            InlineKeyboardButton(text="Kimyo", callback_data="kimyo"),

        ],
        [
            InlineKeyboardButton(text="Kores tili", callback_data="kores_tili"),
            InlineKeyboardButton(text="Fizika", callback_data="fizika"),
            InlineKeyboardButton(text="Tarix", callback_data="tarix"),

        ],
        [
            InlineKeyboardButton(text="Biologiya", callback_data="biologiya"),
            InlineKeyboardButton(text="Geografiya", callback_data="geografiya"),
            InlineKeyboardButton(text="Ingiliz tili", callback_data="ingiliz_tili"),

        ],
        [
            InlineKeyboardButton(text="Ona tili", callback_data="ona_tili"),
            InlineKeyboardButton(text="Mental arifmetika", callback_data="mental_arifmetika"),

        ],
        [
            InlineKeyboardButton(text="Prezident maktabiga tayyatlov", callback_data="prezident_maktabi"),

        ],


    ]

)
lokatsiya = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1)🗺Google xaritada ochish", url='https://www.google.com/maps/dir/39.9166296,66.2478905/39.9165558,66.2479121/@39.9164033,66.2487488,601m/data=!3m1!1e3!4m2!4m1!3e0?hl=ru'),

        ],
        [
            InlineKeyboardButton(text="2)🗺Google xaritada ochish", callback_data="korili"),

        ],
        [
            InlineKeyboardButton(text="3)🗺Google xaritada ochish", callback_data="bioiya"),

        ],
    ]

)

surovnoma_user = InlineKeyboardMarkup(
    inline_keyboard=[

        [
            InlineKeyboardButton(text="👨‍🏫O'qituvchi", callback_data="domla"),
            InlineKeyboardButton(text="🧑‍🎓O'quvchi", callback_data="talaba"),

        ],

    ]

)

tartib_fan = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Matematika", callback_data="1"),
            InlineKeyboardButton(text="Rus tili", callback_data="2"),
            InlineKeyboardButton(text="Kimyo", callback_data="3"),

        ],
        [
            InlineKeyboardButton(text="Kores tili", callback_data="4"),
            InlineKeyboardButton(text="Fizika", callback_data="5"),
            InlineKeyboardButton(text="Tarix", callback_data="6"),

        ],
        [
            InlineKeyboardButton(text="Biologiya", callback_data="7"),
            InlineKeyboardButton(text="Geografiya", callback_data="8"),
            InlineKeyboardButton(text="Ingiliz tili", callback_data="9"),

        ],
        [
            InlineKeyboardButton(text="Ona tili", callback_data="10"),
            InlineKeyboardButton(text="Mental arifmetika", callback_data="11"),

        ],
        [
            InlineKeyboardButton(text="Prezident maktabiga tayyatlov", callback_data="12"),

        ],


    ]

)