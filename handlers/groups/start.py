from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsGroup
from loader import dp,db,bot
from aiogram import types
import sqlite3


@dp.message_handler(IsGroup(), CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.first_name
    chat = message.chat
    try:
        if chat.username is None:
            db.add_groups(title=chat.title, group_id=chat.id,username=chat.username)
        else:
            db.add_groups(title=chat.title, group_id=chat.id)
        await message.answer(f"Hammaga xellou 👋, {chat.title} gruhi bazaga qo'shildi!")
    except sqlite3.IntegrityError:
        await message.answer(f"{chat.title} gruhi bazaga oldin qo'shilgan")