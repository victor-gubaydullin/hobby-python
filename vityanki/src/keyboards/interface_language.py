from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def language_selection_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇬🇧 EN", callback_data="interface_language_en"),
                InlineKeyboardButton(text="🇩🇪 DE", callback_data="interface_language_de"),
                InlineKeyboardButton(text="🇷🇺 RU", callback_data="interface_language_ru"),
            ]
        ]
    )

