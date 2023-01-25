from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


markup = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ro'yxatdan o'tish ✅")],
        [KeyboardButton(text="⛅️ Ob-Havo"),KeyboardButton(text="🌏 Wikipedia")],
        [KeyboardButton(text="🔄 Tarjimon"),KeyboardButton(text="📥 Video Yuklash")],
        [KeyboardButton(text="📥 Youtube"),KeyboardButton(text="👨🏻‍💻 Admin")]
        # [KeyboardButton(text="🔙Orqaga")]
        
        # [KeyboardButton(text="👨🏻‍💻ADMIN BN BOG'LANISH👨🏻‍💻")],
        # [KeyboardButton(text="🌐WIKIPEDIYA BO'LIMI🌐")],
        # [KeyboardButton(text="📥YOUTUBE VIDEO DOWNLOAD📥")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)




til = ReplyKeyboardMarkup(resize_keyboard=True)
til.add("Eng🇺🇸-Uz🇺🇿","Uz🇺🇿-Eng🇺🇸")
til.add("Ru🇷🇺-Uz🇺🇿","Uz🇺🇿-Ru🇷🇺")
til.add(KeyboardButton(text="🔙Orqaga"))



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
wiki_til.add(KeyboardButton(text="Русский🇷🇺"))
wiki_til.add(KeyboardButton(text="O'zbek🇺🇿"),KeyboardButton(text="English🇺🇸"))
wiki_til.add(KeyboardButton(text="🔙Orqaga"))
