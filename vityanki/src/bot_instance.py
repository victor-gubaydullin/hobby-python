import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

if not os.path.join(os.getcwd(), 'vityanki', 'variables.env'):
    raise FileNotFoundError("The 'variables.env' file is missing in the 'vityanki' directory.")
else:
    env_path = os.path.join(os.getcwd(), 'vityanki', 'variables.env')
    print(f"Loading environment variables from {env_path}")

load_dotenv(env_path)
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)