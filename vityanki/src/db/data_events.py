from sqlalchemy import event, select, delete
from sqlalchemy.orm import Session
from db.data_models import Donator, Donation
from logger import setup_logging

logger = setup_logging('data_events')

def register_db_listeners(engine):
    """
    Attach all engine/session-level event listeners.
    """
    # Enable SQLite foreign key support.
    if engine.dialect.name == "sqlite":
        @event.listens_for(engine.sync_engine, "connect")
        def _set_sqlite_pragma(raw_sqlite_connection, _connection_record):
            cursor = raw_sqlite_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()
        logger.info("SQLite PRAGMA foreign_keys=ON listener registered.")

    # Delete orphan donators after last donation removed.
    @event.listens_for(Session, "after_flush")
    def delete_orphan_donators(session, _flush_context_that_is_needed_to_be_passed):
        """
        If a Donation is deleted and that was the donator's last donation, also delete the Donator.
        Example: if a Donator has no remaining donations, they are considered an orphan and deleted.
            donator_ids = {3, 5}
            remaining_donators = {5}
            orphan_ids = {3}.
        """
        donator_ids = {obj.donator_id for obj in session.deleted if isinstance(obj, Donation)}
        if not donator_ids:
            return

        logger.debug(f"Checking for orphaned donators among IDs: {donator_ids}")

        remaining_donators = set(
            session.scalars(
                select(Donation.donator_id).where(Donation.donator_id.in_(donator_ids))
            )
        )
        logger.debug(f"Donators with remaining donations: {remaining_donators}")

        orphan_ids = donator_ids - remaining_donators
        if orphan_ids:
            logger.info(f"Auto-deleting orphaned donators: {orphan_ids}")
            session.execute(
                delete(Donator).where(Donator.donator_id.in_(orphan_ids))
            )
    
    logger.info("Database event listeners registered.")