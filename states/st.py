from aiogram.dispatcher.filters.state import StatesGroup, State


class rasm(StatesGroup):
    photo = State()
    txt = State()
    channel = State()
    del_channel = State()