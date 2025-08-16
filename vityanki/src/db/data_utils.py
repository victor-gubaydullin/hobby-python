from .data_init import SessionLocal
from .data_models import User, Donator, Donation
from sqlalchemy import select, func

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

async def get_top_donators(n=14):
    async with SessionLocal() as session:
        query = (
            select(
                Donator,
                func.sum(Donation.amount).label("total_donated")
            )
            .join(Donation, Donator.donator_id == Donation.donator_id)
            .group_by(Donator.donator_id)
            .order_by(func.sum(Donation.amount).desc())
            .limit(n)
        )
        results = session.execute(query).all()
        # Returns list of tuples: (Donator, total_donated)
        return results