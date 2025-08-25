from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from locales.translation import t

def help_keyboard(language_code) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=t(language_code, "help.back_to_main_menu"), callback_data="main_menu"),
    ]

    return InlineKeyboardMarkup(inline_keyboard=[buttons])