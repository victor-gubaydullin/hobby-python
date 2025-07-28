from aiogram.types import Message
from keyboards.interface_language import language_selection_keyboard
from keyboards.main_menu import main_menu_keyboard
from aiogram.fsm.context import FSMContext
from states.registration import Registration

async def process_start_command(state: FSMContext):
    reply_text = "Select interface language / Wählen Sie die Sprache / Выберите язык интерфейса:"
    reply_keyboard = language_selection_keyboard()

    await state.set_state(Registration.waiting_for_language)

    return reply_text, reply_keyboard

async def process_interface_language_selection(state: FSMContext):
    reply_text = "Language selected. You are now ready to use the bot."
    reply_keyboard = main_menu_keyboard()

    # TODO: Save language_code to DB or FSMContext

    await state.set_state(Registration.registration_complete)

    return reply_text, reply_keyboard