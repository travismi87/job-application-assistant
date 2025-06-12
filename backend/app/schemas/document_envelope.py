from pathlib import Path
from typing import Annotated

from pydantic import UUID4, Field

from ..core.enums import (
    DocumentSource,
    DocumentStatus,
    DocumentType,
    DocumentVersion,
    DocumentVisibility,
    FileType,
    MimeType,
)
from .base_schema import InternalBase, MutableInternalBase, RequestBase, ResponseBase


class DocumentInternalBase(InternalBase):
    """
    Base model for internal document schemas.
    This model is used to define common fields and methods for internal document schemas.
    """

    pass


class DocumentMutableInternalBase(MutableInternalBase):
    """
    Mutable base model for internal document schemas.
    This model allows modification of fields after instantiation.
    """

    pass


class DocumentRequestBase(RequestBase):
    """
    Base model for document request schemas.
    This model is used to define common fields and methods for document request schemas.
    """

    pass


class DocumentResponseBase(ResponseBase):
    """
    Base model for document response schemas.
    This model is used to define common fields and methods for document response schemas.
    """

    pass


class DocumentInfo(DocumentInternalBase):
    """
    Response schema for document information.
    This schema defines the fields returned in the response for document retrieval.
    """

    id: Annotated[
        UUID4,
        Field(
            description="Unique identifier for the document",
            examples=["123e4567-e89b-12d3-a456-426614174000", "987e6543-e21b-32d3-b456-426614174001"],
        ),
    ]
    user_id: Annotated[
        UUID4,
        Field(
            description="Unique identifier of the user who owns the document",
            examples=["123e4567-e89b-12d3-a456-426614174000", "987e6543-e21b-32d3-b456-426614174001"],
        ),
    ]
    title: Annotated[
        str,
        Field(
            description="Title of the document",
            max_length=255,
            examples=["Project Proposal", "Meeting Notes", "Research Paper"],
            min_length=1,
        ),
    ]
    raw_content: Annotated[
        str | None,
        Field(
            description="Raw content of the document",
            default=None,
            examples=[
                "This is the raw content of the document.",
                "Another example of raw content for a different document.",
            ],
        ),
    ]
    file_path: Annotated[
        Path | None,
        Field(
            description="Path to the file on the server",
            default=None,
            examples=[
                "/documents/123e4567-e89b-12d3-a456-426614174000.pdf",
                "/documents/987e6543-e21b-32d3-b456-426614174001.docx",
            ],
        ),
    ]
    type: Annotated[
        DocumentType,
        Field(
            description="Type of the document",
            default=DocumentType.GENERAL,
            examples=[
                DocumentType.GENERAL,
                DocumentType.RESUME,
                DocumentType.COVER_LETTER,
                DocumentType.SUPPORTING_DOCUMENT,
            ],
        ),
    ]
    mime_type: Annotated[
        MimeType | None,
        Field(
            description="MIME type of the document",
            default=None,
            examples=[
                MimeType.PDF,
                MimeType.DOCX,
                MimeType.TXT,
                MimeType.HTML,
            ],
        ),
    ]
    file_type: Annotated[
        FileType | None,
        Field(
            description="File type of the document",
            default=None,
            examples=[
                FileType.PDF,
                FileType.DOCX,
                FileType.TXT,
                FileType.HTML,
            ],
        ),
    ]
    status: Annotated[
        DocumentStatus,
        Field(
            description="Status of the document",
            default=DocumentStatus.PENDING,
            examples=[
                DocumentStatus.UPLOADED,
                DocumentStatus.PROCESSING,
                DocumentStatus.PARSED,
                DocumentStatus.VALIDATED,
                DocumentStatus.ERROR,
                DocumentStatus.ARCHIVED,
                DocumentStatus.PENDING,
            ],
        ),
    ]
    visibility: Annotated[
        DocumentVisibility,
        Field(
            description="Visibility of the document",
            default=DocumentVisibility.PRIVATE,
            examples=[
                DocumentVisibility.PUBLIC,
                DocumentVisibility.PRIVATE,
                DocumentVisibility.INTERNAL,
                DocumentVisibility.CONFIDENTIAL,
            ],
        ),
    ]
    source: Annotated[
        DocumentSource,
        Field(
            description="Source of the document",
            default=DocumentSource.USER_UPLOAD,
            examples=[
                DocumentSource.USER_UPLOAD,
                DocumentSource.EMAIL,
                DocumentSource.EXTERNAL_API,
                DocumentSource.SCRAPED,
                DocumentSource.IMPORTED,
                DocumentSource.GENERATED,
            ],
        ),
    ]
    version: Annotated[
        DocumentVersion | None,
        Field(
            description="Version of the document",
            default=None,
            examples=[
                DocumentVersion.DRAFT,
                DocumentVersion.FINAL,
                DocumentVersion.REVISED,
                DocumentVersion.ARCHIVED,
                DocumentVersion.TEMPLATE,
            ],
        ),
    ]
