from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from services.student_services import process_flashcards_main_menu

student_router = Router()

@student_router.callback_query(F.data.startswith("flashcards_main_menu"))
async def flashcards_main_menu_handler(callback: CallbackQuery, state: FSMContext):
    
    reply_text, reply_keyboard = await process_flashcards_main_menu(callback, state)

    await callback.message.edit_text(reply_text, reply_markup=reply_keyboard)
    await callback.answer()