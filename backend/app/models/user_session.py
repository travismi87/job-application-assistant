import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import TIMESTAMP, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel
from .mixins import SoftDeleteMixin, TimestampMixin

if TYPE_CHECKING:
    from .user import User


class UserSession(BaseModel, TimestampMixin, SoftDeleteMixin):
    """
    UserSession model representing a user session in the system.
    Inherits from BaseModel, TimestampMixin, and SoftDeleteMixin.
    """

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped[User] = relationship("User", back_populates="sessions")

    session_token: Mapped[String] = mapped_column(String, unique=True, nullable=False)
    refresh_token: Mapped[String | None] = mapped_column(String, nullable=True)
    ip_address: Mapped[String | None] = mapped_column(String, nullable=True)
    user_agent: Mapped[String | None] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    expires_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)

    def __repr__(self) -> str:
        return f"<UserSession(user_id={self.user_id}, session_token={self.session_token})>"
