from typing import Annotated

from pydantic import UUID4, Field

from ..core.enums import AssistantStepStatus, AssistantStepType
from .base_schema import InternalBase, MutableInternalBase, RequestBase
from .mixins.timestamp_mixin import TimestampMixin


class AssistantStepInfo(InternalBase, TimestampMixin):
    """
    Response schema for assistant step information.
    This schema defines the fields returned in the response for assistant step retrieval.
    """

    id: Annotated[
        UUID4,
        Field(
            description="Unique identifier for the assistant step",
            examples=["123e4567-e89b-12d3-a456-426614174000"],
        ),
    ]
    job_application_id: Annotated[
        UUID4,
        Field(
            description="Unique identifier of the job application associated with the assistant step",
            examples=["123e4567-e89b-12d3-a456-426614174000"],
        ),
    ]
    step_name: Annotated[
        AssistantStepType,
        Field(
            description="Name of the assistant step",
            examples=[
                AssistantStepType.PENDING,
                AssistantStepType.INITIAL_SYNTHESIS,
                AssistantStepType.MASTER_LIST,
                AssistantStepType.CANDIDATE_VALIDATION,
                AssistantStepType.TAILORED_RESUME,
                AssistantStepType.TAILORED_COVER_LETTER,
                AssistantStepType.HIRING_MANAGER_REVIEW,
                AssistantStepType.LINKEDIN_OPTIMIZATION,
                AssistantStepType.INTERVIEW_PREPARATION,
                AssistantStepType.SKILL_DEVELOPMENT_PLAN,
                AssistantStepType.FINAL_CHECKLIST,
            ],
        ),
    ]
    step_status: Annotated[
        AssistantStepStatus,
        Field(
            description="Status of the assistant step",
            examples=[
                AssistantStepStatus.IN_PROGRESS,
                AssistantStepStatus.COMPLETED,
                AssistantStepStatus.FAILED,
                AssistantStepStatus.CANCELLED,
                AssistantStepStatus.NOT_STARTED,
                AssistantStepStatus.WAITING_FOR_USER_INPUT,
            ],
        ),
    ]
    step_order: Annotated[
        int | None,
        Field(
            description="Order of the assistant step in the sequence",
            default=None,
            examples=[1, 2, 3],
        ),
    ]
    previous_step_id: Annotated[
        UUID4 | None,
        Field(
            description="Unique identifier of the previous assistant step",
            default=None,
            examples=["123e4567-e89b-12d3-a456-426614174000"],
        ),
    ]
    input_context: Annotated[
        dict | None,
        Field(
            description="Input context for the assistant step",
            default=None,
            examples=[{"key": "value"}, {"another_key": "another_value"}],
        ),
    ]
    result: Annotated[
        dict | None,
        Field(
            description="Result of the assistant step",
            default=None,
            examples=[{"result_key": "result_value"}, {"another_result_key": "another_result_value"}],
        ),
    ]


class AssistantStepCreate(MutableInternalBase):
    """
    Request schema for creating a new assistant step.
    This schema defines the fields required to create a new assistant step.
    """

    job_application_id: Annotated[
        UUID4,
        Field(
            description="Unique identifier of the job application associated with the assistant step",
            examples=["123e4567-e89b-12d3-a456-426614174000"],
        ),
    ]
    step_name: Annotated[
        AssistantStepType,
        Field(
            description="Name of the assistant step",
            examples=[
                AssistantStepType.PENDING,
                AssistantStepType.INITIAL_SYNTHESIS,
                AssistantStepType.MASTER_LIST,
                AssistantStepType.CANDIDATE_VALIDATION,
                AssistantStepType.TAILORED_RESUME,
                AssistantStepType.TAILORED_COVER_LETTER,
                AssistantStepType.HIRING_MANAGER_REVIEW,
                AssistantStepType.LINKEDIN_OPTIMIZATION,
                AssistantStepType.INTERVIEW_PREPARATION,
                AssistantStepType.SKILL_DEVELOPMENT_PLAN,
                AssistantStepType.FINAL_CHECKLIST,
            ],
        ),
    ]
    step_order: Annotated[
        int | None,
        Field(
            description="Order of the assistant step in the sequence",
            default=None,
            examples=[1, 2, 3],
        ),
    ]
    input_context: Annotated[
        dict | None,
        Field(
            description="Input context for the assistant step",
            default=None,
            examples=[{"key": "value"}, {"another_key": "another_value"}],
        ),
    ]


