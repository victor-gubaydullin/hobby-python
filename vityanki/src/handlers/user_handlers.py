from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from services.user_services import process_start_command, process_interface_language_selection

user_router = Router()

@user_router.message(CommandStart())
async def start_command_handler(message: Message, state: FSMContext):
    reply_text, reply_keyboard = await process_start_command(state)

    await message.answer(reply_text, reply_markup=reply_keyboard)

@user_router.callback_query(F.data.startswith("interface_language"))
async def interface_language_selection_handler(callback: CallbackQuery, state: FSMContext):
    reply_text, reply_keyboard = await process_interface_language_selection(state)

    await callback.message.edit_text(reply_text, reply_markup=reply_keyboard)
    await callback.answer()