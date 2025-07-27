import asyncio
from aiogram import Dispatcher
from bot_instance import bot
from handlers.user_handlers import user_router

dp = Dispatcher(bot=bot)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    dp.include_router(user_router)
    asyncio.run(main())