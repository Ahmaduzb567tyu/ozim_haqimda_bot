from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    button = KeyboardButton(text="About me")
    button2 = KeyboardButton(text="Media url")
    button3 = KeyboardButton(text="Family")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2, button3]
        ],
        resize_keyboard=True
    )
    return rkm


