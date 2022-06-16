from loader import db, dp, bot
from aiogram import types
from states.st import rasm
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.config import ADMINS
from keyboards.default.btn import menu, rasm_tanlash, rasm_tanlash22
from aiogram.dispatcher.storage import FSMContext

@dp.message_handler(text='Kanal olib tashlash', user_id=ADMINS)
async def delete_ch(msg: types.Message):
    s = "Kanallar ro'yxati:\n\n"
    btn = InlineKeyboardMarkup()
    channels = db.get_channel()
    for channel in channels:
        kanal = await bot.get_chat(channel[0])
        title = kanal.title
        btn.row(InlineKeyboardButton(f"❌ {title} ❌", callback_data=channel[0]))
        invite_link = await kanal.export_invite_link()
        s += f"<a href='{invite_link}'>{title}</a>\n"
    btn.row(InlineKeyboardButton(f"Bosh menyu", callback_data="menu"))
    await msg.answer(s, parse_mode='html', reply_markup=btn, disable_web_page_preview=True)
    await rasm.del_channel.set()


@dp.callback_query_handler(state=rasm.del_channel, user_id=ADMINS)
async def delete(call: types.CallbackQuery, state: FSMContext):
    db.delete_channel(link=call.data)
    await call.message.delete()
    if len(db.get_channel()) == 0:
        await call.message.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash22)
        await state.finish()
    else:
        s = "Kanallar ro'yxati:\n\n"
        btn = InlineKeyboardMarkup()
        channels = db.get_channel()
        for channel in channels:
            kanal = await bot.get_chat(channel[0])
            title = kanal.title
            btn.row(InlineKeyboardButton(f"❌ {title} ❌", callback_data=channel[0]))
            invite_link = await kanal.export_invite_link()
            s += f"<a href='{invite_link}'>{title}</a>\n"
        btn.row(InlineKeyboardButton(f"Bosh menyu", callback_data="menu"))
        await call.message.answer(s, parse_mode='html', reply_markup=btn, disable_web_page_preview=True)
        await rasm.del_channel.set()

@dp.callback_query_handler(text="menu", state='*', user_id=ADMINS)
async def m(call: types.CallbackQuery, state: FSMContext):
    if len(db.get_channel()) == 0:
        await call.message.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash22)
    else:
        await call.message.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash)
    await call.message.delete()
    await state.finish()
    