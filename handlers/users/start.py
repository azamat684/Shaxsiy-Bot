import sqlite3
import wikipedia 
import requests
from googletrans import Translator
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import executor
from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.defoultbutton import markup,shaharlar,wiki_til,registratsiya,til
from data.config import CHANNELS
from keyboards.inline.inline_button import inline_markup,back
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from downloader import tk
from insta import instadownloader
from states.state import video_yuklash_tiktok,video_yuklash_insta,ob_havo_lyuboi_joy,tillar
from aiogram.dispatcher import FSMContext

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # markup = InlineKeyboardMarkup(row_width=1)
    # channels_format = str()
    # for channel in CHANNELS:
    #     chat = await bot.get_chat(channel)
    #     invite_link = await chat.export_invite_link()
    #     markup.insert(InlineKeyboardButton(text=chat.title, url=invite_link))
    #     channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}</b></a>\n"
    # markup.insert(InlineKeyboardButton(text="✅ Obunani tekshirish", callback_data="check_subs"))
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,name=name)
        await message.answer(f"Xush kelibsiz! {name}", reply_markup=markup)
        # Adminga xabar beramiz
        count = db.count_users()[0]
        msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)

    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{name} bazaga oldin qo'shilgan")
        await message.answer(f"Xush kelibsiz! {name}", reply_markup=markup)






########################################################################################################


@dp.message_handler(text = "⛅️ Ob-Havo")
async def ob_havo(message: types.Message):
    await message.answer("Pastdan menyular orqali viloyatingizni tanlang ✅",reply_markup=shaharlar)

@dp.message_handler(text = "Ro'yxatdan o'tish ✅")
async def reg(message: types.Message):
    await message.answer(f"Telefon raqaminggizni jo'nating!\n\nPastda menyuda <b>'📞 Telefon Raqamni jo'natish'</b> tugmasi bor o'shani bosing",parse_mode='HTML',reply_markup=registratsiya)
@dp.message_handler(content_types='contact')
async def kantakt(message: types.Message):
    # kantakt_user = message.contact.phone_number
    # db.add_user(phone_number=kantakt_user)
    await message.answer(f"Sizni raqaminggiz muvvofaqiyatli saqlandi",reply_markup=markup)

@dp.message_handler(text = "🌏 Wikipedia")
async def wikipediaa(message: types.Message):
    await message.answer("Pastdan o'zinggizga kerakli tilni tanlang💁🏻‍♂️",reply_markup=wiki_til)

@dp.message_handler(text = "English🇺🇸")
async def wiki_eng(message: types.Message):
    await message.reply("Menga biror so'z yuboring men u haqida malumot chiqaraman (Agar menda bor bo'lsa)")
    @dp.message_handler(content_types=['text'])
    async def wiki_eng(message: types.Message):
            matn = message.text
            w = wikipedia.summary(matn)
            await message.answer(w)

@dp.message_handler(text = "📥 Video Yuklash",state='*')
async def vd_yuk(message: types.Message):
    await message.answer("Qaysi ishtimoiy tarmoqdan video yuklamoqchisiz?",reply_markup=inline_markup)



