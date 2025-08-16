from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states.registration import Registration
from states.settings import InterfaceLanguage
from locales.translation import t
from keyboards.interface_language import language_selection_keyboard
from keyboards.main_menu import main_menu_keyboard
from keyboards.settings import settings_keyboard
from keyboards.about import about_keyboard
from db.data_utils import set_user_interface_language, get_user_interface_language

async def get_language_selection_prompt():
    reply_text = "Select interface language / Wählen Sie die Sprache / Выберите язык интерфейса:"
    reply_keyboard = language_selection_keyboard()

    return reply_text, reply_keyboard

async def process_start_command(state: FSMContext):
    reply_text, reply_keyboard = await get_language_selection_prompt()
    await state.set_state(Registration.waiting_for_language)

    return reply_text, reply_keyboard

async def process_settings_language_selection(state: FSMContext):
    reply_text, reply_keyboard = await get_language_selection_prompt()
    await state.set_state(InterfaceLanguage.waiting_for_language)

    return reply_text, reply_keyboard

async def process_interface_language_selection(callback: CallbackQuery, state: FSMContext):
    language_code = callback.data.split("_")[-1]
    telegram_id = callback.from_user.id
    
    await set_user_interface_language(telegram_id, language_code)
    await state.clear()

    reply_text = t(language_code, "registration.language_selected")
    reply_keyboard = main_menu_keyboard(language_code)

    return reply_text, reply_keyboard

async def process_main_menu_trigger(callback: CallbackQuery):
    language_code = await get_user_interface_language(callback.from_user.id)
    reply_text = t(language_code, "main_menu.message")
    reply_keyboard = main_menu_keyboard(language_code)

    return reply_text, reply_keyboard

async def process_settings_trigger(callback: CallbackQuery):
    language_code = await get_user_interface_language(callback.from_user.id)
    reply_text = t(language_code, "settings.message")
    reply_keyboard = settings_keyboard(language_code)

    return reply_text, reply_keyboard

async def process_about_trigger(callback: CallbackQuery):
    language_code = await get_user_interface_language(callback.from_user.id)
    reply_text = t(language_code, "about.message")
    reply_keyboard = about_keyboard(language_code)

    return reply_text, reply_keyboard