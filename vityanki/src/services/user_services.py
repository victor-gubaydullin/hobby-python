from aiogram.types import CallbackQuery
from keyboards.interface_language import language_selection_keyboard
from keyboards.main_menu import main_menu_keyboard
from aiogram.fsm.context import FSMContext
from states.registration import Registration
from db.data_utils import set_user_interface_language

async def process_start_command(state: FSMContext):
    reply_text = "Select interface language / Wählen Sie die Sprache / Выберите язык интерфейса:"
    reply_keyboard = language_selection_keyboard()

    await state.set_state(Registration.waiting_for_language)

    return reply_text, reply_keyboard

async def process_interface_language_selection(callback: CallbackQuery, state: FSMContext):
    reply_text = "Language selected. You are now ready to use the bot."
    reply_keyboard = main_menu_keyboard()

    language_code = callback.data.split("_")[-1]
    telegram_id = callback.from_user.id
    await set_user_interface_language(telegram_id, language_code)

    await state.set_state(Registration.registration_complete)

    return reply_text, reply_keyboard