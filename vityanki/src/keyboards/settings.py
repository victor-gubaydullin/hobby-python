from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from locales.translation import t

def settings_keyboard(language_code) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=t(language_code, "navigation.back"), callback_data="main_menu"),
        InlineKeyboardButton(text=t(language_code, "settings.interface_language"), callback_data="change_language"),
    ]

    return InlineKeyboardMarkup(inline_keyboard=[buttons])