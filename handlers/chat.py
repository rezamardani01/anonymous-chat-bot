from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Filter
from keyboards.main import main_keyboard, cancel_chat_keyboard, cancel_serching_keyboard
from database import db
from filters.step import StepFilter

route = Router()

@route.message(F.text == "🔎 پیدا کردن پارتنر")
async def find_partner(message: Message):
    user_id = message.from_user.id
    db.setStep(user_id, "waiting")

    find_partner = db.getUserWaiting(user_id)
    if find_partner:
        partner_id = find_partner[0]
        db.setPartner(user_id, partner_id)
        db.setPartner(partner_id, user_id)
        db.setStep(user_id, "chatting")
        db.setStep(partner_id, "chatting")

        await message.answer(
            "✅ دوست ناشناس شما پیدا شد! حالا می‌توانید پیام ارسال کنید.",
            reply_markup=cancel_chat_keyboard(),
        )
        await message.bot.send_message(
            partner_id,
            "✅ دوست ناشناس شما پیدا شد! حالا می‌توانید پیام ارسال کنید.",
            reply_markup=cancel_chat_keyboard(),
        )
    else:
        await message.answer("🔎 در حال پیدا کردن پارتنر...", reply_markup=cancel_serching_keyboard())


@route.message(F.text == "❌ لغو جستجو")
async def cancel_searching(message: Message):
    user_id = message.from_user.id
    db.setStep(user_id, "start")
    await message.reply("جستجوی دوست لغو گردید!", reply_markup=main_keyboard())


@route.message(F.text == "❌ قطع ارتباط")
async def cancel_chat(message: Message):
    user_id = message.from_user.id
    user = db.get_user(user_id)
    partner_id = user[4]

    if partner_id:
        db.setPartner(user_id, None)
        db.setPartner(partner_id, None)
        db.setStep(user_id, "start")
        db.setStep(partner_id, "start")

        await message.answer(
            "❌ ارتباط قطع شد. حالا می‌توانید یک پارتنر جدید پیدا کنید.",
            reply_markup=main_keyboard(),
        )
        await message.bot.send_message(
            partner_id,
            "❌ دوست ناشناس شما ارتباط را قطع کرد. حالا می‌توانید یک پارتنر جدید پیدا کنید.",
            reply_markup=main_keyboard(),
        )
    else:
        await message.answer(
            "❌ شما هنوز پارتنری ندارید. لطفاً ابتدا یک پارتنر پیدا کنید."
        )


@route.message(StepFilter(step="chatting"))
async def chat(message: Message):
    user_id = message.from_user.id
    user = db.get_user(user_id)
    partner_id = user[4]

    if partner_id:
        await message.bot.send_message(partner_id, message.text)
    else:
        await message.answer(
            "❌ شما هنوز پارتنری ندارید. لطفاً ابتدا یک پارتنر پیدا کنید."
        )
