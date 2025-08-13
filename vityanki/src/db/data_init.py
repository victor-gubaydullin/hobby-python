import os
from logger import setup_logging
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from .data_models import Base
from . import data_events

logger = setup_logging('data_init')

db_path = os.path.join(os.getcwd(), 'vityanki', 'db')
logger.info(f"Database path set to: {db_path}")

if not os.path.exists(db_path):
    logger.info(f"Creating database directory: {db_path}")
    os.makedirs(db_path, exist_ok=True)

DATABASE_URL = f"sqlite+aiosqlite:///{os.path.join(db_path, 'database.db')}"
logger.info(f"Database URL: {DATABASE_URL}")

engine = create_async_engine(DATABASE_URL, echo=False, future=True)
data_events.register_db_listeners(engine)
SessionLocal = async_sessionmaker(bind=engine, autoflush=False, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)