from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from services.donator_services import process_donate_command, process_top_donators_display, process_crypto_wallets_selection, process_blockchain_selection

donator_router = Router()

@donator_router.callback_query(F.data == "donate")
async def donate_button_handler(callback: CallbackQuery, state: FSMContext):
    reply_text, reply_keyboard = await process_donate_command(callback, state)
    
    await callback.message.edit_text(reply_text, reply_markup=reply_keyboard)
    await callback.answer()

@donator_router.callback_query(F.data == "top_donators")
async def top_donators_button_handler(callback: CallbackQuery, state: FSMContext):
    reply_text, reply_keyboard = await process_top_donators_display(callback, state)

    await callback.message.edit_text(reply_text, reply_markup=reply_keyboard)
    await callback.answer()

@donator_router.callback_query(F.data == "crypto_wallets")
async def crypto_wallets_button_handler(callback: CallbackQuery, state: FSMContext):
    reply_text, reply_keyboard = await process_crypto_wallets_selection(callback, state)

    await callback.message.edit_text(reply_text, reply_markup=reply_keyboard)
    await callback.answer()

@donator_router.callback_query(F.data == "crypto_blockchain")
async def crypto_blockchain_button_handler(callback: CallbackQuery, state: FSMContext):
    reply_text, reply_keyboard = await process_blockchain_selection(callback, state)

    await callback.message.edit_text(reply_text, reply_markup=reply_keyboard)
    await callback.answer()