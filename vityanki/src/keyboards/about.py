from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from locales.translation import t

def about_keyboard(language_code) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=t(language_code, "about.back_to_main_menu"), callback_data="main_menu"),
        InlineKeyboardButton(text=t(language_code, "about.donate"), callback_data="donate"),
    ]

    return InlineKeyboardMarkup(inline_keyboard=[buttons])