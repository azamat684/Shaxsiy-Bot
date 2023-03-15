import wikipedia 
import asyncio
from pytube import YouTube
from datetime import timedelta
from datetime import datetime
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from gtts import gTTS
from io import BytesIO
import os
import math
import requests
from googletrans import Translator
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import executor
from loader import dp, db, bot
from keyboards.default.defoultbutton import markup,shaharlar,wiki_til,registratsiya,til
from data.config import CHANNELS
from keyboards.inline.inline_button import inline_markup,back
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from downloader import tk
from insta import instadownloader
from states.state import video_yuklash_tiktok,yt_video_save,video_yuklash_insta,tillar,txt_to_voice,Azamat,tillar2,tillar3,tillar4,tillar5,wikipediakuu,qrcodee,wikipedia_eng,wikipedia_ru
from aiogram.dispatcher import FSMContext
import qrcode
import aiofiles
import pandas as pd

#Qrcode yasash kamandasi /qrcode
@dp.message_handler(commands=['qrcode'],state="*")
async def qrcode_make(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("Menga qrcode uchun biror matn yoki raqam yuboring!")
    await qrcodee.codee.set()

@dp.message_handler(state=qrcodee.codee)
async def ddd1(message: types.Message,state: FSMContext):
    qrcode_uchun_text = message.text
    img = qrcode.make(qrcode_uchun_text)
    # Faylni yaratish
    file_name = f'{message.from_user.id}.png'
    img.save(file_name)
    # Generatsiya qilingan QR kodni foydalanuvchiga yuborish
    with open(file_name, 'rb') as file:
        await message.reply_photo(file)
        await state.finish()
        
@dp.message_handler(text = "🔙Orqaga",state="*")
async def reg(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("◻️ Bosh menyuga qaytdinggiz\n🟢Pastdagi menyulardan o'zinggizga keragini tanlang!",reply_markup=markup)
        
#Ro'yxatdan o'tish Bo'limi
@dp.message_handler(text = "Ro'yxatdan o'tish ✅",state="*")
async def reg(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer(f"Telefon raqaminggizni jo'nating!\n\nPastda menyuda <b>'📞 Telefon Raqamni jo'natish'</b> tugmasi bor o'shani bosing",parse_mode='HTML',reply_markup=registratsiya)

@dp.message_handler(content_types='contact')
async def kantakt(message: types.Message):
    await message.answer(f"Sizni raqaminggiz muvvofaqiyatli saqlandi",reply_markup=markup)


#Matnni ovozli xabar qilish
@dp.message_handler(text = "💬 Text to Voice 🗣",state="*")
async def text_to_voice(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("Menga biror matn yuboring men ingliz tilda ovozli xabar qilib beraman!")
    await txt_to_voice.voicee.set()
    
@dp.message_handler(state=txt_to_voice.voicee)
async def text_to_voice1(message: types.Message,state: FSMContext):
    text = message.text
    audio = BytesIO()
    tts = gTTS(text=text, lang='en',slow=False)
    tts.write_to_fp(audio)
    audio.seek(0)
    await message.reply_voice(voice=audio)
    await state.finish()

#Wikipedia Bo'limi
@dp.message_handler(text = "🌏 Wikipedia",state="*")
async def wikipediaa(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Pastdan o'zinggizga kerakli tilni tanlang💁🏻‍♂️",reply_markup=wiki_til) 
    
# Ingliz tilda wikipedia topish wikipedia
@dp.message_handler(text = "English 🇺🇸",state='*')
async def wiki_eng(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("Send me a word and I'll dig it up (if I have it)")
    await wikipedia_eng.engg.set()

@dp.message_handler(text = "O'zbek 🇺🇿",state="*")
async def wiki_uz(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("Menga biror so'z yuboring men u haqida malumot chiqaraman (Agar menda bor bo'lsa)")
    await wikipediakuu.uzz.set()
    
@dp.message_handler(text = "Русский 🇷🇺",state='*')
async def wiki_ru(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("Пришлите мне слово, и я откопаю его (если он у меня есть)")
    await wikipedia_ru.ruu.set()
    
@dp.message_handler(state=wikipediakuu.uzz)
async def wiki_uz1(message: types.Message,state: FSMContext):
    matn = message.text
    wikipedia.set_lang(prefix='uz')
    w_uz= wikipedia.summary(matn)
    pd.options.display.max_rows = 10000
    try:
        if len(w_uz) > 50:
            for x in range(0, len(w_uz), 3000):
                await asyncio.sleep(0.05)
                await bot.send_message(message.chat.id, w_uz[x:x + 3000])
                await state.finish()
        else:
            await bot.send_message(message.chat.id, w_uz)
            await state.finish()
    except wikipedia.exceptions.PageError as err:
        await message.answer("🤷🏻‍♂️ Afsuski men malumot topolmadim!")
        await state.finish()
        
    

@dp.message_handler(state=wikipedia_ru.ruu)
async def wiki_ru1(message: types.Message,state: FSMContext):
    matn = message.text
    wikipedia.set_lang(prefix='ru')
    w_ru = wikipedia.summary(matn)
    pd.options.display.max_rows = 10000
    if len(w_ru) > 50:
        for x in range(0, len(w_ru), 3000):
            await asyncio.sleep(0.05)
            await bot.send_message(message.chat.id, w_ru[x:x + 3000])
            await state.finish()
    else:
        await bot.send_message(message.chat.id, w_ru)
        await state.finish()


@dp.message_handler(state=wikipedia_eng.engg)
async def wiki_eng3(message: types.Message,state: FSMContext):
    matn = message.text
    wikipedia.set_lang(prefix='en')
    w_eng = wikipedia.summary(matn)
    pd.options.display.max_rows = 10000
    if len(w_eng) > 50:
        for x in range(0, len(w_eng), 3000):
            await asyncio.sleep(0.05)
            await bot.send_message(message.chat.id, w_eng[x:x + 3000])
            await state.finish()
    else:
        await bot.send_message(message.chat.id, w_eng)
        await state.finish()




#Video Yuklash Bo'limi
@dp.message_handler(text = "📥 Video Yuklash",state='*')
async def vd_yuk(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Qaysi ishtimoiy tarmoqdan video yuklamoqchisiz?",reply_markup=inline_markup)



#Video Yuklash Tik Tok
@dp.callback_query_handler(text="tik_tok",state="*")
async def tik_tok(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<b>Yuklamoqchi bo'lgan videongizni url manzilini yuboring</b>",parse_mode='HTML',reply_markup=back)
    await video_yuklash_tiktok.tiktok_1_qism.set()
    
    
#Video Yuklash Instagram
@dp.callback_query_handler(text='instagram',state="*")
async def insta_vd(call: types.CallbackQuery,state: FSMContext):
    await state.finish()
    await call.message.edit_text("<b>Yuklamoqchi bo'lgan videongizni url manzilini yuboring</b>",parse_mode='HTML',reply_markup=back)
    await video_yuklash_insta.insta_1_qism.set()
    

@dp.message_handler(state=video_yuklash_tiktok.tiktok_1_qism)
async def insta_down(message: types.Message,state: FSMContext):
    try:
        u = message.text
        natija = tk(url1=u)
        text1 = message.text
        if text1.startswith("https://vm.tiktok.com/" and "https://vt.tiktok.com/"):
            await message.answer("<b>Iltimos biroz kuting video yuklanmoqda</b>",parse_mode='HTML')
            await message.answer_video(natija['video'],caption="<b>@for_testing_py_bot orqali yuklandi 📥</b>",parse_mode='HTML')
            await state.finish()
        elif text1.startswith("https://www.tiktok.com/"):
            await message.answer("<b>Iltimos biroz kuting video yuklanmoqda</b>",parse_mode='HTML')
            await message.answer_video(natija['video'],caption="<b>@for_testing_py_bot orqali yuklandi 📥</b>",parse_mode='HTML')
            await state.finish()
        else:
            await message.answer("Url manzili xato")
            await state.finish()
    except:
        await message.answer("<b>Kechirasiz,Bu url manzil orqali men hech nima topmadim</b> ",parse_mode='HTML') 
        await state.finish()
    


@dp.message_handler(state=video_yuklash_insta.insta_1_qism)
async def insta_fayl(message: types.Message,state: FSMContext):
    try:
        link = message.text
        data = instadownloader(link=link)
        if data == 'Bad':
            await message.answer("Bu url manzili xato")
            await state.finish()
        else:
            if data['type'] == 'image':
                await message.answer_photo(photo=data['media'],caption=f"<b>@for_testing_py_bot orqali yuklandi</b>",parse_mode='HTML')
                await state.finish()
            elif data['type'] == 'video':
                await message.answer_video(video=data['media'],caption="<b>@for_testing_py_bot orqali yuklandi</b>",parse_mode='HTML')
                await state.finish()
            elif data['type'] == 'carousel':
                for i in data['media']:
                    await message.answer_photo(photo=i,caption="<b>@for_testing_py_bot orqali yuklandi</b>",parse_mode='HTML')
                    # await bot.send_document(document=i,caption="<b>@for_testing_py_bot orqali yuklandi</b>",parse_mode='HTML',)
                    await state.finish()
            else:
                await message.answer("<b>Bu url manzil bo'yicha hech narsa topolmadim</b>")
                await state.finish()
    except:
        await message.answer("Menga faqat Instagramdagi biror postni havolasini jo'nating",parse_mode='HTML')
        await state.finish()

@dp.callback_query_handler(text = 'back',state="*")
async def orqagaa(call: types.CallbackQuery,state: FSMContext):
    await state.finish()
    await call.message.edit_text("Qaysi ishtimoiy tarmoqdan video yuklamoqchisiz?",reply_markup=inline_markup)




#Admin bo'limi
@dp.message_handler(text = "👨🏻‍💻 Admin",state="*")
async def admin1_bot(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Salom!\n👨🏽‍💻 Dasturchi: <a href='https://t.me/azikk_0418'>Azamat Dosmukhambetov</a>\n\nTaklif yoki bot bo'yicha shikoyatinggiz bo'lsa <a href='https://t.me/azikk_0418'>Admin</a> ga murojat qilishingiz mumkin\n<strong>Bizning botdan foydalanayotganinggiz uchun raxmat😊</strong>",parse_mode='HTML',disable_web_page_preview=True)

    


#Youtubedan video ko'chirish qismi
@dp.message_handler(text="📥 Youtube",state="*")
async def eng_uz(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("Menga <b>YOUTUBE</b> dagi videoni havolasini jo'nating",parse_mode="HTML")
    await yt_video_save.ytt.set()
@dp.message_handler(state=yt_video_save.ytt)
async def youtube(message: types.Message,state: FSMContext):   
      if message.text.startswith('https://youtube.com') or message.text.startswith('https://www.youtube.com/') or message.text.startswith('https://youtu.be/'):
            url = message.text
            yt = YouTube(url)
            title = yt.title
            author = yt.author
            channel = yt.channel_url
            resolution = yt.streams.get_highest_resolution().resolution
            file_size = yt.streams.get_highest_resolution().filesize
            length = yt.length
            date_published = yt.publish_date.strftime("%Y-%m-%d")
            views = yt.views
            picture = yt.thumbnail_url
 
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text="Yuklanmoq", callback_data="download"))
            await message.answer_photo(f'{picture}', caption=f"📹 <b>{title}</b> <a href='{url}'>→</a> \n" #Title#
                                 f"👤 <b>{author}</b> <a href='{channel}'>→</a> \n" #Author Of Channel# 
                                 f"⚙️ <b>Kengayish —</b> <code>{resolution}</code> \n" ##
                                 f"🗂 <b>Video Hajmi —</b> <code>{round(file_size * 0.000001, 2)}MB</code> \n" #File Size#
                                 f"⏳ <b>Vaqti —</b> <code>{str(timedelta(seconds=length))}</code> \n" #Length#
                                 f"🗓 <b>Qoyilgan sana —</b> <code>{date_published}</code> \n" #Date Published#
                                 f"👁 <b>Korilganlar —</b> <code>{views:,}</code> \n", parse_mode='HTML', reply_markup=keyboard) #Views#
      else:
            await message.answer(f"❗️<b>Bu Url Orqali hechnima topilmadi!</b>", parse_mode='HTML')
            
            

@dp.callback_query_handler(text="download")
async def button_download(call: types.CallbackQuery):
      url = call.message.html_text
      yt = YouTube(url)
      title = yt.title
      author = yt.author
      bot_info = await bot.get_me()
      resolution = yt.streams.get_highest_resolution().resolution
      stream = yt.streams.filter(progressive=True, file_extension="mp4")
      stream.get_highest_resolution().download(f'{call.message.chat.id}', f'{call.message.chat.id}_{yt.title}')
      with open(f"{call.message.chat.id}/{call.message.chat.id}_{yt.title}", 'rb') as video:
            await bot.send_video(call.message.chat.id, video, caption=f"📹 <b>{title}</b> \n" #Title#
                                    f"👤 <b>{author}</b> \n\n" #Author Of Channel#
                                    f"⚙️ <b>Sifati —</b> <code>{resolution}</code> \n"
                                    f"📥 <b>{bot_info.username} orqali yuklab olindi!</b>", parse_mode='HTML')
            os.remove(f"{call.message.chat.id}/{call.message.chat.id}_{yt.title}")
    
#Tarjimon Bo'limi
@dp.message_handler(text="🔄 Tarjimon",state="*")
async def tarjimon(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Qaysi tildan qaysi tilga tarjima qilmoqchisiz?\nPastdan menyudan tanlang!",reply_markup=til)

#TARJIMON ENG-UZ #1
@dp.message_handler(text="Eng🇺🇸-Uz🇺🇿",state="*")
async def eng_uz(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Tarjima qilmoqchi bo'lgan so'zingizni yuboring")
    await tillar2.eng_uz.set()
    

#TARJIMON UZ-ENG #2
@dp.message_handler(text="Uz🇺🇿-Eng🇺🇸",state="*")
async def uz_eng(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Tarjima qilmoqchi bo'lgan so'zingizni yuboring")
    await tillar.uz_eng.set()

#TARJIMON RU-UZ #3
@dp.message_handler(text="Ru🇷🇺-Uz🇺🇿",state="*")
async def ru_uz(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Tarjima qilmoqchi bo'lgan so'zinggizni yuboring")
    await tillar3.ru_uz.set()
    
#TARJIMON UZ-RU #4
@dp.message_handler(text="Uz🇺🇿-Ru🇷🇺",state="*")
async def uz_ru(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Tarjima qilmoqchi bo'lgan so'zinggizni yuboring")
    await tillar4.uz_ru.set()
    
    
    
#TARJIMON HOHLAGAN-TIL #5
@dp.message_handler(text="?-Uz 🇺🇿",state="*")
async def hohlagan_til_tarjima(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Siz hohlagan tildagi matnni yuboring men o'zbek tiliga tarjima qilib beraman!")
    await tillar5.hohlagan_til.set()



@dp.message_handler(state=tillar2.eng_uz)
async def eng_to_uz(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn = message.text
        translate = translator.translate(matn,dest='uz')
        await message.answer(f"{message.text} ni o'zbekchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        await state.finish()
    except:
        await message.answer("Xato😑\nSiz boshqa tilda matn yubordinggiz❌")
        await state.finish()

    


@dp.message_handler(state=tillar.uz_eng)
async def uz_eng1(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn = message.text
        translate = translator.translate(matn)
        await message.answer(f"{message.text} ni inglizchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        await state.finish()
    except:
        await message.answer("Xato")
        await state.finish()
    

@dp.message_handler(state=tillar3.ru_uz)
async def ru_to_uz(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn = message.text
        translate = translator.translate(matn,dest='uz')
        await message.answer(f"{message.text} ni o'zbekchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        await state.finish()
    except:
        await message.answer("Xato😑\nSiz boshqa tilda matn yubordinggiz❌")
        await state.finish()


@dp.message_handler(state=tillar4.uz_ru)
async def uz_to_ru(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn2 = message.text
        translate = translator.translate(matn2,dest='ru')
        await message.answer(f"{message.text} ni ruschaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        await state.finish()
    except:
        await message.answer("Xato 😑\nSiz boshqa tilda matn yubordingiz ❌")
        await state.finish()
        

    
@dp.message_handler(state=tillar5.hohlagan_til)
async def hohlagan_til_tarjima1(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn2 = message.text
        translate = translator.translate(matn2,dest='uz')
        await message.answer(f"{message.text} ni o'zbekchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        await state.finish()
    except:
        await message.answer("Xato 😑\nSiz boshqa tilda matn yubordingiz ❌")
        await state.finish()

#Ob-Havo bo'limi
@dp.message_handler(text = "⛅️ Ob-Havo",state="*")
async def ob_havo(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Pastdan menyular orqali viloyatingizni tanlang ✅",reply_markup=shaharlar)
    
#Ob-Havo bo'limi menyulari
@dp.message_handler(text='Toshkent')
async def toshkent_ob_havo(message: types.Message):
    try:
        city_name = "Tashkent"
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"<b>Toshkent</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamat_dosmukhambetov_fans'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))

        
@dp.message_handler(text='Samarqand')
async def Samarqand_ob_havo(message: types.Message):
    try:
        city_name = "Samarqand"
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamat_dosmukhambetov_fans'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))


@dp.message_handler(text='Buxoro')
async def Buxoro_ob_havo(message: types.Message):
    try:
        city_name = "Buxoro"
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamat_dosmukhambetov_fans'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))


@dp.message_handler(text='Nukus')
async def Nukus_ob_havo(message: types.Message):
    try:
        city_name = "Nukus"
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamat_dosmukhambetov_fans'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))


@dp.message_handler(text='Xorazm')
async def Nukus_ob_havo(message: types.Message):
    try:
        city_name = "Urganch"
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamat_dosmukhambetov_fans'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))
    
@dp.message_handler(text='Qashqadaryo')
async def Nukus_ob_havo(message: types.Message):
    try:
        city_name = "Qashqadaryo"
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamat_dosmukhambetov_fans'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))

@dp.message_handler(text="Farg'ona")
async def Nukus_ob_havo(message: types.Message):
    try:
        city_name = "Farg'ona"
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamat_dosmukhambetov_fans'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))
@dp.message_handler(text='Surxondaryo')
async def Nukus_ob_havo(message: types.Message):
    try:
        city_name = "Tirmiz"
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"<b>Surxondaryo</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamat_dosmukhambetov_fans'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))
@dp.message_handler(text='Namangan')
async def Nukus_ob_havo(message: types.Message):
    try:
        city_name = "Namangan"
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamat_dosmukhambetov_fans'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))
@dp.message_handler(text='Andijon')
async def Nukus_ob_havo(message: types.Message):
    try:
        city_name = "Andijon"
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamat_dosmukhambetov_fans'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))
@dp.message_handler(text='Jizzax')
async def Nukus_ob_havo(message: types.Message):
    try:
        city_name = "Jizzax"
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamat_dosmukhambetov_fans'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))

@dp.message_handler(text='Navoiy')
async def Nukus_ob_havo(message: types.Message):
    try:
        city_name = "Navoiy"
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamat_dosmukhambetov_fans'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))


#Ob-Havo Bo'limi Hohlagan davlatni ob-havosini bilish qismi
@dp.message_handler(text="Hohlagan davlatni ob-havosin bilish",state="*")
async def ob(message: types.Message):
    await message.reply("Qayerni ob havosi bo'yicha malumot kerak men sizga malumot beraman hududni nomini to'g'ri yozsanggiz albatta😊\nHudud nomini kiriting?")
    await Azamat.boshlanish.set()

@dp.message_handler(state=Azamat.boshlanish)
async def ob_havo_lyuboi_joy(message: types.Message,state: FSMContext):
    try:
        city_name = message.text
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamat_dosmukhambetov_fans'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
        await state.finish()
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))
        await state.finish()

