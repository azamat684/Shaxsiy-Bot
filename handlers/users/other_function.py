import asyncio
from .uzmovi_downloader11 import downloader_uzmovi
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db
from states.state import GameState, uzmovii
from keyboards.inline.inline_button import continue_markup, results_markup,button_for_history,back_from_history, back_from_history_to_home
from keyboards.default.defoultbutton import stickers_markup,markup
import requests
from googletrans import Translator
import pandas as pd
from loader import bot

@dp.message_handler(text="🤖 Games", state="*")
async def start_other(message: types.Message,state: FSMContext):
    await message.answer("Menga quyidagi emojilardan birini jo'nating ikkimiz bahslashamiz qani kim yutadi ekan?! 😅😉",reply_markup=stickers_markup)
    await GameState.sender_user.set()




@dp.message_handler(content_types=['dice'], state=GameState.sender_user)
async def bot_echo(message: types.Message):
    user_score = int(message.dice.value)
    emoji = message.dice.emoji
    dice = await message.answer_dice(emoji=emoji)
    bot_score = dice.dice.value

    await asyncio.sleep(5)
    if bot_score and user_score:
        if bot_score > user_score:
            await message.answer(text="Men yutdim!", reply_markup=results_markup)
            db.add_game(user_id=message.from_user.id, winner='bot')
        elif user_score > bot_score:
            await message.answer(text='Siz yutdingiz!', reply_markup=results_markup)
            db.add_game(user_id=message.from_user.id, winner='user')
        else:
            await message.answer(text='Durrang!', reply_markup=results_markup)
            db.add_game(user_id=message.from_user.id, winner='tie')


@dp.message_handler(commands=['results'], state='*')
async def get_results(message: types.Message, state: FSMContext):
    await state.finish()
    games = db.select_all_games(user_id=message.from_user.id)
    user_result = 0
    bot_result = 0
    tie_result = 0
    for game in games:
        if game['winner'] == 'user':
            user_result += 1
        elif game['winner'] == 'bot':
            bot_result += 1
        else:
            tie_result += 1
    if max(user_result, bot_result, tie_result) == user_result:
        winner = 'user'
    elif max(user_result, bot_result, tie_result) == bot_result:
        winner = 'bot'
    elif max(user_result, bot_result, tie_result) == tie_result:
        winner = 'tie'
    await message.answer(text=f"Natijalar", reply_markup=types.ReplyKeyboardRemove())
    await message.answer(text=f"{user_result} marta yutdingiz!😎\n{bot_result} marta yutqazdingiz!😌\n{tie_result} marta durrang!😉\n\nO'ynashda davom etamizmi?🤨", reply_markup=continue_markup(winner=winner))
    await GameState.results.set()

@dp.callback_query_handler(text='results', state='*')
async def get_results_in_game(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    games = db.select_all_games(user_id=call.from_user.id)
    print(games)
    user_result = 0
    bot_result = 0
    tie_result = 0
    for game in games:
        if game['winner'] == 'user':
            user_result += 1
        elif game['winner'] == 'bot':
            bot_result += 1
        else:
            tie_result += 1
    if max(user_result, bot_result, tie_result) == user_result:
        winner = 'user'
    elif max(user_result, bot_result, tie_result) == bot_result:
        winner = 'bot'
    elif max(user_result, bot_result, tie_result) == tie_result:
        winner = 'tie'
    await call.message.answer(text=f"Natijalar", reply_markup=types.ReplyKeyboardRemove())
    await call.message.answer(text=f"{user_result} marta yutdingiz!😎\n{bot_result} marta yutqazdingiz!😌\n{tie_result} marta durrang!😉\n\nO'ynashda davom etamizmi?🤨", reply_markup=continue_markup(winner=winner))
    await GameState.results.set()

@dp.callback_query_handler(state=GameState.results)
async def continue_game(call: types.CallbackQuery):
    if call.data == 'continue':
        await call.message.answer(text="O'yinni davom ettirish uchun quyidagi stikerlardan birini menga yuboring!", reply_markup=stickers_markup)
        await GameState.sender_user.set()
        
        
        
        
@dp.callback_query_handler(text="uzmovi_down",state="*")
async def uzmovi12(call: types.CallbackQuery):
    await call.message.answer("send url...")
    await uzmovii.start.set()

@dp.message_handler(state=uzmovii.start)
async def uzmovi123(message: types.Message, state: FSMContext):
    urls = message.text
    try:
        print('salom')
        hrefs = [url for url in urls.split('\n') if 'YUKLAB OLISH' in url]
        for href in hrefs:
            print('salom2')
            await message.answer_video(video=downloader_uzmovi(url=href))
        await state.finish()
    except Exception as pr:
        print(pr)
        

#History
# #What happen this date in history
@dp.message_handler(text='✨ Tarix',state="*")
async def history(message: types.Message, state: FSMContext):
    await message.answer(f"<b>{message.text} bo'limigi xush kelibsiz 😊</b>\nBu bo'limda siz aynan bugungi sanada tarixda nimalar bo'lganini bilib olasiz!\n\nBilish uchun bosing 👇🏿!",
                         reply_markup=button_for_history)
    

def history_das(start,stop):
    api_url = "https://history.muffinlabs.com/date"
    response = requests.get(api_url)
    translator = Translator()
    if response.status_code == 200:
        data = response.json()
        events = data["data"]["Events"]
        
        
        all = ""
        for event in events[start:stop]:
            try:
                malumotlar = translator.translate(event['text'],dest='uz')
                content = str(event['year']) + " - " + str(malumotlar.text) + '\n'
                all += content
            
            except Exception as er:
                print(er)
                
        return all
    else:
        return str()
    
    
    
@dp.callback_query_handler(text='bilish_history',state="*")
async def history_bilish(call: types.CallbackQuery, state: FSMContext):
    
# API ni istalgan joydan oling (masalan, History API)
    await call.message.delete()
    await call.message.answer_chat_action(action='typing')
    data = history_das(start=0, stop=25)
    if data:
        await call.message.answer(text=f"Bugungi kun tarixda sodir bo'lgan voqealar\n{data}\n",reply_markup=back_from_history)
    else:
        await call.message.answer(text="Ma'lumotlarni olishda xatolik sodir bo'ldi.", reply_markup=back_from_history)

@dp.callback_query_handler(text='more_info',state="*")
async def history_bilish_more(call: types.CallbackQuery, state: FSMContext):
    data = history_das(start=20,stop=45)
    if data:
        await call.message.edit_text(text=f"Bugungi kun tarixda sodir bo'lgan voqealar\n{data}\n",reply_markup=back_from_history_to_home)
      
    else:
        await call.message.edit_text(text="Ma'lumotlarni olishda xatolik sodir bo'ldi.", reply_markup=back_from_history_to_home)

@dp.callback_query_handler(text='back_from_history',state="*")
async def history_to_home(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("🏠 Asosiy menyu", reply_markup=markup)
    await state.finish()
    
    
    
    