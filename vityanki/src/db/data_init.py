import os
from logger import setup_logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .data_models import Base

logger = setup_logging('data_init')

db_path = os.path.join(os.getcwd(), 'vityanki', 'db')
logger.info(f"Database path set to: {db_path}")

if not os.path.exists(db_path):
    logger.info(f"Creating database directory: {db_path}")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

DATABASE_URL = f"sqlite:///{os.path.join(db_path, "database.db")}"
logger.info(f"Database URL: {DATABASE_URL}")

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def init_db():
    Base.metadata.create_all(bind=engine)