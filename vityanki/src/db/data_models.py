from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String, BigInteger

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    interface_language: Mapped[str] = mapped_column(String(8), nullable=False, default="en")

