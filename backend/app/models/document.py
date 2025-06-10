import uuid
from pathlib import Path
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import ENUM as PG_ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core.enums import (
    DocumentSource,
    DocumentStatus,
    DocumentType,
    DocumentVersion,
    DocumentVisibility,
)
from .base_model import BaseModel
from .custom_types.path_type import PathType
from .job_application import JobApplication
from .mixins import SoftDeleteMixin, TimestampMixin
from .user import User

if TYPE_CHECKING:
    from .user import User


class Document(BaseModel, TimestampMixin, SoftDeleteMixin):
    """
    Document model representing a document in the system.
    Inherits from BaseModel, TimestampMixin, and SoftDeleteMixin.
    """

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped[User] = relationship("User", back_populates="documents")

    job_application_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("job_application.id"), nullable=True
    )
    job_application: Mapped[JobApplication | None] = relationship(
        "JobApplication", back_populates="documents"
    )

    title: Mapped[String] = mapped_column(String, nullable=False)
    content: Mapped[Text | None] = mapped_column(Text, nullable=True)
    file_path: Mapped[Path | None] = mapped_column(PathType, nullable=True, default=None)

    type: Mapped[DocumentType] = mapped_column(
        PG_ENUM(DocumentType), default=DocumentType.GENERAL, nullable=False
    )
    status: Mapped[DocumentStatus] = mapped_column(
        PG_ENUM(DocumentStatus), default=DocumentStatus.PENDING, nullable=False
    )
    visibility: Mapped[DocumentVisibility] = mapped_column(
        PG_ENUM(DocumentVisibility), default=DocumentVisibility.PRIVATE, nullable=False
    )

    source: Mapped[DocumentSource] = mapped_column(
        PG_ENUM(DocumentSource), default=DocumentSource.USER_UPLOAD, nullable=False
    )

    version: Mapped[DocumentVersion | None] = mapped_column(
        PG_ENUM(DocumentVersion), default=None, nullable=True
    )

    def __repr__(self) -> str:
        return f"<Document(title={self.title}, user_id={self.user_id}, status={self.status})>"
