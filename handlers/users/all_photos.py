from aiogram.types import Message, CallbackQuery

from aiogram.dispatcher.storage import FSMContext
from states.st import rasm
from data.config import ADMINS
from loader import dp, db, bot
from keyboards.inline.btn import photo


@dp.message_handler(text="Rasmlar")
async def pht(msg: Message):
    await msg.answer_photo(photo=open("photos/all.jpg", 'rb'), caption="Rasmni tanglang:", reply_markup=photo)
    await rasm.photo.set()


@dp.callback_query_handler(state=rasm.photo)
async def ph(call: CallbackQuery, state: FSMContext):
    await state.update_data(
        {
            'number' : call.data
        }
    )
    await call.message.delete()
    await call.message.answer("Ismingizni yozing:")
    await rasm.txt.set()