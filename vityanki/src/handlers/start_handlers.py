from bot_instance import bot, dp
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio

@dp.message(CommandStart())
async def start_handler(message: Message):
    pass
    # ... await message.answer("Select interface language / Wähle Sie die Sprache / Выберите язык интерфейса:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())