import uuid
from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import ENUM as PG_ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core.enums import (
    DocumentSource,
    DocumentStatus,
    DocumentType,
    DocumentVersion,
    DocumentVisibility,
    FileType,
    MimeType,
)
from .base_model import BaseModel
from .custom_types.path_type import PathType
from .mixins import SoftDeleteMixin, TimestampMixin

if TYPE_CHECKING:
    from .job_application import JobApplication
    from .user import User


class Document(BaseModel, TimestampMixin, SoftDeleteMixin):
    """
    Document model representing a document in the system.
    Inherits from BaseModel, TimestampMixin, and SoftDeleteMixin.
    """

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="documents")
    file_path: Mapped[PathType | None] = mapped_column(PathType, nullable=True, default=None)
    job_applications: Mapped[List["JobApplication"]] = relationship(
        "JobApplication", secondary="document_job_application", back_populates="documents"
    )

    title: Mapped[String] = mapped_column(String, nullable=False)
    content: Mapped[Text | None] = mapped_column(Text, nullable=True)

    type: Mapped[DocumentType] = mapped_column(
        PG_ENUM(DocumentType, name="document_type", create_type=True),
        default=DocumentType.GENERAL,
        nullable=False,
    )
    mime_type: Mapped[MimeType | None] = mapped_column(
        PG_ENUM(MimeType, name="mime_type", create_type=True), default=None, nullable=True
    )
    file_type: Mapped[FileType | None] = mapped_column(
        PG_ENUM(FileType, name="file_type", create_type=True), default=None, nullable=True
    )
    status: Mapped[DocumentStatus] = mapped_column(
        PG_ENUM(DocumentStatus, name="document_status", create_type=True),
        default=DocumentStatus.PENDING,
        nullable=False,
    )
    visibility: Mapped[DocumentVisibility] = mapped_column(
        PG_ENUM(DocumentVisibility, name="document_visibility", create_type=True),
        default=DocumentVisibility.PRIVATE,
        nullable=False,
    )

    source: Mapped[DocumentSource] = mapped_column(
        PG_ENUM(DocumentSource, name="document_source", create_type=True),
        default=DocumentSource.USER_UPLOAD,
        nullable=False,
    )

    version: Mapped[DocumentVersion | None] = mapped_column(
        PG_ENUM(DocumentVersion, name="document_version", create_type=True), default=None, nullable=True
    )
    tags: Mapped[List[str] | None] = mapped_column(String, nullable=True, default=None)
    description: Mapped[Text | None] = mapped_column(Text, nullable=True, default=None)

    def __repr__(self) -> str:
        return f"<Document(title={self.title}, user_id={self.user_id}, status={self.status})>"
