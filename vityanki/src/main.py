import asyncio
from aiogram import Dispatcher
from bot_instance import bot
from db.data_init import init_db
from handlers.user_handlers import user_router
from handlers.donator_handlers import donator_router
from pseudo_usage.pseudo_donators import create_pseudo_donators

dp = Dispatcher(bot=bot)

async def main():
    await init_db()
    
    # Create pseudo donators and donations for testing purposes
    # await create_pseudo_donators()
    
    dp.include_routers(user_router, donator_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())