from aiogram.fsm.state import State, StatesGroup

'''The view of the states should be not from the point of view of the user, but from the point of view of the bot.'''

class WordsetAddition(StatesGroup):
    waiting_for_wordset_name = State()
    waiting_for_wordset_source_language = State()
    waiting_for_wordset_target_language = State()
    waiting_for_words = State()

class WordsetEditing(StatesGroup):
    waiting_for_wordset_selection = State()
    waiting_for_reqired_change = State()
    waiting_for_wordset_name = State()
    waiting_for_wordset_source_language = State()
    waiting_for_wordset_target_language = State()
    waiting_for_words = State()

class WordsetDeletion(StatesGroup):
    waiting_for_wordset_selection = State()
    waiting_for_confirmation = State()