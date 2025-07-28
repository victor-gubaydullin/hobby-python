from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard() -> InlineKeyboardMarkup:
    # Arrange buttons in a grid layout
    # Each sublist represents a row of buttons
    buttons = [
        [
            InlineKeyboardButton(text="Study words set", callback_data="study_words_set"),
            InlineKeyboardButton(text="Add words set", callback_data="add_words_set"),
        ],
        [
            InlineKeyboardButton(text="Edit words set", callback_data="edit_words_set"),
            InlineKeyboardButton(text="Delete words set", callback_data="delete_words_set"),
        ],
        [
            InlineKeyboardButton(text="Settings", callback_data="settings"),
            InlineKeyboardButton(text="Help", callback_data="help"),
        ],
        [
            InlineKeyboardButton(text="About", callback_data="about"),
        ]
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=buttons)
    
    # Alternative way with fixed row width:
    # Arrange buttons in rows of 2
    # main_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[buttons[i:i+2] for i in range(0, len(buttons), 2)])