from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.sqlite import Database
from data import config
import psycopg2

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database(path_to_db="C:/Users/Kazbek/Desktop/MY AIOGRAM BOTS/Shaxsiy-Bot/data/main.db")
# db = Database(dbname="data/main.db", user="azamat", password="azamat1234", host="localhost", port="5432")
