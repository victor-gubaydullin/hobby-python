from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states.donation import Donation
from db.data_utils import get_user_interface_language
from keyboards.donate import donate_keyboard
from locales.translation import t

async def process_donate_command(callback: CallbackQuery, state: FSMContext):
    language_code = await get_user_interface_language(callback.from_user.id)
    
    reply_text = t(language_code, "donate.text")
    reply_keyboard = donate_keyboard(language_code)

    await state.set_state(Donation.waiting_for_preferred_donation_method)
    return reply_text, reply_keyboard