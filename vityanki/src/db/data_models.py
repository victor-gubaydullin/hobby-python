from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, BigInteger, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    interface_language: Mapped[str] = mapped_column(String(8), nullable=False, default="en")

class Donator(Base):
    __tablename__ = "donators"

    donator_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    is_anonymous: Mapped[bool] = mapped_column(default=True, nullable=False)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=True)
    nickname: Mapped[str] = mapped_column(String(64), nullable=True)

    # One donator can have many donations.
    donations: Mapped[list["Donation"]] = relationship(
        back_populates="donator",
        cascade="all, delete-orphan"
    )

    def to_string(self, total_donated=None):
        # Need to add currency handling
        return f"{'Anonymous' if self.is_anonymous else self.nickname}: {total_donated or 0:.2f} USD"


class Donation(Base):
    __tablename__ = "donations"

    donation_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    donator_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("donators.donator_id", ondelete="CASCADE"),
        nullable=False
    )
    crypto_name: Mapped[str] = mapped_column(String(32), nullable=False)
    crypto_wallet: Mapped[str] = mapped_column(String(128), nullable=False)
    feedback_message: Mapped[str] = mapped_column(String(512), nullable=True)
    amount_raw: Mapped[float] = mapped_column(nullable=False)
    amount_usd: Mapped[float] = mapped_column(nullable=True)

    # One donation belongs to one donator.
    donator: Mapped["Donator"] = relationship(
        back_populates="donations"
    )