import wikipedia 
import asyncio
from PIL import Image
import io
from pytube import YouTube
from datetime import timedelta
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from gtts import gTTS
from io import BytesIO
import os
import requests
from googletrans import Translator
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import executor
from loader import dp, db, bot
from .transliterated import to_cyrillic,to_latin
from keyboards.default.defoultbutton import markup,shaharlar,wiki_til,registratsiya,til,chatni_yakunlash
from keyboards.inline.inline_button import txt_to_voice_lang,txt_to_voice_back,pdf_uchun_btn,jokes_lang,back_jokes, reaction_jokes
from data.config import CHANNELS
from keyboards.inline.inline_button import inline_markup,back
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from downloader import tk
from insta import instadownloader
from states.state import ChatGPT,video_yuklash_tiktok,yt_video_save,video_yuklash_insta,tillar,txt_to_voice,Azamat,tillar2,tillar3,tillar4,tillar5,wikipediakuu,qrcodee,wikipedia_eng,wikipedia_ru,kiril_lotin_kiril
from states.state import txt_to_voice_ar,txt_to_voice_de,txt_to_voice_en,txt_to_voice_ru,txt_to_voice_es,txt_to_voice_fr,txt_to_voice_hi,txt_to_voice_pt,txt_to_voice_tr,pdf,Jokes_lang
from aiogram.dispatcher import FSMContext
import qrcode
import pandas as pd
from aiogram.dispatcher.filters import Command
import pyjokes

