from loader import dp, bot
from data.config import CHANNELS
from utils.misc import subscription
from aiogram import types
from keyboards.inline.subscription import check_button
from keyboards.default.defoultbutton import markup
from filters.IsPrivate import IsPrivate

@dp.callback_query_handler(IsPrivate(),text="check_subs")
async def checker(call: types.CallbackQuery):
    await call.answer()
    final_status = True
    result = str()
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.from_user.id,
                                          channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            final_status *= status
            result += f"✅ <b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
        
        else:
            final_status *= False
            invite_link = await channel.export_invite_link()
            result += (f"❌ <a href='{invite_link}'><b>{channel.title}</b></a> kanaliga obuna bo'lmagansiz.\n\n")
    
    if final_status:
        await call.message.delete()
        name = call.from_user.full_name
        msg = f"Assalomu alaykum <a href='tg://user?id={call.from_user.id}'>{name}</a>!\n\nYordam: /help" 
        await call.message.answer(msg,reply_markup=markup,parse_mode='HTML')
    else:
        await call.message.delete()
        await call.message.answer(result, disable_web_page_preview=True, reply_markup=check_button)