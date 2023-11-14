from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from loader import bot

class AdminFilter(BoundFilter):
    async def check(self, message: types.Message):
        user_id = message.from_user.id
        chat_id = message.chat.id
        member = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
        print(member.is_chat_admin())
        if member.is_chat_admin():
            return False
        else:
            return True