from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy.dialects.postgresql import ENUM as PG_ENUM
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core.enums import JobApplicationStatus, JobAssistantStep
from .base_model import BaseModel
from .mixins import SoftDeleteMixin, TimestampMixin

if TYPE_CHECKING:
    from .job_application import JobApplication


class JobApplicationAssistantStep(BaseModel, TimestampMixin, SoftDeleteMixin):
    """
    JobApplicationAssistantStep model representing a step in the job application assistant process.
    Inherits from BaseModel, TimestampMixin, and SoftDeleteMixin.
    """

    job_application_id: Mapped[UUID] = mapped_column(ForeignKey("job_application.id"), nullable=False)
    job_application: Mapped[JobApplication] = relationship("JobApplication", back_populates="assistant_steps")

    step_name: Mapped[JobAssistantStep] = mapped_column(
        PG_ENUM(JobAssistantStep), nullable=False, default=JobAssistantStep.INITIAL
    )
    step_status: Mapped[JobApplicationStatus] = mapped_column(
        PG_ENUM(JobApplicationStatus), nullable=False, default=JobApplicationStatus.PENDING
    )
    content: Mapped[String | None] = mapped_column(String, nullable=True)

    def __repr__(self) -> str:
        return (
            f"<JobApplicationAssistantStep(job_application_id={self.job_application_id}, "
            f"step_name={self.step_name}, step_status={self.step_status})>"
        )
