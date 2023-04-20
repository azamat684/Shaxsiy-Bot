from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

inline_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Tik Tok",callback_data="tik_tok"),InlineKeyboardButton(text="Instagram",callback_data="instagram")],
    [InlineKeyboardButton(text='🏠 Asosiy menyu', callback_data='txt_voice_back2')]
])

back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="↩️ Orqaga",callback_data='back')]
])


txt_to_voice_lang = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="❌ O'zbek",callback_data='uz'),InlineKeyboardButton(text="Rus Tili",callback_data='ru')],
    [InlineKeyboardButton(text="Ingliz Tili",callback_data="en"),InlineKeyboardButton(text="Ispan Tili",callback_data="es")],
    [InlineKeyboardButton(text="Portugal",callback_data="pt"),InlineKeyboardButton(text="Frantsuz Tili",callback_data='fr')],
    [InlineKeyboardButton(text="Nemis Tili",callback_data="de"),InlineKeyboardButton(text="Hind Tili",callback_data='hi')],
    [InlineKeyboardButton(text="Turk Tili",callback_data='tr'),InlineKeyboardButton(text="Arab Tili",callback_data="ar")],
    [InlineKeyboardButton(text='↩️ Asosiy menyuga qaytish', callback_data='txt_voice_back2')]
])

txt_to_voice_back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="↩️ Tilni o'zgartirish",callback_data='txt_voice_back')]
])

pdf_uchun_btn = InlineKeyboardMarkup(row_width=1)
pdf_uchun_btn.add(InlineKeyboardButton(text="🔄 Ha PDF qilaver",callback_data='make_pdf'))
pdf_uchun_btn.add(InlineKeyboardButton(text='❌ Bekor qilish',callback_data='otmen_pdf'))
"""
share_button = InlineKeyboardMarkup(row_width=1)
share_button.add(InlineKeyboardButton(text='Ulashish', switch_inline_query=''))
"""