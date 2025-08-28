from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, BigInteger, Enum, DateTime, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    interface_language: Mapped[str] = mapped_column(String(8), nullable=False, default="en")

    # One user can have many flashcard sets.
    flashcard_sets: Mapped[list["FlashcardSet"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )

class FlashcardSet(Base):
    __tablename__ = "flashcard_sets"

    set_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.telegram_id", ondelete="RESTRICT"), nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    description: Mapped[str] = mapped_column(String(256), nullable=True)
    study_mode: Mapped[str] = mapped_column(Enum("fast", "long-term", name="study_mods_enum"), nullable=False, default="fast")

    # One user can have many sets.
    user: Mapped["User"] = relationship(
        back_populates="flashcard_sets"
    )

    # One set can have many cards.
    flashcards: Mapped[list["Flashcard"]] = relationship(
        back_populates="flashcard_set",
        cascade="all, delete-orphan"
    )

    # One set can have many study logs.
    study_logs: Mapped[list["FlashcardSetsStudyLog"]] = relationship(
        back_populates="flashcard_set",
        cascade="all, delete-orphan"
    )

class FlashcardSetsStudyLog(Base):
    __tablename__ = "flashcard_sets_study_log"

    log_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    set_id: Mapped[int] = mapped_column(Integer, ForeignKey("flashcard_sets.set_id", ondelete="CASCADE"), nullable=False)
    study_datetime: Mapped[str] = mapped_column(DateTime, nullable=False)  # Format: YYYY-MM-DD HH:MM:SS

    # One study log entry belongs to one flashcard set.
    flashcard_set: Mapped["FlashcardSet"] = relationship(
        back_populates="study_logs"
    )

class Flashcard(Base):
    __tablename__ = "flashcards"

    card_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    set_id: Mapped[int] = mapped_column(Integer, ForeignKey("flashcard_sets.set_id", ondelete="CASCADE"), nullable=False)
    front_side: Mapped[str] = mapped_column(String(512), nullable=True)
    back_side: Mapped[str] = mapped_column(String(512), nullable=True)
    correct_answers: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    total_answers: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # One word belongs to one wordset.
    flashcard_set: Mapped["FlashcardSet"] = relationship(
        back_populates="flashcards"
    )

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