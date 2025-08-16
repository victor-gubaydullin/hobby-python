from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states.donation import Donation
from db.data_utils import get_user_interface_language
from keyboards.donate import donate_keyboard, donate_crypto_wallets_keyboard, donate_crypto_blockchain_keyboard
from locales.translation import t

async def process_donate_command(callback: CallbackQuery, state: FSMContext):
    language_code = await get_user_interface_language(callback.from_user.id)
    
    reply_text = t(language_code, "donate.message")
    reply_keyboard = donate_keyboard(language_code)

    await state.set_state(Donation.waiting_for_preferred_donation_method)
    return reply_text, reply_keyboard

async def process_crypto_wallets_selection(callback: CallbackQuery, state: FSMContext):
    language_code = await get_user_interface_language(callback.from_user.id)
    
    reply_text = t(language_code, "donate.crypto_wallets.message")
    reply_keyboard = donate_crypto_wallets_keyboard(language_code)

    # await state.set_state(Donation.waiting_for_crypto_wallet_selection)
    return reply_text, reply_keyboard

async def process_blockchain_selection(callback: CallbackQuery, state: FSMContext):
    language_code = await get_user_interface_language(callback.from_user.id)

    reply_text = t(language_code, "donate.crypto_blockchain.message")
    reply_keyboard = donate_crypto_blockchain_keyboard(language_code)

    # await state.set_state(Donation.waiting_for_blockchain_selection)
    return reply_text, reply_keyboard