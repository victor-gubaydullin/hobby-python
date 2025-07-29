from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from locales.translation import t

def main_menu_keyboard(language_code) -> InlineKeyboardMarkup:
    # Arrange buttons in a grid layout
    # Each sublist represents a row of buttons
    buttons = [
        [
            InlineKeyboardButton(text=t(language_code, "main_menu.study_word_set"), callback_data="study_word_set"),
            InlineKeyboardButton(text=t(language_code, "main_menu.add_word_set"), callback_data="add_word_set"),
        ],
        [
            InlineKeyboardButton(text=t(language_code, "main_menu.edit_word_set"), callback_data="edit_word_set"),
            InlineKeyboardButton(text=t(language_code, "main_menu.delete_word_set"), callback_data="delete_word_set"),
        ],
        [
            InlineKeyboardButton(text=t(language_code, "main_menu.settings"), callback_data="settings"),
            InlineKeyboardButton(text=t(language_code, "main_menu.help"), callback_data="help"),
        ],
        [
            InlineKeyboardButton(text=t(language_code, "main_menu.about"), callback_data="about"),
        ]
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)
    
    # Alternative way with fixed row width:
    # Arrange buttons in rows of 2
    # main_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons[i:i+2] for i in range(0, len(buttons), 2)])