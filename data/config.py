from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()


# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
CHANNELS = env.list("CHANNELS") #kanallar ro'yxati
openai_apikey = env.str('openai_apikey') #your openai_apikey
