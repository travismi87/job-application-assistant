from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import TIMESTAMP, UUID, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import ENUM as PG_ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core.enums import AssistantStepStatus, AssistantStepType, JobApplicationStatus, JobType
from .base_model import BaseModel
from .mixins import SoftDeleteMixin, TimestampMixin

if TYPE_CHECKING:
    from .assistant_step import AssistantStep
    from .document import Document
    from .user import User


class JobApplication(BaseModel, TimestampMixin, SoftDeleteMixin):
    """
    JobApplication model representing a job application in the system.
    Inherits from BaseModel, TimestampMixin, and SoftDeleteMixin.
    """

    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="job_applications")

    title: Mapped[String | None] = mapped_column(String, nullable=True, default=None)
    company_name: Mapped[String | None] = mapped_column(String, nullable=True, default=None)
    location: Mapped[String | None] = mapped_column(String, nullable=True, default=None)
    posting_url: Mapped[String | None] = mapped_column(String, nullable=True, default=None)
    applied_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=False
    )
    notes: Mapped[String | None] = mapped_column(String, nullable=True)
    assistant_status: Mapped[AssistantStepStatus] = mapped_column(
        PG_ENUM(AssistantStepStatus, name="assistant_step_status", create_type=True),
        default=AssistantStepStatus.NOT_STARTED,
        nullable=False,
    )
    type: Mapped[JobType] = mapped_column(
        PG_ENUM(JobType, name="job_type", create_type=True), default=JobType.FULL_TIME, nullable=False
    )
    assistant_steps: Mapped[List["AssistantStep"]] = relationship(
        "AssistantStep", back_populates="job_application", cascade="all, delete-orphan"
    )
    application_status: Mapped[JobApplicationStatus] = mapped_column(
        PG_ENUM(JobApplicationStatus, name="job_application_status", create_type=True),
        default=JobApplicationStatus.PENDING,
        nullable=False,
    )
    assistant_current_step: Mapped[AssistantStepType] = mapped_column(
        PG_ENUM(AssistantStepType, name="assistant_step_type", create_type=True),
        nullable=False,
        default=AssistantStepType.PENDING,
    )
    documents: Mapped[List["Document"]] = relationship(
        "Document", secondary="document_job_application", back_populates="job_applications"
    )

    def __repr__(self) -> str:
        return f"<JobApplication(user_id={self.user_id}, status={self.application_status})>"
