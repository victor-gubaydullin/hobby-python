from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from locales.translation import t

def flashcards_main_menu_keyboard(language_code, user_flashcard_sets, chunk_index=0) -> InlineKeyboardMarkup:
    add_new_set_button = [
        [
            InlineKeyboardButton(text=t(language_code, "flashcards.add_flashcard_set"), callback_data="add_wordset"),
        ]
    ]

    # Split user_flashcard_sets into chunks of 5 for better display
    chunked_flashcard_sets = [
        user_flashcard_sets[i:i + 5] for i in range(0, len(user_flashcard_sets), 5)
    ]

    # Ensure chunk_index is within bounds, default to the first chunk if out of bounds
    if chunk_index < 0 or chunk_index >= len(chunked_flashcard_sets):
        chunk_index = 0

    # Handle empty flashcard sets case
    if chunked_flashcard_sets:
        current_chunk = chunked_flashcard_sets[chunk_index]
    else:
        current_chunk = []
        chunk_index = None

    flashcards_sets_buttons = [
        [
            InlineKeyboardButton(
                text=f"📚 {flashcard_set.name}",
                callback_data=f"flashcard_set_{flashcard_set.set_id}"
            )
        ] for flashcard_set in current_chunk
    ]

    # Navigation buttons if there are multiple chunks
    if chunk_index is None:
        # No flashcard sets
        navigation_buttons = [
            [
                InlineKeyboardButton(text=t(language_code, "navigation.back_to_main_menu"), callback_data="main_menu"),
            ]
        ]
    elif chunk_index == 0 and len(chunked_flashcard_sets) == 1:
        # Only one page
        navigation_buttons = [
            [
                InlineKeyboardButton(text=t(language_code, "navigation.back_to_main_menu"), callback_data="main_menu"),
            ]
        ]
    elif chunk_index == 0:
        # First page
        navigation_buttons = [
            [
                InlineKeyboardButton(text=t(language_code, "navigation.next"), callback_data=f"flashcards_main_menu_{chunk_index + 1}"),
            ],
            [
                InlineKeyboardButton(text=t(language_code, "navigation.back_to_main_menu"), callback_data="main_menu"),
            ],
        ]
    elif chunk_index > 0 and chunk_index < len(chunked_flashcard_sets) - 1:
        # Middle pages
        navigation_buttons = [
            [
                InlineKeyboardButton(text=t(language_code, "navigation.back"), callback_data=f"flashcards_main_menu_{chunk_index - 1}"),
                InlineKeyboardButton(text=t(language_code, "navigation.next"), callback_data=f"flashcards_main_menu_{chunk_index + 1}"),
            ],
            [
                InlineKeyboardButton(text=t(language_code, "navigation.back_to_main_menu"), callback_data="main_menu"),
            ],
        ]
    elif chunk_index == len(chunked_flashcard_sets) - 1:
        # Last page
        navigation_buttons = [
            [
                InlineKeyboardButton(text=t(language_code, "navigation.back"), callback_data=f"flashcards_main_menu_{chunk_index - 1}"),
            ],
            [
                InlineKeyboardButton(text=t(language_code, "navigation.back_to_main_menu"), callback_data="main_menu"),
            ]
        ]

    if flashcards_sets_buttons != []:
        all_buttons = add_new_set_button + flashcards_sets_buttons + navigation_buttons
    else:
        all_buttons = add_new_set_button + navigation_buttons

    return InlineKeyboardMarkup(inline_keyboard=all_buttons)