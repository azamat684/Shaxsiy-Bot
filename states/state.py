from aiogram.dispatcher.filters.state import State,StatesGroup

#/qrcode yasash uchun 
class qrcodee(StatesGroup):
    codee = State()
    
#Matnli xabarni ovozli xabarga aylantirish uchun    
class txt_to_voice(StatesGroup):
    voicee = State()

class txt_to_voice_ru(StatesGroup):
    speak_ru = State() 

class txt_to_voice_en(StatesGroup):
    speak_en = State() 
    
class txt_to_voice_es(StatesGroup):
    speak_es = State() 
    
class txt_to_voice_pt(StatesGroup):
    speak_pt = State() 
    
class txt_to_voice_fr(StatesGroup):
    speak_fr = State() 

class txt_to_voice_de(StatesGroup):
    speak_de = State()
    
class txt_to_voice_hi(StatesGroup):
    speak_hi = State() 

class txt_to_voice_tr(StatesGroup):
    speak_tr = State() 
    
class txt_to_voice_ar(StatesGroup):
    speak_ar = State()  
    
#Video yuklash uchun 
class video_yuklash_tiktok(StatesGroup):
    tiktok_1_qism = State()
    
class video_yuklash_insta(StatesGroup):
    insta_1_qism = State()
    
#Tarjimon uchun
class tillar2(StatesGroup):
    eng_uz = State()
    
class tillar(StatesGroup):
    uz_eng = State()

class tillar3(StatesGroup):
    ru_uz = State()
    
class tillar4(StatesGroup):
    uz_ru = State()
    
class tillar5(StatesGroup):
    hohlagan_til = State()
class kiril_lotin_kiril(StatesGroup):
    to_kiril = State()
    to_lotin = State()
#ChatGPT uchun
class ChatGPT(StatesGroup):
    start = State()
    
#Wikipedia uchun
class wikipediakuu(StatesGroup):
    uzz = State()

class wikipedia_ru(StatesGroup):
    ruu = State()
    
class wikipedia_eng(StatesGroup):
    engg = State()

#Youtubedan video yuklash uchun
class yt_video_save(StatesGroup):
    ytt = State()
  
#Ob_havo: hohlagan mintaqani ob havosini bilish uchun    
class Azamat(StatesGroup):
    boshlanish = State()

class pdf(StatesGroup):
    pdf_start = State()

#Faqat Admin Panel uchun 
class reklama(StatesGroup):
    reklamaa = State()
    
    

class uzmovii(StatesGroup):
    start = State()

class GameState(StatesGroup):
    sender_user = State()
    results = State()