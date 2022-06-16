import re
from loader import dp, db, bot
from aiogram import types
from states.st import rasm
from keyboards.default.btn import menu, rasm_tanlash, rasm_tanlash22, rasm_tanlash2
from utils.misc.subscription import check
from data.config import ADMINS
from aiogram.dispatcher.storage import FSMContext

@dp.message_handler(text="Bosh menyu",state=rasm.channel, user_id=ADMINS)
async def k(msg: types.Message, state: FSMContext):
    if len(db.get_channel()) == 0:
        await msg.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash22)
    else:
        await msg.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash)
    await state.finish()

@dp.message_handler(text="Kanal qo'shish", user_id=ADMINS)
async def k(msg: types.Message):
    await msg.answer("Meni kanalga admin qilgan bo'lsangiz kanal havolasini yuboring\nNamuna: @Bekodev",reply_markup=menu, disable_web_page_preview=True)
    await rasm.channel.set()

@dp.message_handler(state=rasm.channel, user_id=ADMINS)
async def k(msg: types.Message, state: FSMContext):
    if re.match('^@', msg.text):
        try:
            s = await check(user_id=msg.from_user.id, channel=msg.text)
            try:
                db.add_channel(msg.text)
                await msg.answer(f"{msg.text} kanallar ro'yxatiga qo'shildi!")
                await msg.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash)
                await state.finish()
            except:
                await msg.answer("Bunday havola bizning ro'yxatda mavjud!", reply_markup=menu)
        except:
            await msg.answer("Iltimos meni admin qiling!", reply_markup=menu)
    else:
        await msg.answer("Namuna shaklida yuboring!\nNamuna: @Bekodev", reply_markup=menu)