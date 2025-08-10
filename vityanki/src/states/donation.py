from aiogram.fsm.state import State, StatesGroup

class Donation(StatesGroup):
    waiting_for_preferred_donation_method = State()
    waiting_for_anonymous_or_public_donation = State()
    waiting_for_nickname = State()
    waiting_for_crypto_name = State()
    waiting_for_crypto_wallet = State()
    waiting_for_feedback_message = State()