from aiogram.dispatcher.filters.state import StatesGroup, State


class PersonalData(StatesGroup):
    fullname = State()
    phoneNum = State()
    day = State()

class LOGIN_USERS(StatesGroup):
    log = State()
    password = State()

class LOGIN_teachers(StatesGroup):
    name = State()
    full = State()
    parol = State()

class LOGIN_staeta(StatesGroup):
    guruh = State()
    one_time = State()
    two_time =State()
