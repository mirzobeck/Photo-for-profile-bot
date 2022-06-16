from aiogram.types import Message, CallbackQuery
from PIL import Image, ImageDraw, ImageFont

from aiogram.dispatcher.storage import FSMContext
from states.st import rasm
from data.config import ADMINS
from loader import dp, db, bot
from keyboards.inline.btn import photo
from keyboards.default.btn import rasm_tanlash
import os

@dp.message_handler(state=rasm.txt)
async def photo_text(msg: Message, state: FSMContext):
    if len(msg.text) > 15:
        await msg.answer("Biz faqat eng ko'pi bilan 15 ta harfdan iborat ismni yoza olamiz! Uzur")
        await msg.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash)
        await state.finish()
    else:
        data = await state.get_data()
        number = data.get('number')
        if int(number) == 1:
            img = Image.open('photos/1.jpg')
            d1 = ImageDraw.Draw(img)
            if 13 > len(msg.text) > 9:
                myFont = ImageFont.truetype('fonts/grindanddeath/GrindAndDeath_Demo.ttf', 28)
            elif 15 >= len(msg.text) >= 13:
                myFont = ImageFont.truetype('fonts/grindanddeath/GrindAndDeath_Demo.ttf', 25)
            else:
                myFont = ImageFont.truetype('fonts/grindanddeath/GrindAndDeath_Demo.ttf', 35)
            sz = img.size
            W, H = sz[0], sz[1]
            w, h = d1.textsize(msg.text, myFont)
            d1.text((((W-w)/2+7), 245), f"{msg.text}", font=myFont, fill =(255, 0, 0),)
            img.save(f"photos/{msg.from_user.id}.jpg")
            await msg.answer_photo(photo=open(f"photos/{msg.from_user.id}.jpg", 'rb'))
            os.remove(os.path.join(f'photos/{msg.from_user.id}.jpg'))
            await msg.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash)
            await state.finish()
        elif int(number) == 2:
            img = Image.open('photos/2.jpg')
            d1 = ImageDraw.Draw(img)
            if 13 > len(msg.text) > 9:
                myFont = ImageFont.truetype('fonts/hey_brothers/Hey Brothers.ttf', 100)
            elif 15 >= len(msg.text) >= 13:
                myFont = ImageFont.truetype('fonts/hey_brothers/Hey Brothers.ttf', 100)
            else:
                myFont = ImageFont.truetype('fonts/hey_brothers/Hey Brothers.ttf', 120)
            sz = img.size
            W, H = sz[0], sz[1]
            w, h = d1.textsize(msg.text, myFont)
            d1.text((((W-w)/2+7), 910), f"{msg.text}", font=myFont, fill =(31, 144, 209),)
            img.save(f"photos/{msg.from_user.id}.jpg")
            await msg.answer_photo(photo=open(f"photos/{msg.from_user.id}.jpg", 'rb'))
            os.remove(os.path.join(f'photos/{msg.from_user.id}.jpg'))
            await msg.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash)
            await state.finish()
        elif int(number) == 3:
            img = Image.open('photos/3.jpg')
            d1 = ImageDraw.Draw(img)
            if 13 > len(msg.text) > 9:
                myFont = ImageFont.truetype('fonts/hopes_letter/Hopes Letter.ttf', 180)
            elif 15 >= len(msg.text) >= 13:
                myFont = ImageFont.truetype('fonts/hopes_letter/Hopes Letter.ttf', 165)
            else:
                myFont = ImageFont.truetype('fonts/hopes_letter/Hopes Letter.ttf', 210)
            sz = img.size
            W, H = sz[0], sz[1]
            w, h = d1.textsize(msg.text, myFont)
            d1.text((((W-w)/2+7), 720), f"{msg.text}", font=myFont, fill =(4, 20, 201))
            img.save(f"photos/{msg.from_user.id}.jpg")
            await msg.answer_photo(photo=open(f"photos/{msg.from_user.id}.jpg", 'rb'))
            os.remove(os.path.join(f'photos/{msg.from_user.id}.jpg'))
            await msg.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash)
            await state.finish()
        elif int(number) == 4:
            img = Image.open('photos/4.jpg')
            d1 = ImageDraw.Draw(img)
            if 9 < len(msg.text) < 13:
                myFont = ImageFont.truetype('fonts/drainwood/Drainwood.ttf', 33)
            if 13 <= len(msg.text) <= 15:
                myFont = ImageFont.truetype('fonts/drainwood/Drainwood.ttf', 25)
            else:
                myFont = ImageFont.truetype('fonts/drainwood/Drainwood.ttf', 40)
            sz = img.size
            W, H = sz[0], sz[1]
            w, h = d1.textsize(msg.text, myFont)
            d1.text((((W-w)/2+3), 168), f"{msg.text}", font=myFont, fill =(255, 0, 0),)
            img.save(f"photos/{msg.from_user.id}.jpg")
            await msg.answer_photo(photo=open(f"photos/{msg.from_user.id}.jpg", 'rb'))
            os.remove(os.path.join(f'photos/{msg.from_user.id}.jpg'))
            await msg.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash)
            await state.finish()
        elif int(number) == 5:
            img = Image.open('photos/5.jpg')
            d1 = ImageDraw.Draw(img)
            if 13 > len(msg.text) > 9:
                myFont = ImageFont.truetype('fonts/hopes_letter/Hopes Letter.ttf', 160)
            elif 15 >= len(msg.text) >= 13:
                myFont = ImageFont.truetype('fonts/hopes_letter/Hopes Letter.ttf', 150)
            else:
                myFont = ImageFont.truetype('fonts/hopes_letter/Hopes Letter.ttf', 180)
            sz = img.size
            W, H = sz[0], sz[1]
            w, h = d1.textsize(msg.text, myFont)
            d1.text((((W-w)/2+7), 410), f"{msg.text}", font=myFont, fill =(127, 17, 191))
            img.save(f"photos/{msg.from_user.id}.jpg")
            await msg.answer_photo(photo=open(f"photos/{msg.from_user.id}.jpg", 'rb'))
            os.remove(os.path.join(f'photos/{msg.from_user.id}.jpg'))
            await msg.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash)
            await state.finish()
        elif int(number) == 6:
            img = Image.open('photos/6.jpg')
            d1 = ImageDraw.Draw(img)
            if 13 > len(msg.text) > 9:
                myFont = ImageFont.truetype('fonts/mephisto/MEPHISTO.TTF', 78)
            elif 15 >= len(msg.text) >= 13:
                myFont = ImageFont.truetype('fonts/mephisto/MEPHISTO.TTF', 65)
            else:
                myFont = ImageFont.truetype('fonts/mephisto/MEPHISTO.TTF', 105)
            sz = img.size
            W, H = sz[0], sz[1]
            w, h = d1.textsize(msg.text, myFont)
            d1.text((((W-w)/2+7), 370), f"{msg.text}", font=myFont, fill =(0, 173, 23))
            img.save(f"photos/{msg.from_user.id}.jpg")
            await msg.answer_photo(photo=open(f"photos/{msg.from_user.id}.jpg", 'rb'))
            os.remove(os.path.join(f'photos/{msg.from_user.id}.jpg'))
            await msg.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash)
            await state.finish()
        elif int(number) == 7:
            img = Image.open('photos/7.jpg')
            d1 = ImageDraw.Draw(img)
            if 13 > len(msg.text) > 9:
                myFont = ImageFont.truetype('fonts/cabaret_2/Cabaret.ttf', 135)
            elif 15 >= len(msg.text) >= 13:
                myFont = ImageFont.truetype('fonts/cabaret_2/Cabaret.ttf', 115)
            else:
                myFont = ImageFont.truetype('fonts/cabaret_2/Cabaret.ttf', 165)
            sz = img.size
            W, H = sz[0], sz[1]
            w, h = d1.textsize(msg.text, myFont)
            d1.text((((W-w)/2+7), 890), f"{msg.text}", font=myFont, fill =(0, 133, 64))
            img.save(f"photos/{msg.from_user.id}.jpg")
            await msg.answer_photo(photo=open(f"photos/{msg.from_user.id}.jpg", 'rb'))
            os.remove(os.path.join(f'photos/{msg.from_user.id}.jpg'))
            await msg.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash)
            await state.finish()
        elif int(number) == 8:
            img = Image.open('photos/8.jpg')
            d1 = ImageDraw.Draw(img)
            if 13 > len(msg.text) > 9:
                myFont = ImageFont.truetype('fonts/pinky_monogram/Pinky Monogram.ttf', 110)
            elif 15 >= len(msg.text) >= 13:
                myFont = ImageFont.truetype('fonts/pinky_monogram/Pinky Monogram.ttf', 85)
            else:
                myFont = ImageFont.truetype('fonts/pinky_monogram/Pinky Monogram.ttf', 165)
            sz = img.size
            W, H = sz[0], sz[1]
            w, h = d1.textsize(msg.text, myFont)
            d1.text((((W-w)/2+7), 850), f"{msg.text}", font=myFont, fill =(138, 0, 46))
            img.save(f"photos/{msg.from_user.id}.jpg")
            await msg.answer_photo(photo=open(f"photos/{msg.from_user.id}.jpg", 'rb'))
            os.remove(os.path.join(f'photos/{msg.from_user.id}.jpg'))
            await msg.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash)
            await state.finish()
        elif int(number) == 9:
            img = Image.open('photos/9.jpg')
            d1 = ImageDraw.Draw(img)
            if 13 > len(msg.text) > 9:
                myFont = ImageFont.truetype('fonts/dragon_3/Dragon FREE.ttf', 140)
            elif 15 >= len(msg.text) >= 13:
                myFont = ImageFont.truetype('fonts/dragon_3/Dragon FREE.ttf', 120)
            else:
                myFont = ImageFont.truetype('fonts/dragon_3/Dragon FREE.ttf', 165)
            sz = img.size
            W, H = sz[0], sz[1]
            w, h = d1.textsize(msg.text, myFont)
            d1.text((((W-w)/2+7), 1000), f"{msg.text}", font=myFont, fill =(141, 158, 90))
            img.save(f"photos/{msg.from_user.id}.jpg")
            await msg.answer_photo(photo=open(f"photos/{msg.from_user.id}.jpg", 'rb'))
            os.remove(os.path.join(f'photos/{msg.from_user.id}.jpg'))
            await msg.answer(f"Siz bosh menyudasiz!", reply_markup=rasm_tanlash)
            await state.finish()

@dp.message_handler()
async def d(msg: Message):
    await msg.delete()

@dp.message_handler(state=rasm.photo)
async def d(msg: Message):
    await msg.delete()