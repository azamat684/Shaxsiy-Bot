from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

inline_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Tik Tok",callback_data="tik_tok"),InlineKeyboardButton(text="Instagram",callback_data="instagram"),InlineKeyboardButton(text="🎬 Uzmovi",callback_data="uzmovi_down")],
    [InlineKeyboardButton(text='🏠 Asosiy menyu', callback_data='txt_voice_back2')]
])

back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="↩️ Orqaga",callback_data='back')]
])

back_from_history = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏠 Asosiy menyu",callback_data='back_from_history'),InlineKeyboardButton(text="More...",callback_data='more_info')]
])

back_from_history_to_home = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏠 Asosiy menyu",callback_data='back_from_history')]
])

jokes_lang = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🇺🇸 English",callback_data='joke_en'),InlineKeyboardButton(text="🇺🇿 O'zbek",callback_data='joke_uz')],
    [InlineKeyboardButton(text="🇷🇺 Pусский",callback_data='joke_ru')]
])
reaction_jokes = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="😐",callback_data='😐'),InlineKeyboardButton(text="🙂",callback_data='🙂'),InlineKeyboardButton(text="😂",callback_data='😂')],
    [InlineKeyboardButton(text="↩️ Orqaga",callback_data='back_jokes'),InlineKeyboardButton(text="🆕 Yangisi",callback_data='new_joke')]
])
back_jokes = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="↩️ Orqaga",callback_data='back_jokes'),InlineKeyboardButton(text="🆕 Yangisi",callback_data='new_joke')]
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

admin_panels_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👥 Count all users",callback_data='count_users'),InlineKeyboardButton(text="➕ Send advertise",callback_data='send_advertise')],
    [InlineKeyboardButton(text="")]
])

button_for_history = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🫳🏿 Bilish ✔️",callback_data='bilish_history')]
])


results_markup = InlineKeyboardMarkup(row_width=1)
results_markup.insert(InlineKeyboardButton(text='Natijalar', callback_data='results'))

def continue_markup(winner: str):
    markup = InlineKeyboardMarkup(row_width=1)
    if winner == 'user':
        text = "Yutishda davom etaman"
    elif winner == 'bot':
        text = 'Botni yutaman'
    else:
        text = "Yana o'ynayman"
    markup.insert(InlineKeyboardButton(text=text, callback_data='continue'))
    return markup