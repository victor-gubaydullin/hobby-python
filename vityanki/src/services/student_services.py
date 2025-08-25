from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from locales.translation import t
from db.data_utils import get_user_interface_language
from keyboards.wordset import wordset_main_menu_keyboard

async def handle_wordset_main_menu(callback: CallbackQuery, state: FSMContext):
    language_code = await get_user_interface_language(callback.from_user.id)
    
    reply_text = t(language_code, "wordset.messages.main_menu_message")
    reply_keyboard = wordset_main_menu_keyboard(language_code)

    return reply_text, reply_keyboard