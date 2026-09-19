from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import db

from keyboards.main import main_keyboard, age_keyboard, gender_keyboard

route = Router()


@route.message(Command("start"))
async def start_bot(message: Message):
    user_id = message.from_user.id
    user = db.get_user(user_id)

    if user is None:
     db.add_user(user_id, step="register-enter-name")

     await message.answer(
        "👋 سلام و خوش اومدی!\n\n"
        "به ربات چت ناشناس خوش اومدی 🤝\n\n"
        "برای شروع، چند اطلاعات ساده ازت می‌گیریم.\n\n"
        "📝 لطفاً اسمت رو وارد کن:"
    )
     return

    if user[2] is not None and user[3] is not None and user[4] is not None and user[5] is not None:
     db.set_step(user_id, "start")

     await message.answer(
        "👋 خوش برگشتی!\n\n"
        "از منوی زیر می‌تونی ادامه بدی 🤝",
        reply_markup=main_keyboard()
    )
     return

    if user[2] is not None and user[3] is not None and user[4] is not None:
        db.set_step(user_id, "start")
        await message.answer(
            "👋 خوش برگشتی!\n\n"
            "به ربات چت ناشناس خوش اومدی 🤝\n\n"
            "از منوی زیر می‌تونی ادامه بدی:",
            reply_markup=main_keyboard(),
        )


@route.message(
    lambda message: db.get_user(message.from_user.id)[7].startswith("register-")
)
async def register_handler(message: Message):
    step = db.get_user(message.from_user.id)[7]
    user_id = message.from_user.id

    match step:

        case "register-enter-name":
            db.update_user(user_id, "name", message.text)
            db.set_step(user_id, "register-enter-age")
            await message.answer(
                "🎂 عالیه! حالا سنت رو از لیست زیر انتخاب کن:",
                reply_markup=age_keyboard(),
            )
            return

        case "register-enter-age":
            db.update_user(user_id, "age", int(message.text))
            db.set_step(user_id, "register-enter-gender")
            await message.answer(
                "👤 خیلی خوب! حالا جنسیتت رو انتخاب کن:", reply_markup=gender_keyboard()
            )
            return

        case "register-enter-gender":
            db.update_user(user_id, "gender", message.text)
            db.set_step(user_id, "register-enter-bio")
            await message.answer(
                "✍️ تقریباً تمومه! حالا یک معرفی کوتاه از خودت بنویس:",
                reply_markup=None,
            )
            return

        case "register-enter-bio":
            db.update_user(user_id, "bio", message.text)
            db.set_step(user_id, "start")
            await message.answer(
                "🎉 ثبت‌نامت با موفقیت کامل شد!\n\nحالا می‌تونی از منوی زیر شروع به پیدا کردن پارتنر کنی 🤝",
                reply_markup=main_keyboard(),
            )
            return
