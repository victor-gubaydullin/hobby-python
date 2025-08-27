from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from locales.translation import t
from db.data_utils import get_user_interface_language, get_user_flashcard_sets
from keyboards.flashcards import flashcards_main_menu_keyboard

async def process_flashcards_main_menu(callback: CallbackQuery, state: FSMContext):
    telegram_id = callback.from_user.id
    language_code = await get_user_interface_language(telegram_id)
    chunk_index = callback.data.rsplit("_", 1)[-1]

    user_flashcard_sets = await get_user_flashcard_sets(telegram_id)

    try:
        chunk_index = int(chunk_index)
    except ValueError:
        chunk_index = 0

    reply_text = t(language_code, "flashcards.messages.main_menu_message")
    reply_keyboard = flashcards_main_menu_keyboard(language_code=language_code, user_flashcard_sets=user_flashcard_sets, chunk_index=chunk_index)

    return reply_text, reply_keyboard