from .data_init import SessionLocal
from .data_models import User, FlashcardSet, Flashcard, Donator, Donation
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

async def add_flashcard_set(telegram_id, name, description=None):
    async with SessionLocal() as session:
        new_set = FlashcardSet(
            telegram_id=telegram_id,
            name=name,
            description=description
        )
        session.add(new_set)
        await session.commit()
        await session.refresh(new_set)  # Ensure new_set.set_id is populated after commit
        return new_set.set_id

async def add_flashcard(set_id, front_side, back_side):
    async with SessionLocal() as session:
        new_card = Flashcard(
            set_id=set_id,
            front_side=front_side,
            back_side=back_side
        )
        session.add(new_card)
        await session.commit()
        await session.refresh(new_card)  # Ensure new_card.card_id is populated after commit
        return new_card.card_id

async def get_user_flashcard_sets(telegram_id):
    async with SessionLocal() as session:
        result = await session.execute(
            select(FlashcardSet)
            .where(FlashcardSet.telegram_id == telegram_id)
            .order_by(FlashcardSet.set_id.desc())
        )
        return result.scalars().all()

async def get_top_donators(n=14):
    """
    Get the top N donators based on the total amount donated in USD.
    Returns list of tuples: (Donator, total_donated)
    """
    async with SessionLocal() as session:
        query = (
            select(
                Donator,
                func.sum(Donation.amount_usd).label("total_donated")
            )
            .join(Donation, Donator.donator_id == Donation.donator_id)
            .group_by(Donator.donator_id)
            .order_by(func.sum(Donation.amount_usd).desc())
            .limit(n)
        )
        # Need to wait for the result to be fetched when using async
        temp_result = await session.execute(query)
        result = temp_result.all()
        return result