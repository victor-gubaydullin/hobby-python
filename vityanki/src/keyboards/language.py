from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def language_selection_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇬🇧 EN", callback_data="lang_en"),
                InlineKeyboardButton(text="🇩🇪 DE", callback_data="lang_de"),
                InlineKeyboardButton(text="🇷🇺 RU", callback_data="lang_ru"),
            ]
        ]
    )

'''''
# Aflernative implementation for language selection keyboard
# More dinamic and can be used in contexts where you do not know the amount of buttons beforehand

def language_selection_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=3)
    buttons = [
        InlineKeyboardButton(text="EN", callback_data="lang_en"),
        InlineKeyboardButton(text="DE", callback_data="lang_de"),
        InlineKeyboardButton(text="RU", callback_data="lang_ru")
    ]
    keyboard.add(*buttons)
    return keyboard
'''