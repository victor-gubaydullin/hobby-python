import asyncio
from aiogram import Dispatcher
from bot_instance import bot
from db.data_init import init_db
from handlers.user_handlers import user_router
from handlers.donator_handlers import donator_router

dp = Dispatcher(bot=bot)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    init_db()
    dp.include_routers(user_router, donator_router)
    asyncio.run(main())