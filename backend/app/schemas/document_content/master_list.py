from typing import Annotated, Literal

from pydantic import Field

from ...core.enums import DocumentType
from .profile import ProfessionalProfileStructure


class MasterList(ProfessionalProfileStructure):
    """
    Schema for the master list document content.
    This schema defines the structure of the master list used in job applications.
    """

    document_type: Annotated[
        Literal[DocumentType.MASTER_LIST],
        Field(
            description="Type of the document, always 'MASTER_LIST'",
        ),
    ]