@dp.callback_query_handler(text="tik_tok")
async def tik_tok(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<b>Yuklamoqchi bo'lgan videongizni url manzilini yuboring</b>",parse_mode='HTML',reply_markup=back)
   
    @dp.message_handler(content_types=['text'])
    async def insta_down(message: types.Message):
        try:
            u = message.text
            natija = tk(url1=u)
            text1 = message.text
            if text1.startswith("https://vm.tiktok.com/" and "https://vt.tiktok.com/"):
                await message.answer("<b><i>Iltimos biroz kuting video yuklanmoqda</i></b>",parse_mode='HTML')
                await message.answer_video(natija['video'],caption="<b>@for_testing_py_bot orqali yuklandi 📥</b>",parse_mode='HTML')
                # await state.finish()
            elif text1.startswith("https://www.tiktok.com/"):
                await message.answer("<b><i>Iltimos biroz kuting video yuklanmoqda</i></b>",parse_mode='HTML')
                await message.answer_video(natija['video'],caption="<b>@for_testing_py_bot orqali yuklandi 📥</b>",parse_mode='HTML')
                # await state.finish()
            else:
                await message.answer("Url manzili xato")
                # await state.finish()
        except:
            await message.answer("<b>Menga faqat <i>Tik Tok</i> videoni havolasini jo'nating</b> ",parse_mode='HTML') 
        # await state.finish()
    

@dp.callback_query_handler(text='instagram')
async def insta_vd(call: types.CallbackQuery,state: FSMContext):
    await call.message.edit_text("<b>Yuklamoqchi bo'lgan videongizni url manzilini yuboring</b>",parse_mode='HTML',reply_markup=back)
    # await video_yuklash_insta.next()

    @dp.message_handler(content_types=['text'])
    async def insta_fayl(message: types.Message,state: FSMContext):
        try:
            link = message.text
            data = instadownloader(link=link)
            if data == 'Bad':
                await message.answer("Hech narsa topolmadim")
                # await state.finish()
            else:
                if data['type'] == 'image':
                    await message.answer_photo(photo=data['media'],caption=f"<b>@for_testing_py_bot orqali yuklandi</b>",parse_mode='HTML')
                    # await state.finish()
                elif data['type'] == 'video':
                    await message.answer_video(video=data['media'],caption="<b>@for_testing_py_bot orqali yuklandi</b>",parse_mode='HTML')
                    # await state.finish()
                elif data['type'] == 'carousel':
                    for i in range(data['media']):
                        await message.answer_document(document=i,caption="<b>@for_testing_py_bot orqali yuklandi</b>",parse_mode='HTML')
                        # await state.finish()
                else:
                    await message.answer("<b>Bu url manzil bo'yicha hech narsa topolmadim</b>")
                    # await state.finish()
        except:
            await message.answer("<b>Menga faqat <i>Instagramdagi</i> videoni havolasini jo'nating</b> ",parse_mode='HTML')
            # await state.finish()

@dp.callback_query_handler(text = 'back')
async def orqagaa(call: types.CallbackQuery):
    await call.message.edit_text("Qaysi ishtimoiy tarmoqdan video yuklamoqchisiz?",reply_markup=inline_markup)





@dp.message_handler(text = "👨🏻‍💻 Admin")
async def admin1_bot(message: types.Message):
    await message.answer("Salom!\nBot admini: <b>Azamat Do'smukhambetov</b>\n\n<i>Taklif yoki bot bo'yicha shikoyatinggiz bo'lsa @azikk_0418 ga murojat qilishinggiz mumkin </i>\n<strong>Bizning botdan foydalanayotganinggiz uchun raxmat😊</strong>",parse_mode='HTML')

@dp.message_handler(text = "🔙Orqaga")
async def reg(message: types.Message):
    await message.answer("◻️Bosh menyuga qaytdinggiz\n🟢Pastdagi menyulardan o'zinggizga keragini tanlang!",reply_markup=markup)

@dp.message_handler(text="🔄 Tarjimon")
async def tarjimon(message: types.Message):
    await message.answer("<b>⚠️OGOHLANTIRISH\nBu funksiya hali yaxshi ishlamaydi biroz vaqtdan so'ng albatda tuzatamiz etiboringgiz uchun raxmat</b>",parse_mode='HTML')
    await message.answer("Qaysi tildan qaysi tilga tarjima qilmoqchi bo'lsez pastdan menyudan tanlang!",reply_markup=til)

#TARJIMON ENG-UZ #1
@dp.message_handler(text="Eng🇺🇸-Uz🇺🇿")
async def eng_uz(message: types.Message):
    await message.answer("Tarjima qilmoqchi bo'lgan so'zinggizni yuboring")
    @dp.message_handler(content_types=['text'])
    async def eng_to_uz(message: types.Message):
        try:
            translator = Translator()
            matn = message.text
            translate = translator.translate(matn,src='en',dest='uz')
            await message.answer(f"{message.text} ni o'zbekchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        except:
            await message.answer("Xato😑\nSiz boshqa tilda matn yubordinggiz❌")

@dp.message_handler(text="📥 Youtube")
async def eng_uz(message: types.Message):
    await message.answer("Hali bu funksiya ishga tushmagan😣")

#TARJIMON UZ-ENG #2
@dp.message_handler(text="Uz🇺🇿-Eng🇺🇸",state=tillar.uz_eng)
async def eng_uz(message: types.Message):
    await message.answer("Tarjima qilmoqchi bo'lgan so'zinggizni yuboring")
    await til.next()
@dp.message_handler(state=tillar.uz_eng_2)
async def eng1_to_uz(message: types.Message,state: FSMContext):
    try:
        translator = Translator()
        matn = message.text
        translate = translator.translate(matn)
        await message.answer(f"{message.text} ni inglizchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        await state.finish()
    except:
        await message.answer("Xato")
        state.finish()
    
#TARJIMON RU-UZ #3
@dp.message_handler(text="Ru🇷🇺-Uz🇺🇿")
async def eng_uz(message: types.Message):
    await message.answer("Tarjima qilmoqchi bo'lgan so'zinggizni yuboring")
    @dp.message_handler(content_types=['text'])
    async def eng_to_uz(message: types.Message):
        try:
            translator = Translator()
            matn = message.text
            translate = translator.translate(matn,dest='uz')
            await message.answer(f"{message.text} ni o'zbekchaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        except:
            await message.answer("Xato😑\nSiz boshqa tilda matn yubordinggiz❌")
#TARJIMON UZ-RU #4
@dp.message_handler(text="Uz🇺🇿-Ru🇷🇺")
async def eng_uz(message: types.Message):
    await message.answer("Tarjima qilmoqchi bo'lgan so'zinggizni yuboring")
    @dp.message_handler(content_types=['text'])
    async def eng_to_uz(message: types.Message):
        try:
            translator = Translator()
            matn = message.text
            translate = translator.translate(matn,src='uz',dest='ru')
            await message.answer(f"{message.text} ni ruschaga tarjimasi 👇🏻\n\n<code>{translate.text}</code>\n\nBot creator👨🏻‍💻: @azikk_0418",parse_mode='HTML')
        except:
            await message.answer("Xato😑\nSiz boshqa tilda matn yubordinggiz❌")


@dp.message_handler(text='Toshkent')
async def toshkent_ob_havo(message: types.Message):
    try:
        city_name = "Toshkent"
        sayt_api = "0470ec5dfb0b856ad6d7215a1a42136b"
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={sayt_api}&units=metric"
        response = requests.get(url).json()
        harorat = response['main']['temp']
        namlik = response['main']['humidity']
        yuqori_harorat = response['main']['temp_max']
        pas_harorat = response['main']['temp_min']
        bosim = response['main']['pressure']
        jami = f"{city_name} dagi ob-havo malumotlari🌤\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat} \n\n Kanal t.me/azamat_dosmukhambetov_fans ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami)
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
        jami = f"{city_name} dagi ob-havo malumotlari🌤\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat} \n\n Kanal t.me/azamat_dosmukhambetov_fans ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
    
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
        jami = f"{city_name} dagi ob-havo malumotlari🌤\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat} \n\n Kanal t.me/azamat_dosmukhambetov_fans ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami)
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
        jami = f"{city_name} dagi ob-havo malumotlari🌤\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat} \n\n Kanal t.me/azamat_dosmukhambetov_fans ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami)
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
        jami = f"Xorazm dagi ob-havo malumotlari🌤\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat} \n\n Kanal t.me/azamat_dosmukhambetov_fans ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami)
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
        jami = f"{city_name} dagi ob-havo malumotlari🌤\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat} \n\n Kanal t.me/azamat_dosmukhambetov_fans ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami)
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
        jami = f"{city_name} dagi ob-havo malumotlari🌤\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat} \n\n Kanal t.me/azamat_dosmukhambetov_fans ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami)
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
        jami = f"Surxondaryo dagi ob-havo malumotlari🌤\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat} \n\n Kanal t.me/azamat_dosmukhambetov_fans ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami)
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
        jami = f"{city_name} dagi ob-havo malumotlari🌤\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat} \n\n Kanal t.me/azamat_dosmukhambetov_fans ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami)
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
        jami = f"{city_name} dagi ob-havo malumotlari🌤\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat} \n\n Kanal t.me/azamat_dosmukhambetov_fans ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami)
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
        jami = f"{city_name} dagi ob-havo malumotlari🌤\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat} \n\n Kanal t.me/azamat_dosmukhambetov_fans ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami)
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
        jami = f"{city_name} dagi ob-havo malumotlari🌤\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat} \n\n Kanal t.me/azamat_dosmukhambetov_fans ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
        await message.answer(jami)
    except:
        await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))


@dp.message_handler(text="Hohlagan davlatni ob-havosin bilish")
async def ob(message: types.Message):
    await message.reply("Qayerni ob havosi bo'yicha malumot kerak men sizga malumot beraman hududni nomini to'g'ri yozsanggiz albatta😊\nHudud nomini kiriting?")
    @dp.message_handler(content_types=['text'])
    async def ob_havo_lyuboi_joy(message: types.Message):
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
            jami = f"{city_name} dagi ob-havo malumotlari🌤\n🙂Harorat: {harorat} gradus\n☁️Namlik: {namlik}%\n😶Bosim: {bosim}\n☀️Yuqori harorat: {yuqori_harorat}\n🥶Pas harorat: {pas_harorat} \n\n Kanal t.me/azamat_dosmukhambetov_fans ✅🔰\nBot creator👨🏻‍💻: @azikk_0418"
            await message.answer(jami)
        except:
            await message.answer((f"Davlatlar yoki shaharlar nomini tekshirib takroran yuboring yoki menda {city_name} xaqida malumot yo'q uzr!"))


