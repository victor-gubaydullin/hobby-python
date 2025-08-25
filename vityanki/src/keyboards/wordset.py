from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from locales.translation import t

def wordset_main_menu_keyboard(language_code) -> InlineKeyboardMarkup:
    arranged_buttons = [
        [
            InlineKeyboardButton(text=t(language_code, "wordset.study_wordset"), callback_data="study_wordset"),
        ],
        [
            InlineKeyboardButton(text=t(language_code, "wordset.add_wordset"), callback_data="add_wordset"),
        ],
        [
            InlineKeyboardButton(text=t(language_code, "wordset.edit_wordset"), callback_data="edit_wordset"),
            InlineKeyboardButton(text=t(language_code, "wordset.delete_wordset"), callback_data="delete_wordset"),
        ],
        [
            InlineKeyboardButton(text=t(language_code, "navigation.back"), callback_data="main_menu"),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=arranged_buttons)