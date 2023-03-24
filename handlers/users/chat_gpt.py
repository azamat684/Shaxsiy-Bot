from loader import dp,bot 
import openai
from keyboards.default.defoultbutton import markup,chatni_yakunlash
from aiogram import types
from aiogram.dispatcher import FSMContext
from states.state import ChatGPT
import asyncio

########### ChatGPT Bot ##############

openai.api_key = "your_api_key"

def chat_with_gpt(messages):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    return completion.choices[0].message['content']

message_history=[]

##### ChatGpt START ######
@dp.message_handler(text='❌ Chatni yakunlash', state='*')
async def close_chat(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(text="<b>Siz chatni yakunladingiz\nMen sizni qiziqtirgan mavzu bo'yicha yordam berishim mumkin uning uchun yana ChatGPT bo'limiga qayting</b>", reply_markup=markup)


@dp.message_handler(text="🤖 ChatGPT",state="*")
async def chat_gpt_await(message: types.Message,state: FSMContext):
    await state.finish()
    await message.reply("Qiziqtirgan savolingiz bo'lsa menga yozishingiz mumkin,Men tez orada javob beraman!",reply_markup=chatni_yakunlash)
    await ChatGPT.start.set()
    
@dp.message_handler(state=ChatGPT.start)
async def chat_gpt_start(message: types.Message):
    stickers = ['⏳', '⌛️']
    msg = await message.answer(text=stickers[-1])
    msg_id = msg.message_id

    for sticker in stickers:
        await asyncio.sleep(3.1)
        await bot.edit_message_text(text=sticker, chat_id=message.chat.id, message_id=msg_id)
        
    user_message = message.text 

    message_history.append({"role":"user","content": user_message})

    responce = chat_with_gpt(message_history)

    message_history.append({"role": "assistant","content" : responce})
    
    await bot.delete_message(chat_id=message.chat.id, message_id=msg_id)
    await message.answer(text=responce)
    
