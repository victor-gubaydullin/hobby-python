from .data_init import SessionLocal
from .data_models import User

async def get_user_interface_language(telegram_id):
    with SessionLocal() as session:
        user = session.get(User, telegram_id)
        return user.interface_language if user else None

async def set_user_interface_language(telegram_id, language):
    with SessionLocal() as session:
        user = session.get(User, telegram_id)
        if user:
            user.interface_language = language
            session.commit()
        else:
            new_user = User(telegram_id=telegram_id, interface_language=language)
            session.add(new_user)
            session.commit()