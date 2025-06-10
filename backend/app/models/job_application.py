from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import TIMESTAMP, UUID, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import ENUM as PG_ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core.enums import JobApplicationStatus, JobAssistantStep, JobType
from .base_model import BaseModel
from .document import Document
from .mixins import SoftDeleteMixin, TimestampMixin
from .user import User

if TYPE_CHECKING:
    from .user import User


class JobApplication(BaseModel, TimestampMixin, SoftDeleteMixin):
    """
    JobApplication model representing a job application in the system.
    Inherits from BaseModel, TimestampMixin, and SoftDeleteMixin.
    """

    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped[User] = relationship("User", back_populates="job_applications")

    job_title: Mapped[String | None] = mapped_column(String, nullable=True, default=None)
    company_name: Mapped[String | None] = mapped_column(String, nullable=True, default=None)
    job_location: Mapped[String | None] = mapped_column(String, nullable=True, default=None)
    job_posting_url: Mapped[String | None] = mapped_column(String, nullable=True, default=None)
    applied_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=False
    )
    notes: Mapped[String | None] = mapped_column(String, nullable=True)
    job_application_status: Mapped[JobApplicationStatus] = mapped_column(
        PG_ENUM(JobApplicationStatus), default=JobApplicationStatus.PENDING, nullable=False
    )
    job_type: Mapped[JobType] = mapped_column(PG_ENUM(JobType), default=JobType.FULL_TIME, nullable=False)
    assisant_step: Mapped[JobAssistantStep] = mapped_column(
        PG_ENUM(JobAssistantStep), default=JobAssistantStep.INITIAL, nullable=False
    )
    documents: Mapped[List[Document]] = relationship(
        "Document", back_populates="job_application", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<JobApplication(user_id={self.user_id}, status={self.job_application_status})>"
