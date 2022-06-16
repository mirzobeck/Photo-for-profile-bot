import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.btn import rasm_tanlash, rasm_tanlash2, rasm_tanlash22

@dp.message_handler(CommandStart(), user_id=ADMINS)
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        if len(db.get_channel()) == 0:
            await message.answer(f"Xush kelibsiz! {name}\n\nSiz bu bot'da har xil rasmlarga o'z ismingizni yozishingiz mumkin!\nUning uchun avval o'zingizga maqul rasmni tanlang!", reply_markup=rasm_tanlash22)
        else:
            await message.answer(f"Xush kelibsiz! {name}\n\nSiz bu bot'da har xil rasmlarga o'z ismingizni yozishingiz mumkin!\nUning uchun avval o'zingizga maqul rasmni tanlang!", reply_markup=rasm_tanlash2)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as er:
        if len(db.get_channel()) == 0:
            await message.answer(f"Xush kelibsiz! {name}\n\nSiz bu bot'da har xil rasmlarga o'z ismingizni yozishingiz mumkin!\nUning uchun avval o'zingizga maqul rasmni tanlang!", reply_markup=rasm_tanlash22)
        else:
            await message.answer(f"Xush kelibsiz! {name}\n\nSiz bu bot'da har xil rasmlarga o'z ismingizni yozishingiz mumkin!\nUning uchun avval o'zingizga maqul rasmni tanlang!", reply_markup=rasm_tanlash2)



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        await message.answer(f"Xush kelibsiz! {name}\n\nSiz bu bot'da har xil rasmlarga o'z ismingizni yozishingiz mumkin!\nUning uchun avval o'zingizga maqul rasmni tanlang!", reply_markup=rasm_tanlash)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as er:
        await message.answer(f"Xush kelibsiz! {name}\n\nSiz bu bot'da har xil rasmlarga o'z ismingizni yozishingiz mumkin!\nUning uchun avval o'zingizga maqul rasmni tanlang!", reply_markup=rasm_tanlash)
