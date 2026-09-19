from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from database import db

from keyboards.main import main_keyboard

route = Router()

@route.message(Command("start"))
async def start_bot(message: Message):
    db.setStep(message.from_user.id, "start")
    await message.reply("کاربر گرامی سلام به ربات چت ناشناس خوش آمدید!", reply_markup=main_keyboard())