class AssistantStepUpdate(MutableInternalBase):
    """Request schema for updating an existing assistant step.
    This schema defines the fields that can be updated for an existing assistant step.
    """

    step_name: Annotated[
        AssistantStepType | None,
        Field(
            description="Name of the assistant step",
            default=None,
            examples=[],
        ),
    ]
    step_status: Annotated[
        AssistantStepStatus | None,
        Field(
            description="Status of the assistant step",
            default=None,
            examples=[
                AssistantStepStatus.IN_PROGRESS,
                AssistantStepStatus.COMPLETED,
                AssistantStepStatus.FAILED,
                AssistantStepStatus.CANCELLED,
                AssistantStepStatus.NOT_STARTED,
                AssistantStepStatus.WAITING_FOR_USER_INPUT,
            ],
        ),
    ]
    step_order: Annotated[
        int | None,
        Field(
            description="Order of the assistant step in the sequence",
            default=None,
            examples=[1, 2, 3],
        ),
    ]
    previous_step_id: Annotated[
        UUID4 | None,
        Field(
            description="Unique identifier of the previous assistant step",
            default=None,
            examples=["123e4567-e89b-12d3-a456-426614174000"],
        ),
    ]
    input_context: Annotated[
        dict | None,
        Field(
            description="Input context for the assistant step",
            default=None,
            examples=[{"key": "value"}, {"another_key": "another_value"}],
        ),
    ]
    result: Annotated[
        dict | None,
        Field(
            description="Result of the assistant step",
            default=None,
            examples=[{"result_key": "result_value"}, {"another_result_key": "another_result_value"}],
        ),
    ]


class AssistantStepRequest(RequestBase):
    """
    Request schema for assistant step operations.
    This schema defines the fields required for creating or updating an assistant step.
    """

    job_application_id: Annotated[
        UUID4,
        Field(
            description="Unique identifier of the job application associated with the assistant step",
            examples=["123e4567-e89b-12d3-a456-426614174000"],
        ),
    ]
    step_name: Annotated[
        AssistantStepType,
        Field(
            description="Name of the assistant step",
            examples=[
                AssistantStepType.PENDING,
                AssistantStepType.INITIAL_SYNTHESIS,
                AssistantStepType.MASTER_LIST,
                AssistantStepType.CANDIDATE_VALIDATION,
                AssistantStepType.TAILORED_RESUME,
                AssistantStepType.TAILORED_COVER_LETTER,
                AssistantStepType.HIRING_MANAGER_REVIEW,
                AssistantStepType.LINKEDIN_OPTIMIZATION,
                AssistantStepType.INTERVIEW_PREPARATION,
                AssistantStepType.SKILL_DEVELOPMENT_PLAN,
                AssistantStepType.FINAL_CHECKLIST,
            ],
        ),
    ]
    step_status: Annotated[
        AssistantStepStatus | None,
        Field(
            description="Status of the assistant step",
            default=None,
            examples=[
                AssistantStepStatus.IN_PROGRESS,
                AssistantStepStatus.COMPLETED,
                AssistantStepStatus.FAILED,
                AssistantStepStatus.CANCELLED,
                AssistantStepStatus.NOT_STARTED,
                AssistantStepStatus.WAITING_FOR_USER_INPUT,
            ],
        ),
    ]
    step_order: Annotated[
        int | None,
        Field(
            description="Order of the assistant step in the sequence",
            default=None,
            examples=[1, 2, 3],
        ),
    ]
    previous_step_id: Annotated[
        UUID4 | None,
        Field(
            description="Unique identifier of the previous assistant step",
            default=None,
            examples=["123e4567-e89b-12d3-a456-426614174000"],
        ),
    ]
    input_context: Annotated[
        dict | None,
        Field(
            description="Input context for the assistant step",
            default=None,
            examples=[{"key": "value"}, {"another_key": "another_value"}],
        ),
    ]
