from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

rasm_tanlash = ReplyKeyboardMarkup(
    [
        [KeyboardButton("Rasmlar")],
    ], resize_keyboard=True,
    one_time_keyboard=True
)

rasm_tanlash22 = ReplyKeyboardMarkup(
    [
        [KeyboardButton("Rasmlar")],
        [KeyboardButton("Kanal qo'shish")],
    ], resize_keyboard=True,
    one_time_keyboard=True
)

rasm_tanlash2 = ReplyKeyboardMarkup(
    [
        [KeyboardButton("Rasmlar")],
        [KeyboardButton("Kanal qo'shish")],
        [KeyboardButton("Kanal olib tashlash")]
    ], resize_keyboard=True,
    one_time_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton('Bosh menyu')]
    ], resize_keyboard=True, one_time_keyboard=True
)