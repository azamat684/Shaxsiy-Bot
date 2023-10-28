from loader import dp,bot 
import openai
from keyboards.default.defoultbutton import markup,chatni_yakunlash
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.state import ChatGPT
import asyncio
from data.config import openai_apikey

########### ChatGPT Bot ##############

openai.api_key = openai_apikey

def chat_with_gpt(messages):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-16k",
        messages=messages,
        temperature=0.7
    )
    return completion.choices[0].message['content']

message_history=[]

##### ChatGpt START ######
@dp.message_handler(text='❌ Chatni yakunlash', state='*')
async def close_chat(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text="Siz chatni yakunladingiz\nMen sizni qiziqtirgan mavzu bo'yicha yordam berishim mumkin uning uchun yana ChatGPT bo'limiga qayting", reply_markup=markup)



    
@dp.message_handler(state=ChatGPT.start)
async def chat_gpt_start(message: types.Message):
    await message.answer_chat_action(action='typing')
    stickers = ['⏳', '⌛️']
    msg = await message.answer(text=stickers[-1])
    msg_id = msg.message_id

    for sticker in stickers:
        await asyncio.sleep(3.0)
        await bot.edit_message_text(text=sticker, chat_id=message.chat.id, message_id=msg_id)
    await message.answer_chat_action(action='typing')
    try:
        await message.answer_chat_action(action='typing')
        user_message = message.text 
        await message.answer_chat_action(action='typing')
        message_history.append({"role":"user","content": user_message})

        responce = chat_with_gpt(message_history)
        await message.answer_chat_action(action='typing')
        message_history.append({"role": "assistant","content" : responce})
        await message.answer_chat_action(action='typing')
        await bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
        await message.answer(text=responce)
    except Exception:
        await bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
        await message.answer("Nimadir xato ketdi keyinroq qayta urining",reply_markup=markup)