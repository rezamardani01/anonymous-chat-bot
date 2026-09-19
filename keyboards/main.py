from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔎 پیدا کردن پارتنر")],
            [KeyboardButton(text="👤 پروفایل"), KeyboardButton(text="⚙️ تنظیمات")],
        ],
        resize_keyboard=True,
    )


def cancel_chat_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="❌ قطع ارتباط"),
            ]
        ],
        resize_keyboard=True,
    )


def cancel_serching_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="❌ لغو جستجو"),
            ]
        ],
        resize_keyboard=True,
    )
