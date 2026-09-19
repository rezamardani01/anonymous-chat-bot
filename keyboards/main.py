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


def age_keyboard():

    keyboard = []

    ages = list(range(12, 71))

    for i in range(0, len(ages), 5):

        row = []

        for age in ages[i : i + 5]:
            row.append(KeyboardButton(text=str(age)))

        keyboard.append(row)

    return ReplyKeyboardMarkup(
        keyboard=keyboard, resize_keyboard=True, one_time_keyboard=True
    )

def gender_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👨 مرد"), KeyboardButton(text="👩 زن")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )