from aiogram import BaseMiddleware
from database import db

class UserMiddleware(BaseMiddleware):
    
    async def __call__(self, handler, event, data):
        user_id = event.from_user.id
        name = event.from_user.full_name

        user = db.cursor.execute(
            "SELECT * FROM users WHERE user_id = ?", (user_id,)
        ).fetchone()

        if user is None:
            db.add_user(user_id, name, "start")

        return await handler(event, data)
