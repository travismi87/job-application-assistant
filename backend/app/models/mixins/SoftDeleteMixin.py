from datetime import datetime

from sqlalchemy import TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column


class SoftDeleteMixin:
    deleted_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=True
    )
    is_deleted: Mapped[bool | None] = mapped_column(default=False, nullable=False)
    """
    Soft delete mixin for models.
    """

    def soft_delete(self):
        """
        Marks the record as deleted without actually removing it from the database.
        """
        self.is_deleted = True
        self.deleted_at = func.now()

    def restore(self):
        """
        Restores the record by marking it as not deleted.
        """
        self.is_deleted = False
        self.deleted_at = None
