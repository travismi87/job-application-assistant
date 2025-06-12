from typing import Annotated, Literal

from pydantic import Field

from ...core.enums import DocumentType
from .profile import ProfessionalProfileStructure


class Resume(ProfessionalProfileStructure):
    """
    Schema for the resume document content.
    This schema defines the structure of the resume used in job applications.
    """

    document_type: Annotated[
        Literal[DocumentType.RESUME],
        Field(
            description="Type of the document, always 'RESUME'",
        ),
    ]
