from typing import Annotated, List, Literal

from pydantic import Field

from ...core.enums import DocumentType
from ..base_schema import InternalBase


class SupportingDocument(InternalBase):
    """
    Schema for the supporting document content.
    This schema defines the structure of the supporting documents used in job applications.
    """

    document_type: Annotated[
        Literal[DocumentType.SUPPORTING_DOCUMENT],
        Field(
            description="Type of the document, always 'SUPPORTING_DOCUMENT'",
        ),
    ]

    title: Annotated[
        str,
        Field(
            description="Title of the supporting document",
            max_length=255,
            examples=["Project Report", "Certification", "Reference Letter"],
            min_length=1,
        ),
    ]
    ai_generated_summary: Annotated[
        str,
        Field(
            description="AI-generated summary of the supporting document",
            examples=[
                "This document provides a detailed report on the project outcomes.",
                "This certification validates the completion of the course.",
            ],
        ),
    ]
    extracted_key_points: Annotated[
        List[str],
        Field(
            default_factory=list,
            description="Key points extracted from the supporting document",
            examples=[
                ["Key point 1", "Key point 2"],
                ["Certification details", "Completion date"],
            ],
        ),
    ]
    extracted_keywords: Annotated[
        List[str] | None,
        Field(
            description="Keywords extracted from the supporting document",
            default=None,
            examples=[
                ["project", "report", "outcomes"],
                ["certification", "course", "completion"],
            ],
        ),
    ]
