from aiogram.types import Message
from keyboards.language import language_selection_keyboard

async def process_start_command():
    reply_text = "Select interface language / Wähle Sie die Sprache / Выберите язык интерфейса:"
    reply_keyboard = language_selection_keyboard()

    return reply_text, reply_keyboard