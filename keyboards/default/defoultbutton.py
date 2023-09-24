from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Register"),KeyboardButton(text="🔄 Tarjimon")],
        [KeyboardButton(text="🏞 Rasmni PDF qilish 📁"),KeyboardButton(text='😂 Jokes')],
        [KeyboardButton(text="⛅️ Ob-Havo"),KeyboardButton(text="🌏 Wikipedia")],
        [KeyboardButton(text="💬 Matnni Ovozli xabar qilish 🗣")],
        [KeyboardButton(text="📥 Video Yuklash"),KeyboardButton(text="👨🏻‍💻 Dasturchi")],
        [KeyboardButton(text="📥 Youtube"),KeyboardButton(text="🤖 ChatGPT")],
        [KeyboardButton(text="🤖 Games"),KeyboardButton(text="Uzmovi")]
    ],
    resize_keyboard=True
)


chatni_yakunlash = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="❌ Chatni yakunlash")]
],resize_keyboard=True)



til = ReplyKeyboardMarkup(resize_keyboard=True)
til.add(KeyboardButton(text="🔙Orqaga"),KeyboardButton(text="?-Uz 🇺🇿"))
til.add("Eng🇺🇸-Uz🇺🇿","Uz🇺🇿-Eng🇺🇸")
til.add("Ru🇷🇺-Uz🇺🇿","Uz🇺🇿-Ru🇷🇺")
til.add("Кирил-Lotin","Lotin-Кирил")




shaharlar = ReplyKeyboardMarkup(resize_keyboard=True)
shaharlar.row("Toshkent","Qashqadaryo")
shaharlar.row("Buxoro","Navoiy")
shaharlar.row("Samarqand","Jizzax")
shaharlar.row("Xorazm","Nukus")
shaharlar.row("Andijon","Namangan")
shaharlar.row("Farg'ona","Surxondaryo")
shaharlar.row("Hohlagan davlatni ob-havosin bilish")
shaharlar.row("🔙Orqaga")


registratsiya = ReplyKeyboardMarkup(resize_keyboard=True)
registratsiya.add(KeyboardButton(text="📞 Telefon Raqamni jo'natish",request_contact=True))
registratsiya.add(KeyboardButton(text="🔙Orqaga"))

wiki_til = ReplyKeyboardMarkup(resize_keyboard=True)
wiki_til.add(KeyboardButton(text="🔙Orqaga"),KeyboardButton(text="O'zbek 🇺🇿"))
wiki_til.add(KeyboardButton(text="English 🇺🇸"),KeyboardButton(text="Русский 🇷🇺"))



stickers_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
stickers_markup.insert(KeyboardButton(text='🎲'))
stickers_markup.insert(KeyboardButton(text='🎯'))
stickers_markup.insert(KeyboardButton(text='🏀'))
stickers_markup.insert(KeyboardButton(text='⚽'))
stickers_markup.insert(KeyboardButton(text='🎰'))
stickers_markup.insert(KeyboardButton(text='🎳'))