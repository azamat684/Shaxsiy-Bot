# import psycopg2
import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import executor
from data.config import ADMINS
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import executor
from data.config import ADMINS,CHANNELS
from loader import dp, db, bot
from keyboards.default.defoultbutton import markup
from keyboards.inline.inline_button import inline_markup,back
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from filters.IsPrivate import IsPrivate

from aiogram.dispatcher import FSMContext

@dp.message_handler(IsPrivate(),CommandStart(),state='*')
async def bot_start(message: types.Message,state: FSMContext):
    await state.finish()
    name = message.from_user.full_name
    channels_format = str()
    markup = InlineKeyboardMarkup(row_width=1)
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        channels_format += f"📌 <a href='{invite_link}'><b>{chat.title}</b></a>\n\n"
        markup.insert(InlineKeyboardButton(text=f"{chat.title}",url=invite_link))
    markup.insert(InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_subs"))
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,name=name,language=message.from_user.language_code)
        await message.answer(f"Assalomu alaykum <a href='tg://user?id={message.from_user.id}'>{name}</a>!\n<b><i>Quyidagi kanalga obuna bo'ling 👇🏻</i></b>", reply_markup=markup)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        if message.from_user.username is not None: 
            msg = f"Bazaga yangi foydalanuvchi qo'shildi\n🙎🏻‍♂️ Ismi: <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>\n🆔 ID si: <code>{message.from_user.id}</code>\n✉️ Foydalanuvchi nomi: @{message.from_user.username}\n✡️ Telegram tili: {message.from_user.language_code}\n\nBazada {count} ta foydalanuvchi bor"
            await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode='HTML')
        else:
            msg = f"Bazaga yangi foydalanuvchi qo'shildi\n🙎🏻‍♂️ Ismi: <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>\n🆔 ID si: <code>{message.from_user.id}</code>\n✡️ Telegram tili: {message.from_user.language_code}\n\nBazada {count} ta foydalanuvchi bor."
            await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode='HTML')

    except sqlite3.IntegrityError as err:
        if message.from_user.username is not None:
            await bot.send_message(chat_id=ADMINS[0], text=f"🙎🏻‍♂️ <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a> bazaga oldin qo'shilgan\n✉️ Foydalanuvchi nomi: @{message.from_user.username}\n🆔 ID si: <code>{message.from_user.id}</code>\n✡️ Telegram tili: {message.from_user.language_code}",parse_mode='HTML')
        else:
            await bot.send_message(chat_id=ADMINS[0], text=f"🙎🏻‍♂️ <a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a> bazaga oldin qo'shilgan\n🆔 ID si: <code>{message.from_user.id}</code>\n✡️ Telegram tili: {message.from_user.language_code}",parse_mode='HTML')
        await message.answer(f"Assalomu aleykum <a href='tg://user?id={message.from_user.id}'>{name}</a>!\n<b><i>Quyidagi kanalga obuna bo'ling 👇🏻</i></b>", reply_markup=markup)


