from aiogram import Dispatcher, Bot
from os import getenv

API_TOKEN = str(getenv("API_TOKEN"))
dp = Dispatcher(bot=Bot(...))


