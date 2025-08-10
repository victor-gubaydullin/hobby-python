from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from services.donator_services import process_donate_command

donator_router = Router()

@donator_router.callback_query(F.data == "donate")
async def donate_button_handler(callback: CallbackQuery, state: FSMContext):
    reply_text, reply_keyboard = await process_donate_command(callback, state)
    
    await callback.message.edit_text(reply_text, reply_markup=reply_keyboard)