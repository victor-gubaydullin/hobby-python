from aiogram.fsm.state import State, StatesGroup

'''
The view of the states should be not from the point of view of the user, but from the point of view of the bot.
Example: The bot is waiting for the user to select a language, and then it completes the registration.
'''

class InterfaceLanguage(StatesGroup):
    waiting_for_language = State()