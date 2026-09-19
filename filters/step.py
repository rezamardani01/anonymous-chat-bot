from aiogram.filters import Filter

class StepFilter(Filter):
    def __init__(self, step):
        self.step = step

    async def __call__(self, message):
        current_step = db.getStep(message.from_user.id)
        return current_step == self.step