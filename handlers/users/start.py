import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import executor
from data.config import ADMINS
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import executor
from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.defoultbutton import markup
from keyboards.inline.inline_button import inline_markup,back
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


from aiogram.dispatcher import FSMContext

@dp.message_handler(CommandStart(),state="*")
async def bot_start(message: types.Message,state: FSMContext):
    await state.finish()
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,name=name)
        await message.answer(f"Assalomu alaykum {name}\nBizning botimizga tashrif buyirganingizdan xursandmiz 😊\n\n⚠️ Botni qanday ishlatish bilmasangiz /help kamandasin bosing", reply_markup=markup)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        if message.from_user.username is not None: 
            msg = f"Bazaga yangi user qo'shildi\n🙎🏻‍♂️ Name: <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n🆔 ID si: <code>{message.from_user.id}</code>\n✉️ Username: @{message.from_user.username}\n\nBazada {count} ta foydalanuvchi bor"
            await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode='HTML')
        else:
            msg = f"Bazaga yangi user qo'shildi\n🙎🏻‍♂️ Name: <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n🆔 ID si: <code>{message.from_user.id}</code>\n\nBazada {count} ta foydalanuvchi bor."
            await bot.send_message(chat_id=ADMINS[0], text=msg,parse_mode='HTML')

    except sqlite3.IntegrityError as err:
        if message.from_user.username is not None:
            await bot.send_message(chat_id=ADMINS[0], text=f"🙎🏻‍♂️ <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> bazaga oldin qo'shilgan\n✉️ Username: @{message.from_user.username}\n🆔 ID si: <code>{message.from_user.id}</code>",parse_mode='HTML')
        else:
            await bot.send_message(chat_id=ADMINS[0], text=f"🙎🏻‍♂️ <a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a> bazaga oldin qo'shilgan\n🆔 ID si: <code>{message.from_user.id}</code>",parse_mode='HTML')
        await message.answer(f"Assalomu alaykum {name}\nBizning botimizga tashrif buyirganingizdan xursandmiz 😊\n\n⚠️ Botni qanday ishlatish bilmasangiz /help kamandasin bosing", reply_markup=markup)


