import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from config import load_config
from logger import setup_logging

config = load_config()
logger = setup_logging('bot_instance')

bot = Bot(token=config.TOKEN)
logger.info("Bot instance created with token from config.")

dp = Dispatcher(bot=bot)
logger.info("Dispatcher initialized with the bot instance.")