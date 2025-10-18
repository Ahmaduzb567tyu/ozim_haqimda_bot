import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardRemove
from defoult_keyboard import main_keyboard
from keyboard_inline import about_inline, photo_inline, family, media_url


API_TOKEN = "8393138192:AAFYGWnnZx2j4fwnQ0gGCQ3zvDT4wAGSvso"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
photo = "https://yt3.googleusercontent.com/oQAzzpWIXuBcjU2F4oK6ZB0XzevUlv4DLP6aE5QAsJ1EvDOWHv_4uxyvoAFdQjrGCn5wqGh9=s900-c-k-c0x00ffffff-no-rj"
ahmadjon = "https://ik.imagekit.io/amj5ymhvt/Ahmadjon.jpg?updatedAt=1758704319420"
oilam = "https://ik.imagekit.io/amj5ymhvt/photo_2_2025-02-15_16-11-21.jpg?updatedAt=1758707401773"
@dp.message(Command("start"))
async def send_message(message: types.Message):
    await message.answer(text="Salom bu men haqimdagi bot",
                         reply_markup=main_keyboard())
# asd

@dp.message(F.text == "About me")
async def send_message(message: types.Message):
    await message.answer(text="Men haqimda malumot",
                         reply_markup=about_inline())
    await message.answer(text=" ",
                         reply_markup=ReplyKeyboardRemove())


@dp.callback_query(F.data == "text")
async def send_message(callback: types.CallbackQuery):
    await callback.message.answer(text="Nigmatullayev Ahmadjon")

@dp.callback_query(F.data == "photo")
async def send_message(callback: types.CallbackQuery):
    await callback.message.answer_photo(photo=ahmadjon)

@dp.callback_query(F.data == "photo")
async def send_message(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(photo=photo,
                                        reply_markup=photo_inline())



@dp.message(F.text == "Media url")
async def send_message(message: types.Message):
    await message.answer(text="Media",
                         reply_markup=media_url())
    await message.answer(text=" ",
                         reply_markup=ReplyKeyboardRemove())


@dp.message(F.text == "Family")
async def send_message(message: types.Message):
    await message.answer(text="Family",
                         reply_markup=family())
    await message.answer(text=" ",
                         reply_markup=ReplyKeyboardRemove())


@dp.callback_query(F.data == "info")
async def send_message(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="Men oilamni judaham yaxshi koraman!",
                                  reply_markup=family())


@dp.callback_query(F.data == "photo5")
async def send_message(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer_photo(photo=oilam,
                                        reply_markup=family())



@dp.callback_query(F.data == "back")
async def send_message(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="Ortga",
                                  reply_markup=main_keyboard())


@dp.callback_query(F.data == "back2")
async def send_message(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(text="Ortga",
                                  reply_markup=about_inline())



# like = False
# @dp.callback_query(F.data == "like")
# async def send_message(callback: types.CallbackQuery):
#     global like
#     if like == False:
#         await callback.answer(text="Siz like bosdingiz")
#         like = True
#     else:
#         await callback.answer(text="Siz like ni qaytarib oldingiz",
#                               show_alert=True)
#         like = False
#
#
#
# dislike = False
# @dp.callback_query(F.data == "dislike")
# async def send_message(callback: types.CallbackQuery):
#     global dislike
#     if dislike == False:
#         await callback.answer(text="Siz dislike bostingiz")
#         dislike = True
#     else:
#         await callback.answer(text="Siz dislike ni qaytarib oldingiz",
#                               show_alert=True)
#         dislike = False


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
