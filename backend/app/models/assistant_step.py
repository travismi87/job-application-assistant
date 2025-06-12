from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import ENUM as PG_ENUM
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..core.enums import AssistantStepStatus, AssistantStepType
from .base_model import BaseModel
from .mixins import SoftDeleteMixin, TimestampMixin

if TYPE_CHECKING:
    from .job_application import JobApplication


class AssistantStep(BaseModel, TimestampMixin, SoftDeleteMixin):
    """
    JobApplicationAssistantStep model representing a step in the job application assistant process.
    Inherits from BaseModel, TimestampMixin, and SoftDeleteMixin.
    """

    job_application_id: Mapped[UUID] = mapped_column(ForeignKey("job_application.id"), nullable=False)
    job_application: Mapped[JobApplication] = relationship("JobApplication", back_populates="assistant_steps")

    step_name: Mapped[AssistantStepType] = mapped_column(
        PG_ENUM(AssistantStepType), nullable=False, default=AssistantStepType.INITIAL
    )
    step_status: Mapped[AssistantStepStatus] = mapped_column(
        PG_ENUM(AssistantStepStatus), nullable=False, default=AssistantStepStatus.NOT_STARTED
    )
    step_order: Mapped[int] = mapped_column(Integer, nullable=True)
    previous_step_id: Mapped[UUID | None] = mapped_column(ForeignKey("assistant_step.id"), nullable=True)
    input_context: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    result: Mapped[dict | None] = mapped_column(JSONB, nullable=True)

    def __repr__(self) -> str:
        return (
            f"<AssistantStep(job_application_id={self.job_application_id}, "
            f"step_name={self.step_name}, step_status={self.step_status}, "
            f"step_order={self.step_order}, previous_step_id={self.previous_step_id})>"
        )
