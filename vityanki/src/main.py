import asyncio
from aiogram import Dispatcher
from bot_instance import bot

dp = Dispatcher(bot=bot)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())