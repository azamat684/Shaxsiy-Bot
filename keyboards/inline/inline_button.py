from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

inline_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Tik Tok",callback_data="tik_tok"),InlineKeyboardButton(text="Instagram",callback_data="instagram")]
])

back = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="◀️ Orqaga",callback_data='back')]
])