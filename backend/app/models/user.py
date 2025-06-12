from pathlib import Path
from typing import TYPE_CHECKING, List

from sqlalchemy import Boolean, String
from sqlalchemy.dialects.postgresql import ENUM as PG_ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core.enums import SSOProvider, UserRole
from .base_model import BaseModel
from .custom_types.path_type import PathType
from .mixins import SoftDeleteMixin, TimestampMixin

if TYPE_CHECKING:
    from .document import Document
    from .job_application import JobApplication
    from .user_session import UserSession


class User(BaseModel, TimestampMixin, SoftDeleteMixin):
    """
    User model representing a user in the system.
    Inherits from BaseModel, TimestampMixin, and SoftDeleteMixin.
    """

    username: Mapped[String] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[String] = mapped_column(String, unique=True, nullable=False)
    first_name: Mapped[String | None] = mapped_column(String, nullable=True)
    last_name: Mapped[String | None] = mapped_column(String, nullable=True)
    password: Mapped[String] = mapped_column(String, nullable=False)
    is_active: Mapped[Boolean] = mapped_column(Boolean, default=True, nullable=False)
    role: Mapped[UserRole] = mapped_column(PG_ENUM(UserRole), default=UserRole.USER, nullable=False)
    profile_picture: Mapped[Path | None] = mapped_column(PathType, nullable=True)
    dir: Mapped[Path | None] = mapped_column(PathType, nullable=True, default=Path(""))
    sso_id: Mapped[String | None] = mapped_column(String, nullable=True, default=None)
    sso_provider: Mapped[SSOProvider | None] = mapped_column(
        PG_ENUM(SSOProvider), nullable=True, default=None
    )
    sso_email_verified: Mapped[Boolean] = mapped_column(Boolean, default=False, nullable=False)
    avatar_url: Mapped[String | None] = mapped_column(String, nullable=True, default=None)
    sessions: Mapped[List["UserSession"]] = relationship(
        "UserSession", back_populates="user", cascade="all, delete-orphan"
    )
    job_applications: Mapped[List["JobApplication"]] = relationship(
        "JobApplication", back_populates="user", cascade="all, delete-orphan"
    )
    documents: Mapped[List["Document"]] = relationship(
        "Document", back_populates="user", cascade="all, delete-orphan"
    )

    @property
    def is_admin(self) -> bool:
        """
        Check if the user has admin privileges.
        """
        return self.role == UserRole.ADMIN

    def __repr__(self) -> str:
        return f"<User(username={self.username}, email={self.email}, role={self.role})>"
