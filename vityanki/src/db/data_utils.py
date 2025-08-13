from .data_init import SessionLocal
from .data_models import User

async def get_user_interface_language(telegram_id):
    async with SessionLocal() as session:
        # In case telegram_id is not a primary key or is not unique, use
        # user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        user = await session.get(User, telegram_id)
        return user.interface_language if user else None

async def set_user_interface_language(telegram_id, language):
    async with SessionLocal() as session:
        # In case telegram_id is not a primary key or is not unique, use
        # user = await session.scalar(select(User).where(User.telegram_id == telegram_id))
        user = await session.get(User, telegram_id)
        if user:
            user.interface_language = language
        else:
            new_user = User(telegram_id=telegram_id, interface_language=language)
            session.add(new_user)
        await session.commit()