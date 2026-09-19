from aiogram.filters import Filter
from database import db

class StepFilter(Filter):
    def __init__(self, step):
        self.step = step

    async def __call__(self, message):
        user = db.get_user(message.from_user.id)
        return user[7] == self.step