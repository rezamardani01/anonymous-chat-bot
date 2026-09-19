import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

from middlewares.users import UserMiddleware
from handlers.start import route as start_route
from handlers.chat import route as chat_route


TOKEN = "8507805503:AAHLvBbslolA1WVL45Mw_c_VWLGGkWnInoo"

dp = Dispatcher()

dp.include_router(start_route)
dp.include_router(chat_route)

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
