from typing import Annotated, List

from pydantic import UUID4, Field, HttpUrl

from ..core.enums import JobApplicationStatus, JobType
from .base_schema import InternalBase, RequestBase, ResponseBase


class JobApplicationInfo(ResponseBase):
    """
    Response schema for job application information.
    This schema defines the fields returned in the response for job application retrieval.
    """

    user_id: Annotated[
        UUID4,
        Field(
            description="Unique identifier of the user who applied for the job",
            examples=["b3c1e2d4-5678-1234-9abc-1234567890ab"],
        ),
    ]
    job_title: Annotated[
        str | None,
        Field(
            description="Title of the job being applied for",
            max_length=255,
            min_length=1,
            default=None,
            examples=["Software Engineer", "Data Analyst"],
        ),
    ]
    company_name: Annotated[
        str | None,
        Field(
            description="Name of the company for the job application",
            max_length=255,
            min_length=1,
            default=None,
            examples=["Tech Solutions Inc.", "Global Enterprises Ltd."],
        ),
    ]
    job_location: Annotated[
        str | None,
        Field(
            description="Location of the job being applied for",
            max_length=255,
            min_length=1,
            default=None,
            examples=["New York, NY", "Remote"],
        ),
    ]
    job_posting_url: Annotated[
        HttpUrl | None,
        Field(
            description="URL of the job posting",
            default=None,
            examples=["https://company.com/jobs/123"],
        ),
    ]
    notes: Annotated[
        str | None,
        Field(
            description="Additional notes or comments for the job application",
            max_length=1000,
            default=None,
            examples=["Follow up in two weeks", "Referred by Jane Smith"],
        ),
    ]
    job_application_status: Annotated[
        JobApplicationStatus,
        Field(
            description="Status of the job application",
            default=JobApplicationStatus.PENDING,
            examples=[
                JobApplicationStatus.PENDING,
                JobApplicationStatus.ACCEPTED,
                JobApplicationStatus.REJECTED,
            ],
        ),
    ]
    job_type: Annotated[
        JobType | None,
        Field(
            description="Type of the job being applied for",
            default=None,
            examples=[
                JobType.FULL_TIME,
                JobType.PART_TIME,
                JobType.CONTRACT,
            ],
        ),
    ]


class JobApplicationCreateRequest(RequestBase):
    """
    Request schema for creating a new job application.
    This schema defines the fields required to create a new job application.
    """

    user_id: Annotated[
        UUID4,
        Field(
            description="Unique identifier of the user applying for the job",
            examples=["b3c1e2d4-5678-1234-9abc-1234567890ab"],
        ),
    ]
    job_title: Annotated[
        str | None,
        Field(
            description="Title of the job being applied for",
            max_length=255,
            min_length=1,
            default=None,
            examples=["Software Engineer", "Data Analyst"],
        ),
    ]
    company_name: Annotated[
        str | None,
        Field(
            description="Name of the company for the job application",
            max_length=255,
            min_length=1,
            default=None,
            examples=["Tech Solutions Inc.", "Global Enterprises Ltd."],
        ),
    ]
    job_location: Annotated[
        str | None,
        Field(
            description="Location of the job being applied for",
            max_length=255,
            min_length=1,
            default=None,
            examples=["New York, NY", "Remote"],
        ),
    ]
    job_posting_url: Annotated[
        HttpUrl | None,
        Field(
            description="URL of the job posting",
            default=None,
            examples=["https://company.com/jobs/123"],
        ),
    ]
    notes: Annotated[
        str | None,
        Field(
            description="Additional notes or comments for the job application",
            max_length=1000,
            default=None,
            examples=["Follow up in two weeks", "Referred by Jane Smith"],
        ),
    ]
    job_application_status: Annotated[
        JobApplicationStatus | None,
        Field(
            description="Status of the job application",
            default=JobApplicationStatus.PENDING,
            examples=[
                JobApplicationStatus.PENDING,
                JobApplicationStatus.ACCEPTED,
                JobApplicationStatus.REJECTED,
            ],
        ),
    ] = JobApplicationStatus.PENDING
    job_type: Annotated[
        str | None,
        Field(
            description="Type of the job being applied for (e.g., Full-time, Part-time)",
            max_length=50,
            min_length=2,
            default=None,
            examples=["Full-time", "Part-time", "Contract"],
        ),
    ]


class JobApplicationUpdateRequest(InternalBase):
    """
    Request schema for updating an existing job application.
    This schema defines the fields that can be updated for a job application.
    """

    user_id: Annotated[
        UUID4,
        Field(
            description="Unique identifier of the user applying for the job",
            examples=["b3c1e2d4-5678-1234-9abc-1234567890ab"],
        ),
    ]
    job_title: Annotated[
        str | None,
        Field(
            description="Title of the job being applied for",
            max_length=255,
            min_length=1,
            default=None,
            examples=["Software Engineer", "Data Analyst"],
        ),
    ]
    company_name: Annotated[
        str | None,
        Field(
            description="Name of the company for the job application",
            max_length=255,
            min_length=1,
            default=None,
            examples=["Tech Solutions Inc.", "Global Enterprises Ltd."],
        ),
    ]
    job_location: Annotated[
        str | None,
        Field(
            description="Location of the job being applied for",
            max_length=255,
            min_length=1,
            default=None,
            examples=["New York, NY", "Remote"],
        ),
    ]
    job_posting_url: Annotated[
        HttpUrl | None,
        Field(
            description="URL of the job posting",
            default=None,
            examples=["https://company.com/jobs/123"],
        ),
    ]
    notes: Annotated[
        str | None,
        Field(
            description="Additional notes or comments for the job application",
            max_length=1000,
            default=None,
            examples=["Follow up in two weeks", "Referred by Jane Smith"],
        ),
    ]
    job_application_status: Annotated[
        JobApplicationStatus | None,
        Field(
            description="Status of the job application",
            default=JobApplicationStatus.PENDING,
            examples=[
                JobApplicationStatus.PENDING,
                JobApplicationStatus.ACCEPTED,
                JobApplicationStatus.REJECTED,
            ],
        ),
    ] = JobApplicationStatus.PENDING
    job_type: Annotated[
        str | None,
        Field(
            description="Type of the job being applied for (e.g., Full-time, Part-time)",
            max_length=50,
            min_length=2,
            default=None,
            examples=["Full-time", "Part-time", "Contract"],
        ),
    ]


class JobApplicationListResponse(ResponseBase):
    """
    Response schema for a list of job applications.
    This schema defines the fields returned in the response for retrieving a list of job applications.
    """

    job_applications: Annotated[
        List[JobApplicationInfo],
        Field(
            description="List or single job application information",
            examples=[
                [{"user_id": "b3c1e2d4-5678-1234-9abc-1234567890ab", "job_title": "Software Engineer"}]
            ],
        ),
    ]
