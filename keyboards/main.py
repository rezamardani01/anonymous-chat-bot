from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✍🏻 به یک ناشناس وصلم کن!", style="primary")],
            [KeyboardButton(text="👤 پروفایل"), KeyboardButton(text="⚙️ تنظیمات")],
        ],
        resize_keyboard=True,
    )


def cancel_chat_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="❌ قطع ارتباط", style="danger"),
            ]
        ],
        resize_keyboard=True,
    )


def cancel_serching_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="❌ لغو جستجو", style="danger"),
            ]
        ],
        resize_keyboard=True,
    )
