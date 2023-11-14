from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.dispatcher import FSMContext
from loader import dp,bot
from filters.IsPrivate import IsPrivate

@dp.message_handler(IsPrivate(),CommandHelp(),state="*")
async def bot_help(message: types.Message,state: FSMContext):
        await state.finish()
        bot_info = await bot.get_me()
        text = (f"Bu bot nima qila oladi?\n\n"
                f"Ushbu bot orqali siz \n\n▪️ <b>Youtube</b>,<b>Instagram</b>,<b>Tik Tok</b> ishtimoiy tarmoqlaridan <b>video rasmlarni</b> yuklab olishingiz\n\n<b>▪️ Ob-Havo</b> malumotlari haqida bilib olishingiz\n\n▪️ To'g'ridan to'g'ri <b>google</b> dan biror narsa xaqida malumot so'rashingiz \n\n▪️ <b>Matnli</b> xabarlarni <b>Ovozli</b> xabarga aylatirishingiz\nva\n▪️ <b>Tarjimondan</b> foydalanishingiz mumkin 😊\n\nBotni Kamandalari\n\n"
                f"/start - Botni qayta ishga tushirish ♻️\n"
                f"/qrcode - Qrcode yasash *️⃣\n"
                f"/help - Botni qanday ishlatish 🆘\n\n"
                f"Bu bot Inline rejimdaham ishlaydi va bot usernameni olasizda va biror chatga kirib bot usernameni qo'yib keyin izidan biror bir narsa qidirasiz va bot sizga youtubedan video topib beradi 🤩\n\nTushinmagan bo'lsangiz misol: @{bot_info.username} Biror narsa")
        
        await message.answer(text,parse_mode="HTML")
