import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from data.config import CHANNELS
from utils.misc import subscription
from loader import bot
from keyboards.inline.subscription import check_button

class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
            if update.message.text in ['/start',]:
                return
        elif update.callback_query:
            user = update.callback_query.from_user.id
            if update.callback_query.data in ['check_subs',]:
                return
        else:
            return
        logging.info(user)
        result = str()
        final_status = True
        for channel in CHANNELS:
            status = await subscription.check(user_id=user,
                                              channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            if not status:
                invite_link = await channel.export_invite_link()
                result += (f"Siz bizni kanallardan chiqib ketdingiz!\n\n❌ <a href='{invite_link}'><b>{channel.title}</b></a>\n")
                
        if not final_status:
            await update.message.answer(result, disable_web_page_preview=True,reply_markup=check_button)
            raise CancelHandler()
