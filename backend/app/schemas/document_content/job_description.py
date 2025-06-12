from typing import Annotated, List, Literal

from pydantic import Field

from ...core.enums import DocumentType
from ..base_schema import InternalBase


class Qualifications(InternalBase):
    """
    Schema for qualifications in a job description.
    This schema defines the fields related to qualifications required for a job.
    """

    required: List[str] = Field(
        default_factory=list,
        description="List of required qualifications for the job",
        examples=["Bachelor's degree in Computer Science", "5+ years of experience in software development"],
    )
    preferred: List[str] = Field(
        default_factory=list,
        description="List of preferred qualifications for the job",
        examples=["Experience with cloud technologies", "Familiarity with Agile methodologies"],
    )


class JobDescription(InternalBase):
    """
    Base model for job descriptions.
    This model is used to define common fields and methods for job description schemas.
    """

    document_type: Annotated[
        Literal[DocumentType.JOB_DESCRIPTION],
        Field(
            description="Type of the document, always 'JOB_DESCRIPTION'",
        ),
    ]

    job_title: Annotated[
        str | None,
        Field(
            default=None,
            max_length=255,
            min_length=1,
            description="Title of the job position",
            examples=["Software Engineer", "Data Scientist"],
        ),
    ]
    company_name: Annotated[
        str | None,
        Field(
            default=None,
            max_length=255,
            min_length=1,
            description="Name of the company offering the job",
            examples=["Tech Innovations Inc.", "Data Solutions Ltd."],
        ),
    ]
    location: Annotated[
        str | None,
        Field(
            default=None,
            max_length=255,
            min_length=1,
            description="Location of the job",
            examples=["New York, NY", "Remote"],
        ),
    ]
    summary: Annotated[
        str | None,
        Field(
            default=None,
            description="Brief summary of the job description",
            examples=[
                "We are looking for a skilled software engineer to join our team.",
                "Seeking a data scientist with expertise in machine learning.",
            ],
        ),
    ]
    responsibilities: Annotated[
        List[str] | None,
        Field(
            default_factory=list,
            description="List of job responsibilities",
            examples=[
                "Develop and maintain software applications",
                "Analyze and interpret complex data sets",
            ],
        ),
    ]
    qualifications: Annotated[
        Qualifications | None,
        Field(
            default=None,
            description="Qualifications required for the job",
            examples=[
                {
                    "required": [
                        "Bachelor's degree in Computer Science",
                        "5+ years of experience in software development",
                    ],
                    "preferred": [
                        "Experience with cloud technologies",
                        "Familiarity with Agile methodologies",
                    ],
                }
            ],
        ),
    ]
