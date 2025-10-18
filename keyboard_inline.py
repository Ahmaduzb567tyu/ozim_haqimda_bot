from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton


def about_inline():
    button = InlineKeyboardButton(text="Text", callback_data="text")
    button2 = InlineKeyboardButton(text="Photo", callback_data="photo")
    button4 = InlineKeyboardButton(text="Back ⬅️", callback_data="back")
    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2],
            [button4]
        ]
    )
    return ikm


def media_url():
    button = InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/ahmaduzb567tyu/")
    button2 = InlineKeyboardButton(text="Github", url="https://github.com/Ahmaduzb567tyu")
    button3 = InlineKeyboardButton(text="Telegram", url="https://t.me/ahmad_uzd")
    button4 = InlineKeyboardButton(text="Back ⬅️", callback_data="back")
    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2,button3],
            [button4]
        ]
    )
    return ikm


def family():
    button = InlineKeyboardButton(text="Malumot",callback_data="info")
    button2 = InlineKeyboardButton(text="Photo", callback_data="photo5")
    button4 = InlineKeyboardButton(text="Back ⬅️", callback_data="back")
    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2],
            [button4]
        ]
    )
    return ikm



def photo_inline():
    button = InlineKeyboardButton(text="👍 Like", callback_data="like")
    button2 = InlineKeyboardButton(text="👎 Dislike", callback_data="dislike")
    button3 = InlineKeyboardButton(text="⬅️ Back", callback_data="back2")
    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2],
            [button3]
        ]
    )
    return ikm


