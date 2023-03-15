from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ro'yxatdan o'tish ✅"),KeyboardButton(text="💬 Text to Voice 🗣")],
        [KeyboardButton(text="⛅️ Ob-Havo"),KeyboardButton(text="🌏 Wikipedia")],
        [KeyboardButton(text="🔄 Tarjimon"),KeyboardButton(text="📥 Video Yuklash")],
        [KeyboardButton(text="📥 Youtube"),KeyboardButton(text="👨🏻‍💻 Admin")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)




til = ReplyKeyboardMarkup(resize_keyboard=True)
til.add(KeyboardButton(text="🔙Orqaga"),KeyboardButton(text="?-Uz 🇺🇿"))
til.add("Eng🇺🇸-Uz🇺🇿","Uz🇺🇿-Eng🇺🇸")
til.add("Ru🇷🇺-Uz🇺🇿","Uz🇺🇿-Ru🇷🇺")




shaharlar = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
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
wiki_til.add(KeyboardButton(text="O'zbek 🇺🇿"),KeyboardButton(text="Русский 🇷🇺"))
wiki_til.add(KeyboardButton(text="English 🇺🇸"))
wiki_til.add(KeyboardButton(text="🔙Orqaga"))
