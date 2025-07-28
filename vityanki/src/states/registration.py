from aiogram.fsm.state import State, StatesGroup

class Registration(StatesGroup):
    waiting_for_language = State()
    registration_complete = State()