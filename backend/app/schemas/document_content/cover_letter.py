import datetime
from typing import Annotated, List, Literal

from pydantic import Field

from ...core.enums import DocumentType
from ..base_schema import InternalBase
from .profile import ContactInfo


class RecipientInfo(InternalBase):
    """
    Schema for recipient information in a cover letter.
    This schema defines the structure of the recipient's contact details.
    """

    name: Annotated[
        str,
        Field(
            description="Name of the recipient",
            max_length=100,
            examples=["John Doe", "Jane Smith"],
        ),
    ]
    title: Annotated[
        str | None,
        Field(
            description="Title of the recipient",
            max_length=50,
            default=None,
            examples=["Hiring Manager", "Recruiter"],
        ),
    ]
    company_name: Annotated[
        str | None,
        Field(
            description="Company name of the recipient",
            max_length=100,
            default=None,
            examples=["Tech Solutions Inc.", "Global Enterprises"],
        ),
    ]
    address: Annotated[
        str | None,
        Field(
            description="Address of the recipient",
            max_length=255,
            default=None,
            examples=["123 Main St, City, State, ZIP", "456 Elm St, City, State, ZIP"],
        ),
    ]


class CoverLetter(InternalBase):
    """
    Schema for the cover letter document content.
    This schema defines the structure of the cover letter used in job applications.
    """

    document_type: Annotated[
        Literal[DocumentType.COVER_LETTER],
        Field(
            description="Type of the document, always 'COVER_LETTER'",
        ),
    ]
    sender_contact_info: Annotated[
        ContactInfo,
        Field(
            description="Contact information of the applicant",
            examples=[
                {
                    "name": "John Doe",
                    "address": "123 Main St, City, State, ZIP",
                    "email": "john.doe@example.com",
                    "phone": "555-1234",
                    "links": [
                        {
                            "url": "https://www.linkedin.com/in/johndoe",
                            "title": "LinkedIn Profile",
                            "description": "Professional LinkedIn profile of John Doe",
                        },
                        {
                            "url": "https://www.github.com/johndoe",
                            "title": "GitHub Profile",
                            "description": "GitHub profile showcasing John Doe's projects",
                        },
                    ],
                }
            ],
        ),
    ]
    date_written: Annotated[
        datetime.date,
        Field(
            description="Date when the cover letter was written",
            examples=["2023-10-01", "2023-10-15"],
        ),
    ]
    recipient_info: Annotated[
        RecipientInfo,
        Field(
            description="Recipient information for the cover letter",
            examples=[
                {
                    "name": "Jane Smith",
                    "title": "Hiring Manager",
                    "company_name": "Tech Solutions Inc.",
                    "address": "456 Elm St, City, State, ZIP",
                }
            ],
        ),
    ]
    subject: Annotated[
        str | None,
        Field(
            description="Subject of the cover letter",
            max_length=255,
            default=None,
            examples=[
                "Application for Software Engineer Position",
                "Interest in Marketing Manager Role",
                "RE: Application for Senior Software Engineer (ID: 12345)",
            ],
        ),
    ]
    salutation: Annotated[
        str,
        Field(
            description="Salutation used in the cover letter",
            max_length=50,
            examples=["Dear Hiring Manager", "To Whom It May Concern", "Hello Jane"],
        ),
    ]
    body_paragraphs: Annotated[
        List[str],
        Field(
            description="Body paragraphs of the cover letter",
            min_length=1,
            max_length=10,
            examples=[
                "I am writing to express my interest in the Software Engineer position at Tech Solutions Inc.",
                "With over 5 years of experience in software development, I am confident in my ability to contribute effectively to your team.",
            ],
        ),
    ]
    closing: Annotated[
        str,
        Field(
            description="Closing statement of the cover letter",
            max_length=100,
            examples=["Sincerely", "Best regards", "Thank you for your consideration"],
        ),
    ]
    signature: Annotated[
        str,
        Field(
            description="Signature of the applicant",
            max_length=100,
            examples=["John Doe", "Jane Smith"],
        ),
    ]
