from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from services.user_services import process_start_command

user_router = Router()

@user_router.message(CommandStart())
async def start_command_handler(message: Message):
    reply_text, reply_keyboard = await process_start_command()

    await message.answer(reply_text, reply_markup=reply_keyboard)