#Qrcode yasash kamandasi /qrcode
@dp.message_handler(commands=['qrcode'],state="*")
async def qrcode_make(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("Menga qrcode yasash uchun biror matn yuboring!")
    await qrcodee.codee.set()


@dp.message_handler(text = "🔙Orqaga",state="*")
async def reg(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Siz asosiy bo'limdasiz kerakli bo'limni tanlang!",reply_markup=markup)
        
#Ro'yxatdan o'tish Bo'limi
@dp.message_handler(text = "✅ Register",state="*")
async def reg(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer(f"Telefon raqaminggizni jo'nating!\n\nPastda menyuda <b>'📞 Telefon Raqamni jo'natish'</b> tugmasi bor o'shani bosing",parse_mode='HTML',reply_markup=registratsiya)

@dp.message_handler(content_types='contact')
async def kantakt(message: types.Message):
    await message.answer(f"Sizni raqaminggiz muvvofaqiyatli saqlandi",reply_markup=markup)

@dp.message_handler(text="🤖 ChatGPT",state="*")
async def chat_gpt_await(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("Qiziqtirgan savolingiz bo'lsa menga yozishingiz mumkin,Men tez orada javob beraman!",reply_markup=chatni_yakunlash)
    await ChatGPT.start.set()
    
@dp.message_handler(text="🏞 Rasmni PDF qilish 📁",state="*")
async def rasm_to_pdf(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("Menga rasm yuboring men uni PDF shakilda sizga tashlab beraman")
    await pdf.pdf_start.set()
    


#Youtubedan video yuklash bo'limi 
@dp.message_handler(text="📥 Youtube",state="*")
async def eng_uz(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("Menga <b>youtube</b> dagi biror bir videoni havolasini jo'nating\n\n⚠️Eslatma: Havolani jo'natganingizdan keyin biroz kuting,\nVideoni yuklab bermasligiham mumkin!",parse_mode="HTML")
    await yt_video_save.ytt.set()


#Wikipedia Bo'limi
@dp.message_handler(text = "🌏 Wikipedia",state="*")
async def wikipediaa(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Malumotlar qaysi tilda chiqsin?",reply_markup=wiki_til) 
    
#Video Yuklash Bo'limi
@dp.message_handler(text = "📥 Video Yuklash",state='*')
async def vd_yuk(message: types.Message,state: FSMContext):
    await state.finish()
    # db.create_table_urls()
    await message.answer("Qaysi ishtimoiy tarmoqdan video yuklamoqchisiz?",reply_markup=inline_markup)
    
#Tarjimon Bo'limi
@dp.message_handler(text="🔄 Tarjimon",state="*")
async def tarjimon(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Qaysi tildan qaysi tilga tarjima qilmoqchisiz?\nPastdan menyudan tanlang!",reply_markup=til)

    
#Matnni ovozli xabar qilish
@dp.message_handler(text = "💬 Matnni Ovozli xabar qilish 🗣",state="*")
async def text_to_voice(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("<b><i>Xabarni qaysi tilda ovozli xabarga aylantirmoqchisiz...?\n(O'zbek tili ishlamaydi)!</i></b>",reply_markup=txt_to_voice_lang)
    
    
#Admin bo'limi
@dp.message_handler(text = "👨🏻‍💻 Dasturchi",state="*")
async def admin1_bot(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("Salom!\n👨🏽‍💻 Dasturchi: <a href='https://t.me/azikk_0418'>Azamat Dosmukhambetov</a>\n\nTaklif yoki bot bo'yicha shikoyatingiz bo'lsa <a href='https://t.me/azikk_0418'>Dasturchiga</a> ga murojat qiling iltimos\n<strong>Mening telegram botimdan foydalanayotganingiz uchun raxmat😊</strong>",parse_mode='HTML',disable_web_page_preview=True)

#Jokes
@dp.message_handler(text = "😅 Latifalar",state="*")
async def jokess(message: types.Message,state: FSMContext):
    await message.reply(text="Qaysi tilda latifa aytay?",reply_markup=jokes_lang)

    
@dp.callback_query_handler(text = "back_jokes",state="*")
async def new_jokes_en(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text(text="Qaysi tilda latifa aytay?",reply_markup=jokes_lang)
      

@dp.callback_query_handler(text = "joke_en",state="*")
async def jokes_en(call: types.CallbackQuery,state: FSMContext):
    await call.message.delete()
    get_jokes = pyjokes.get_joke(category='neutral')
    await call.message.answer(get_jokes,reply_markup=reaction_jokes)
    await Jokes_lang.set_lang_eng.set()
    
@dp.callback_query_handler(text = "new_joke",state=Jokes_lang.set_lang_eng)
async def new_jokes_en(call: types.CallbackQuery,state: FSMContext):
    get_jokes = pyjokes.get_joke(category='neutral')
    await call.message.edit_text(text=get_jokes,reply_markup=reaction_jokes)
 

@dp.callback_query_handler(lambda call: call.data in ["😐","🙂","😂"],state="*")
async def jokes_react_en(call: types.CallbackQuery,state: FSMContext):
    await call.answer('Thanks for reaction 👌')
    await call.message.edit_reply_markup(reply_markup=back_jokes)
    
@dp.callback_query_handler(text = "joke_uz",state="*")
async def jokes_uz(call: types.CallbackQuery,state: FSMContext):
    await call.message.delete()
    translator = Translator()
    get_jokes = pyjokes.get_joke(language='en',category='neutral')
    tarjima = translator.translate(get_jokes,dest='uz')
    await call.message.answer(tarjima.text, reply_markup=reaction_jokes)
    await Jokes_lang.set_lang_uz.set()
    
@dp.callback_query_handler(text = "new_joke",state=Jokes_lang.set_lang_uz)
async def new_jokes_uz(call: types.CallbackQuery,state: FSMContext):
    translator = Translator()
    get_jokes = pyjokes.get_joke(language='en',category='neutral')
    tarjima = translator.translate(get_jokes,dest='uz')
    await call.message.edit_text(text=tarjima.text,reply_markup=reaction_jokes)
 

@dp.callback_query_handler(lambda call: call.data in ["😐","🙂","😂"],state="*")
async def jokes_react_uz(call: types.CallbackQuery,state: FSMContext):
    await call.answer('Reaksiya uchun raxmat 👌')
    await call.message.edit_reply_markup(reply_markup=back_jokes)

@dp.callback_query_handler(text = "joke_ru",state="*")
async def jokes_ru(call: types.CallbackQuery,state: FSMContext):
    await call.message.delete()
    translator = Translator()
    get_jokes = pyjokes.get_joke(category='neutral')
    tarjima = translator.translate(get_jokes,dest='ru')
    await call.message.answer(tarjima.text, reply_markup=reaction_jokes)
    await Jokes_lang.set_lang_ru.set()
    
@dp.callback_query_handler(text = "new_joke",state=Jokes_lang.set_lang_ru)
async def new_jokes_ru(call: types.CallbackQuery,state: FSMContext):
    translator = Translator()
    get_jokes = pyjokes.get_joke(language='en',category='neutral')
    tarjima = translator.translate(get_jokes,dest='ru')
    await call.message.edit_text(text=tarjima.text,reply_markup=reaction_jokes)
 

@dp.callback_query_handler(lambda call: call.data in ["😐","🙂","😂"],state=Jokes_lang.set_lang_ru)
async def jokes_react_ru(call: types.CallbackQuery,state: FSMContext):
    await call.answer('Спасибо за реакцию 👌')
    await call.message.edit_reply_markup(reply_markup=back_jokes)
    
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
        

    
@dp.callback_query_handler(text='txt_voice_back',state="*")
async def txt_eng(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<b><i>Xabarni qaysi tilda ovozli xabarga aylantirmoqchisiz...?\n(O'zbek tili ishlamaydi)!</i></b>",reply_markup=txt_to_voice_lang)
    await state.finish()

@dp.callback_query_handler(text='uz',state="*")
async def txt_eng(call: types.CallbackQuery,state: FSMContext):
    await state.finish()
    await call.answer("❌ Mendagi malumotlar o'zbek tilini qo'llab quvvatlamaydi")

@dp.callback_query_handler(text='en')
async def txt_eng(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<i>Yaxshi Ingliz tili tanlandi ✅ Endi menga matn yuboring...</i>",parse_mode='HTML',reply_markup=txt_to_voice_back)
    await txt_to_voice_en.speak_en.set()
    
@dp.callback_query_handler(text='ru')
async def txt_eng(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<i>Yaxshi Rus tili tanlandi ✅ Endi menga matn yuboring...</i>",parse_mode='HTML',reply_markup=txt_to_voice_back)
    await txt_to_voice_ru.speak_ru.set()
    
@dp.callback_query_handler(text='es')
async def txt_eng(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<i>Yaxshi Ispan tili tanlandi ✅ Endi menga matn yuboring...</i>",parse_mode='HTML',reply_markup=txt_to_voice_back)
    await txt_to_voice_es.speak_es.set()
    
@dp.callback_query_handler(text='pt')
async def txt_eng(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<i>Yaxshi Portugal tili tanlandi ✅ Endi menga matn yuboring...</i>",parse_mode='HTML',reply_markup=txt_to_voice_back)
    await txt_to_voice_pt.speak_pt.set()
    
@dp.callback_query_handler(text='fr')
async def txt_eng(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<i>Yaxshi Frantsuz tili tanlandi ✅ Endi menga matn yuboring...</i>",parse_mode='HTML',reply_markup=txt_to_voice_back)
    await txt_to_voice_fr.speak_fr.set()
    
@dp.callback_query_handler(text='de')
async def txt_eng(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<i>Yaxshi Nemis tili tanlandi ✅ Endi menga matn yuboring...</i>",parse_mode='HTML',reply_markup=txt_to_voice_back)
    await txt_to_voice_de.speak_de.set()


@dp.callback_query_handler(text='hi')
async def txt_eng(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<i>Yaxshi Hind tili tanlandi ✅ Endi menga matn yuboring...</i>",parse_mode='HTML',reply_markup=txt_to_voice_back)
    await txt_to_voice_hi.speak_hi.set()


@dp.callback_query_handler(text='tr')
async def txt_eng(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<i>Yaxshi Turk tili tanlandi ✅ Endi menga matn yuboring...</i>",parse_mode='HTML',reply_markup=txt_to_voice_back)
    await txt_to_voice_tr.speak_tr.set()
    
@dp.callback_query_handler(text='ar')
async def txt_eng(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<i>Yaxshi Arab tili tanlandi ✅ Endi menga matn yuboring...</i>",parse_mode='HTML',reply_markup=txt_to_voice_back)
    await txt_to_voice_ar.speak_ar.set()
    

@dp.message_handler(state=txt_to_voice_en.speak_en)
async def text_to_voice_en(message: types.Message,state: FSMContext):
    text = message.text
    audio = BytesIO()
    tts = gTTS(text=text, lang='en',slow=False,)
    tts.write_to_fp(audio)
    audio.seek(0)
    await message.reply_voice(voice=audio)
    await state.finish()


    
@dp.message_handler(state=txt_to_voice_ru.speak_ru)
async def text_to_voice_en(message: types.Message,state: FSMContext):
    text = message.text
    audio = BytesIO()
    tts = gTTS(text=text, lang='ru',slow=False)
    tts.write_to_fp(audio)
    audio.seek(0)
    await message.reply_voice(voice=audio)
    await state.finish()
    

@dp.message_handler(state=txt_to_voice_es.speak_es)
async def text_to_voice_en(message: types.Message,state: FSMContext):
    text = message.text
    audio = BytesIO()
    tts = gTTS(text=text, lang='es',slow=False)
    tts.write_to_fp(audio)
    audio.seek(0)
    await message.reply_voice(voice=audio)
    await state.finish()
    

@dp.message_handler(state=txt_to_voice_pt.speak_pt)
async def text_to_voice_en(message: types.Message,state: FSMContext):
    text = message.text
    audio = BytesIO()
    tts = gTTS(text=text, lang='pt',slow=False)
    tts.write_to_fp(audio)
    audio.seek(0)
    await message.reply_voice(voice=audio)
    await state.finish()
    
    
@dp.message_handler(state=txt_to_voice_fr.speak_fr)
async def text_to_voice_en(message: types.Message,state: FSMContext):
    text = message.text
    audio = BytesIO()
    tts = gTTS(text=text, lang='fr',slow=False)
    tts.write_to_fp(audio)
    audio.seek(0)
    await message.reply_voice(voice=audio)
    await state.finish()

    
@dp.message_handler(state=txt_to_voice_de.speak_de)
async def text_to_voice_en(message: types.Message,state: FSMContext):
    text = message.text
    audio = BytesIO()
    tts = gTTS(text=text, lang='de',slow=False)
    tts.write_to_fp(audio)
    audio.seek(0)
    await message.reply_voice(voice=audio)
    await state.finish()

    
@dp.message_handler(state=txt_to_voice_hi.speak_hi)
async def text_to_voice_en(message: types.Message,state: FSMContext):
    text = message.text
    audio = BytesIO()
    tts = gTTS(text=text, lang='hi',slow=False)
    tts.write_to_fp(audio)
    audio.seek(0)
    await message.reply_voice(voice=audio)
    await state.finish()

    
@dp.message_handler(state=txt_to_voice_tr.speak_tr)
async def text_to_voice_en(message: types.Message,state: FSMContext):
    text = message.text
    audio = BytesIO()
    tts = gTTS(text=text, lang='tr',slow=False)
    tts.write_to_fp(audio)
    audio.seek(0)
    await message.reply_voice(voice=audio)
    await state.finish()
    

@dp.message_handler(state=txt_to_voice_ar.speak_ar)
async def text_to_voice_en(message: types.Message,state: FSMContext):
    text = message.text
    audio = BytesIO()
    tts = gTTS(text=text, lang='ar',slow=False)
    tts.write_to_fp(audio)
    audio.seek(0)
    await message.reply_voice(voice=audio)
    await state.finish()
    
@dp.callback_query_handler(text="txt_voice_back2",state="*")
async def txt_voice_back2(call: types.CallbackQuery,state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer(f"Siz asosiy bo'limdasiz kerakli bo'limni tanlang!",reply_markup=markup)



    
# Ingliz tilda wikipedia topish wikipedia
@dp.message_handler(text = "English 🇺🇸",state='*')
async def wiki_eng(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("What do you need information about?")
    await wikipedia_eng.engg.set()

@dp.message_handler(text = "O'zbek 🇺🇿",state="*")
async def wiki_uz(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("Nima haqida malumot kerak?")
    await wikipediakuu.uzz.set()
    
@dp.message_handler(text = "Русский 🇷🇺",state='*')
async def wiki_ru(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("О чем вам нужна информация?")
    await wikipedia_ru.ruu.set()
    
@dp.message_handler(state=wikipediakuu.uzz)
async def wiki_uz1(message: types.Message,state: FSMContext):
    try:
        matn = message.text
        wikipedia.set_lang(prefix='uz')
        w_uz= wikipedia.summary(matn)
        pd.options.display.max_rows = 10000
        if len(w_uz) > 50:
            await message.answer_chat_action(action="typing")
            for x in range(0, len(w_uz), 3000):
                await asyncio.sleep(0.05)
                await bot.send_message(message.chat.id, w_uz[x:x + 3000])
                await state.finish()
        else:
            await message.answer_chat_action(action="typing")
            await bot.send_message(message.chat.id, w_uz)
            await state.finish()
    except Exception:
        await message.reply("🤷🏻‍♂️ Afsuski men malumot topolmadim!")
        await state.finish()
        
    

@dp.message_handler(state=wikipedia_ru.ruu)
async def wiki_ru1(message: types.Message,state: FSMContext):
    try:
        matn = message.text
        wikipedia.set_lang(prefix='ru')
        w_ru = wikipedia.summary(matn)
        pd.options.display.max_rows = 10000
        if len(w_ru) > 50:
            await message.answer_chat_action(action="typing")
            for x in range(0, len(w_ru), 3000):
                await asyncio.sleep(0.05)
                await bot.send_message(message.chat.id, w_ru[x:x + 3000])
                await state.finish()
        else:
            await message.answer_chat_action(action="typing")
            await bot.send_message(message.chat.id, w_ru)
            await state.finish()
    except Exception:
        await message.reply("🤷🏻‍♂️ К сожалению, никакой информации найти не удалось!")

@dp.message_handler(state=wikipedia_eng.engg)
async def wiki_eng3(message: types.Message,state: FSMContext):
    try:
        matn = message.text
        wikipedia.set_lang(prefix='en')
        w_eng = wikipedia.summary(matn)
        pd.options.display.max_rows = 10000
        if len(w_eng) > 50:
            await message.answer_chat_action(action="typing")
            for x in range(0, len(w_eng), 3000):
                await asyncio.sleep(0.05)
                await bot.send_message(message.chat.id, w_eng[x:x + 3000])
                await state.finish()
        else:
            await message.answer_chat_action(action="typing")
            await bot.send_message(message.chat.id, w_eng)
            await state.finish()
    except Exception:
        await message.reply("🤷🏻‍♂️ Unfortunately, I couldn't find any information!")
        await state.finish()







#Video Yuklash Tik Tok
@dp.callback_query_handler(text="tik_tok",state="*")
async def tik_tok(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<b>Yuklamoqchi bo'lgan videongizni havolasini yuboring</b>",parse_mode='HTML',reply_markup=back)
    await video_yuklash_tiktok.tiktok_1_qism.set()
    
    
@dp.message_handler(state=video_yuklash_tiktok.tiktok_1_qism)
async def insta_down(message: types.Message,state: FSMContext):
    try:
        u = message.text
        natija = tk(url1=u)
        text1 = message.text
        if text1.startswith("https://vm.tiktok.com/" and "https://vt.tiktok.com/"):
            white = '◽️'
            black = '◼️'
            xabar = await bot.send_message(chat_id=message.from_user.id,text='<b>Yuklanmoqda</b>',parse_mode='HTML')
            for i in range(1,11):
                oq = (10-i) * white
                qora = i*black 
                await xabar.edit_text(text=f"{qora}{oq}\n"
                                    f"{10*i}% yuklanmoqda...")
    
            await xabar.delete()
            await message.answer_chat_action(action="upload_video")
            await message.answer_video(natija['video'],caption="<b>@azamats_robot orqali yuklandi 📥</b>",parse_mode='HTML')
            await state.finish()
        elif text1.startswith("https://www.tiktok.com/"):
            white = '◽️'
            black = '◼️'
            xabar = await bot.send_message(chat_id=message.from_user.id,text='<b>Yuklanmoqda</b>',parse_mode='HTML')
            for i in range(1,11):
                oq = (10-i) * white
                qora = i*black 
                await xabar.edit_text(text=f"{qora}{oq}\n"
                                    f"{10*i}% yuklanmoqda...")
    
            await xabar.delete()
            await message.answer_chat_action(action="upload_video")
            await message.answer_video(video=natija['video'],caption="<b>@azamats_robot orqali yuklandi 📥</b>",parse_mode='HTML')
            await state.finish()
        else:
            await message.answer("error")
            await state.finish()
    except:
        await message.answer("<b>Bu havola xato</b> ",parse_mode='HTML') 
        await state.finish()
    
#Video Yuklash Instagram
@dp.callback_query_handler(text='instagram',state="*")
async def insta_vd(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<b>Yuklamoqchi bo'lgan videongizni havolasini yuboring</b>",parse_mode='HTML',reply_markup=back)
    await video_yuklash_insta.insta_1_qism.set()

@dp.message_handler(state=video_yuklash_insta.insta_1_qism)
async def insta_fayl(message: types.Message,state: FSMContext):
    try:
        link = message.text
        data = instadownloader(link=link)
        if data == 'Bad':
            await message.answer("Bu havola xato")
            await state.finish()
        else:
            if data['type'] == 'image':
                white = '◽️'
                black = '◼️'
                xabar = await bot.send_message(chat_id=message.from_user.id,text='<b>Yuklanmoqda</b>',parse_mode='HTML')
                for i in range(1,11):
                    oq = (10-i) * white
                    qora = i*black 
                    await xabar.edit_text(text=f"{qora}{oq}\n"
                                        f"{10*i}% yuklanmoqda...")
        
                await xabar.delete()
                await message.answer_chat_action(action="upload_photo")
                await message.answer_photo(photo=data['media'],caption=f"{data['title']}\n\n<b>@azamats_robot orqali yuklandi</b>",parse_mode='HTML')
                await state.finish()
            elif data['type'] == 'video':
                white = '◽️'
                black = '◼️'
                xabar = await bot.send_message(chat_id=message.from_user.id,text='<b>Yuklanmoqda</b>',parse_mode='HTML')
                for i in range(1,11):
                    oq = (10-i) * white
                    qora = i*black 
                    await xabar.edit_text(text=f"{qora}{oq}\n"
                                        f"{10*i}% yuklanmoqda...")
        
                await xabar.delete()
                await message.answer_chat_action(action="upload_video")
                await message.answer_video(video=data['media'],caption=f"{data['title']}\n\n<b>@azamats_robot orqali yuklandi</b>",parse_mode='HTML')
                await state.finish()
            elif data['type'] == 'carousel':
                white = '◽️'
                black = '◼️'
                xabar = await bot.send_message(chat_id=message.from_user.id,text='<b>Yuklanmoqda</b>',parse_mode='HTML')
                for i in range(1,11):
                    oq = (10-i) * white
                    qora = i*black 
                    await xabar.edit_text(text=f"{qora}{oq}\n"
                                        f"{10*i}% yuklanmoqda...")
                await xabar.delete()
                for i in data['media']:
                    await message.answer_chat_action(action="upload_photo")
                    await message.answer_photo(photo=i,caption=f"{data['title']}\n\n<b>@azamats_robot orqali yuklandi</b>",parse_mode='HTML')
                    await state.finish()
            elif data['type'] == 'story':
                white = '◽️'
                black = '◼️'
                xabar = await bot.send_message(chat_id=message.from_user.id,text='<b>Yuklanmoqda</b>',parse_mode='HTML')
                for i in range(1,11):
                    oq = (10-i) * white
                    qora = i*black 
                    await xabar.edit_text(text=f"{qora}{oq}\n"
                                        f"{10*i}% yuklanmoqda...")
                await xabar.delete()
                await message.answer_chat_action(action="upload_video")
                await message.answer_video(video=data['media'],caption=f"<b>@azamats_robot orqali yuklandi</b>",parse_mode='HTML')
                await state.finish()
            elif data['type'] == 'story_image':
                white = '◽️'
                black = '◼️'
                xabar = await bot.send_message(chat_id=message.from_user.id,text='<b>Yuklanmoqda</b>',parse_mode='HTML')
                for i in range(1,11):
                    oq = (10-i) * white
                    qora = i*black 
                    await xabar.edit_text(text=f"{qora}{oq}\n"
                                        f"{10*i}% yuklanmoqda...")
                await xabar.delete()
                await message.answer_chat_action(action="upload_photo")
                await message.answer_photo(photo=data['media'],caption=f"<b>@azamats_robot orqali yuklandi</b>",parse_mode='HTML')
                await state.finish()
            else:
                await message.answer("<b>Bu havola bo'yicha hech narsa topolmadim</b>")
                await state.finish()
    except:
        await message.answer("Ooops! Biror nimani xato qildingiz yoki Menda instagramdan video yuklab berish so'rovi tamom bo'lgan",parse_mode='HTML')
        await state.finish()

@dp.callback_query_handler(text = 'back',state="*")
async def orqagaa(call: types.CallbackQuery,state: FSMContext):
    await state.finish()
    await call.message.edit_text("Qaysi ishtimoiy tarmoqdan video yuklamoqchisiz?",reply_markup=inline_markup)



#PDF Tayorlash qismi
@dp.message_handler(content_types=['photo'],state=pdf.pdf_start)
async def make_pdf(message: types.Message,state: FSMContext):
    await state.finish()
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id=file_id)
    file_url = bot.get_file_url(file_path=file.file_path)
    
    data = await state.get_data()
    urls = data.get('urls',[])
    urls.append(file_url)
    await state.update_data({"urls":urls})
    
    
    await message.reply("✅ Rasm qabul qilindi"
                        f"\n\nPDF formatga o'tkazaymi 👇🏻?",reply_markup=pdf_uchun_btn)

@dp.callback_query_handler(text="make_pdf", state="*")
async def make_pdf1(call: types.CallbackQuery, state: FSMContext):
    await call.answer('Tayyorlanmoqda...')
    await call.message.delete()
    data = await state.get_data()
    urls = data.get('urls', [])
    images = []
    for url in urls:
        image = Image.open(requests.get(url=url, stream=True).raw)
        images.append(image)

    pdf = io.BytesIO()
    images[0].save(pdf, format='PDF', save_all=True, append_images=images[1:], resolution=100)
    pdf.seek(0)
    file = types.InputFile(pdf, filename=f"{call.from_user.full_name}.pdf")

    white = '◽️'
    black = '◼️'
    xabar = await bot.send_message(chat_id=call.from_user.id,text='<b>Yuklanmoqda</b>',parse_mode='HTML')
    for i in range(1,11):
        oq = (10-i) * white
        qora = i*black 
        await xabar.edit_text(text=f"{qora}{oq}\n"
                              f"{10*i}% yuklanmoqda...")
    
    await xabar.delete()
    await call.message.answer_document(document=file,caption="@azamats_robot orqali yuklandi ")


#PDF yasashni bekor qilish
@dp.callback_query_handler(text="otmen_pdf",state="*")
async def otmen_pdf1(call: types.CallbackQuery,state: FSMContext):
    await state.update_data({
        'urls':[]
    })
    await call.message.delete()
    
    await call.message.answer("Amal bekor qilindi!\nSiz asosiy bo'limdasiz kerakli bo'limni tanlang!",reply_markup=markup)
    await state.finish()
    
    

#Youtubedan video ko'chirish qismi
@dp.message_handler(state=yt_video_save.ytt)
async def youtube(message: types.Message,state: FSMContext):   
      if message.text.startswith('https://youtube.com') or message.text.startswith('https://www.youtube.com/') or message.text.startswith('https://youtu.be/') or message.text.startswith('http://youtube.com/') or message.text.startswith('http://youtu.be/'):
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
 
            btn_down = types.InlineKeyboardMarkup()
            btn_down.add(types.InlineKeyboardButton(text="Yuklanmoq", callback_data="download"))
            await message.answer_photo(f'{picture}', caption=f"📹 <b>{title}</b> <a href='{url}'>→</a> \n" #Title#
                                 f"👤 <b>{author}</b> <a href='{channel}'>→</a> \n" #Author Of Channel# 
                                 f"⚙️ <b>Kengayish —</b> <code>{resolution}</code> \n" ##
                                 f"🗂 <b>Video Hajmi —</b> <code>{round(file_size * 0.000001, 2)}MB</code> \n" #File Size#
                                 f"⏳ <b>Vaqti —</b> <code>{str(timedelta(seconds=length))}</code> \n" #Length#
                                 f"🗓 <b>Qoyilgan sana —</b> <code>{date_published}</code> \n" #Date Published#
                                 f"👁 <b>Korilganlar —</b> <code>{views:,}</code> \n", parse_mode='HTML', reply_markup=btn_down) #Views#
      else:
            await message.answer(f"❗️<b>Bu Url Orqali hechnima topilmadi!</b>", parse_mode='HTML')
            await state.finish()
            
            

@dp.callback_query_handler(text="download")
async def button_download(call: types.CallbackQuery,state: FSMContext):
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
            await state.finish()
            os.remove(f"{call.message.chat.id}/{call.message.chat.id}_{yt.title}")
    

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
    
    
#TARJIMON Кирил-Lotin #6
@dp.message_handler(text = "Кирил-Lotin",state="*")
async def kiril_lotin1(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("<b>Кирил tilidan Lotin tiliga o'tkazish uchun xabar yuboring...</b>",parse_mode='HTML')
    await kiril_lotin_kiril.to_lotin.set()
    
    
#TARJIMON Lotin-Кирил #7
@dp.message_handler(text = "Lotin-Кирил",state="*")
async def lotin_kiril1(message: types.Message,state: FSMContext):
    await state.finish()
    await message.answer("<b>Lotin тилидан Кирил тилига ўтказиш учун хабар юборинг...</b>",parse_mode='HTML')
    await kiril_lotin_kiril.to_kiril.set()

@dp.message_handler(state=kiril_lotin_kiril.to_lotin)
async def kiril_lotin2(message: types.Message,state: FSMContext):
    xabar = message.text
    if xabar.isascii():
        await message.answer(to_latin(xabar))
    else:
        await message.answer(to_latin(xabar))
        
    
    
@dp.message_handler(state=kiril_lotin_kiril.to_kiril)
async def lotin_kiril2(message: types.Message,state: FSMContext):
    xabar = message.text
    if xabar.isascii():
        await message.answer(to_cyrillic(xabar))
    else:
        await message.answer(to_cyrillic(xabar))

@dp.message_handler(state=tillar2.eng_uz)
async def eng_to_uz(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn = message.text
        translate = translator.translate(matn,dest='uz')
        pd.options.display.max_rows = 10000
        if len(translate.text) > 2000:
            for x in range(0, len(translate.text), 3000):
                await asyncio.sleep(0.05)
                await bot.send_message(message.chat.id, f"Matningizni tarjimasi 👇🏻\n\n<code>{translate.text[x:x + 2000]}</code>\n\n👨🏻‍💻 Bot creator: @azikk_0418",parse_mode='HTML')
                await state.finish()
        else:
            await bot.send_message(message.chat.id, f"Matningizni tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\n👨🏻‍💻 Bot creator: @azikk_0418",parse_mode='HTML')
            await state.finish()
    except:
        await message.answer("Oops😑 qandaydir xato ketdi ❌")
        await state.finish()

    

@dp.message_handler(state=tillar.uz_eng)
async def uz_eng1(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn = message.text
        translate = translator.translate(matn)
        pd.options.display.max_rows = 10000
        if len(translate.text) > 2000:
            for x in range(0, len(translate.text), 3000):
                await asyncio.sleep(0.05)
                await bot.send_message(message.chat.id, f"Matningizni tarjimasi 👇🏻\n\n<code>{translate.text[x:x + 2000]}</code>\n\n👨🏻‍💻 Bot creator: @azikk_0418",parse_mode='HTML')
                await state.finish()
        else:
            await bot.send_message(message.chat.id, f"Matningizni tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\n👨🏻‍💻 Bot creator: @azikk_0418",parse_mode='HTML')
            await state.finish()
    except:
        await message.answer("Oops😑 qandaydir xato ketdi ❌")
        await state.finish()
    

@dp.message_handler(state=tillar3.ru_uz)
async def ru_to_uz(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn = message.text
        translate = translator.translate(matn,dest='uz')
        pd.options.display.max_rows = 10000
        if len(translate.text) > 2000:
            for x in range(0, len(translate.text), 3000):
                await asyncio.sleep(0.05)
                await bot.send_message(message.chat.id, f"Matningizni tarjimasi 👇🏻\n\n<code>{translate.text[x:x + 2000]}</code>\n\n👨🏻‍💻 Bot creator: @azikk_0418",parse_mode='HTML')
                await state.finish()
        else:
            await bot.send_message(message.chat.id, f"Matningizni tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\n👨🏻‍💻 Bot creator: @azikk_0418",parse_mode='HTML')
            await state.finish()
    except:
        await message.answer("Oops😑 qandaydir xato ketdi ❌")
        await state.finish()


@dp.message_handler(state=tillar4.uz_ru)
async def uz_to_ru(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn2 = message.text
        translate = translator.translate(matn2,dest='ru')
        pd.options.display.max_rows = 10000
        if len(translate.text) > 2000:
            for x in range(0, len(translate.text), 3000):
                await asyncio.sleep(0.05)
                await bot.send_message(message.chat.id, f"Matningizni tarjimasi 👇🏻\n\n<code>{translate.text[x:x + 2000]}</code>\n\n👨🏻‍💻 Bot creator: @azikk_0418",parse_mode='HTML')
                await state.finish()
        else:
            await bot.send_message(message.chat.id, f"Matningizni tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\n👨🏻‍💻 Bot creator: @azikk_0418",parse_mode='HTML')
            await state.finish()
    except:
        await message.answer("Oops😑 qandaydir xato ketdi ❌")
        await state.finish()
        

    
@dp.message_handler(state=tillar5.hohlagan_til)
async def hohlagan_til_tarjima1(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn2 = message.text
        translate = translator.translate(matn2,dest='uz')
        pd.options.display.max_rows = 10000
        if len(translate.text) > 2000:
            for x in range(0, len(translate.text), 3000):
                await asyncio.sleep(0.05)
                await bot.send_message(message.chat.id, f"Matningizni tarjimasi 👇🏻\n\n<code>{translate.text[x:x + 2000]}</code>\n\n👨🏻‍💻 Bot creator: @azikk_0418",parse_mode='HTML')
                await state.finish()
        else:
            await bot.send_message(message.chat.id, f"Matningizni tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\n👨🏻‍💻 Bot creator: @azikk_0418",parse_mode='HTML')
            await state.finish()
    except:
        await message.answer("Oops😑 qandaydir xato ketdi ❌")
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
        jami = f"<b>Toshkent</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamatcoders'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
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
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamatcoders'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
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
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamatcoders'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
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
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamatcoders'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
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
        jami = f"<b>Xorazm</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamatcoders'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
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
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamatcoders'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
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
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamatcoders'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
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
        jami = f"<b>Surxondaryo</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamatcoders'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
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
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamatcoders'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
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
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamatcoders'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
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
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamatcoders'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
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
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamatcoders'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
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
        jami = f"<b>{city_name}</b> dagi ob-havo malumotlari🌤\n\n<code>\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat}</code>\n\n\nKanal <a href='https://t.me/azamatcoders'>Azamat's Blog</a> ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami,parse_mode='HTML',disable_web_page_preview=True)
        await state.finish()
    except:
        await message.answer((f"Davlatingiz yoki shaharingizni nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))
        await state.finish()