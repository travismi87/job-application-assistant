from typing import Annotated, List

from pydantic import BaseModel, EmailStr, Field, HttpUrl

from ...core.enums import SkillProficiency
from ..base_schema import InternalBase


class Link(InternalBase):
    """
    Base model for links.
    This model is used to define common fields and methods for link schemas.
    """

    url: Annotated[
        HttpUrl,
        Field(
            description="URL of the link",
            examples=["https://www.example.com", "https://www.another-example.com"],
        ),
    ]
    title: Annotated[
        str,
        Field(
            description="Title of the link",
            examples=["Example Link", "Another Example Link"],
        ),
    ]
    description: Annotated[
        str | None,
        Field(
            description="Description of the link",
            default=None,
            examples=[
                "This is an example link that provides information about...",
                "Another example link that showcases...",
            ],
        ),
    ]


class DateRangeMixin(BaseModel):
    """
    Mixin for date range fields.
    This mixin is used to define common date range fields for various schemas.
    """

    start_date: Annotated[
        str,
        Field(
            description="Start date of the range (ISO format)",
            examples=["2020-01-01", "2019-06-15"],
        ),
    ]
    end_date: Annotated[
        str | None,
        Field(
            description="End date of the range (ISO format), if applicable",
            default=None,
            examples=["2021-12-31", None],
        ),
    ]


class ContactInfo(InternalBase):
    """
    Base model for contact information.
    This model is used to define common fields and methods for contact information schemas.
    """

    name: Annotated[
        str,
        Field(
            description="Name of the contact person",
            examples=["John Doe", "Jane Smith"],
        ),
    ]
    email: Annotated[
        EmailStr,
        Field(
            description="Email address of the contact person",
            examples=["john.doe@example.com", "jane.smith@example.com"],
        ),
    ]
    phone: Annotated[
        str | None,
        Field(
            description="Phone number of the contact person",
            default=None,
            examples=["+1-234-567-8901", "+44-1234-567890"],
            pattern=r"^\+?[1-9]\d{1,14}$",
        ),
    ]
    links: Annotated[
        List[Link],
        Field(
            description="List of links related to the contact person",
            default_factory=list,
            examples=[
                {
                    "url": "https://www.linkedin.com/in/johndoe",
                    "title": "LinkedIn Profile",
                    "description": "John Doe's LinkedIn profile",
                },
                {
                    "url": "https://www.github.com/johndoe",
                    "title": "GitHub Profile",
                    "description": "John Doe's GitHub profile",
                },
            ],
        ),
    ]


class Experience(InternalBase, DateRangeMixin):
    """
    Base model for work experience.
    This model is used to define common fields and methods for work experience schemas.
    """

    company_name: Annotated[
        str,
        Field(
            description="Name of the company",
            examples=["Tech Solutions Inc.", "Global Enterprises Ltd."],
        ),
    ]
    job_title: Annotated[
        str,
        Field(
            description="Job title held at the company",
            examples=["Software Engineer", "Senior Developer"],
        ),
    ]
    bullet_points: Annotated[
        List[str],
        Field(
            description="List of bullet points describing responsibilities and achievements",
            default_factory=list,
            examples=[
                "Developed and maintained web applications using Python and Django",
                "Led a team of developers in building a scalable microservices architecture",
            ],
        ),
    ]


class Education(InternalBase, DateRangeMixin):
    """
    Base model for educational qualifications.
    This model is used to define common fields and methods for education schemas.
    """

    institution_name: Annotated[
        str,
        Field(
            description="Name of the educational institution",
            examples=["University of Technology", "Global Business School"],
        ),
    ]
    degree: Annotated[
        str,
        Field(
            description="Degree obtained",
            examples=[
                "Bachelor of Science in Computer Science",
                "Master of Business Administration",
            ],
        ),
    ]
    field_of_study: Annotated[
        str,
        Field(
            description="Field of study",
            examples=["Computer Science", "Business Administration"],
        ),
    ]
    bullet_points: Annotated[
        List[str],
        Field(
            description="List of bullet points describing relevant coursework, honors, or activities",
            default_factory=list,
            examples=[
                "Completed coursework in Data Structures and Algorithms",
                "Graduated with honors, top 10% of the class",
            ],
        ),
    ]


class Skill(InternalBase):
    """Base model for skills.
    This model is used to define common fields and methods for skill schemas.
    """

    name: Annotated[
        str,
        Field(
            description="Name of the skill",
            examples=[
                "Python",
                "JavaScript",
                "Machine Learning",
                "Project Management",
                "Data Analysis",
            ],
        ),
    ]
    proficiency: Annotated[
        SkillProficiency,
        Field(
            description="Proficiency level of the skill",
            default=SkillProficiency.FAMILIAR_WITH,
            examples=[
                SkillProficiency.FAMILIAR_WITH,
                SkillProficiency.PROFICIENT,
                SkillProficiency.EXPERIENCED,
            ],
        ),
    ]
    years_of_experience: Annotated[
        int | None,
        Field(
            description="Number of years of experience with the skill",
            default=None,
            examples=[1, 3, 5, 10],
            ge=0,
            le=50,
        ),
    ]
    context: Annotated[
        str | None,
        Field(
            description="Context or projects where the skill was applied",
            default=None,
            examples=[
                "Developed a web application using React and Node.js",
                "Led a team in implementing machine learning algorithms for data analysis",
            ],
        ),
    ]


class SkillSection(InternalBase):
    """
    Base model for skill sections.
    This model is used to define common fields and methods for skill section schemas.
    """

    title: Annotated[
        str,
        Field(
            description="Title of the skill section",
            examples=[
                "Programming Languages",
                "Data Science Skills",
                "Project Management Skills",
            ],
        ),
    ]
    skills: Annotated[
        List[Skill],
        Field(
            description="List of skills in the section",
            default_factory=List,
            examples=[
                {
                    "name": "Python",
                    "proficiency": SkillProficiency.PROFICIENT,
                    "years_of_experience": 5,
                    "context": "Developed multiple web applications using Django and Flask",
                },
                {
                    "name": "Machine Learning",
                    "proficiency": SkillProficiency.EXPERIENCED,
                    "years_of_experience": 3,
                    "context": "Implemented machine learning models for predictive analytics",
                },
            ],
        ),
    ]


class Certification(InternalBase):
    """
    Base model for certifications.
    This model is used to define common fields and methods for certification schemas.
    """

    name: Annotated[
        str,
        Field(
            description="Name of the certification",
            examples=[
                "Certified Kubernetes Administrator",
                "AWS Certified Solutions Architect",
            ],
        ),
    ]
    issuing_organization: Annotated[
        str,
        Field(
            description="Organization that issued the certification",
            examples=[
                "Cloud Native Computing Foundation",
                "Amazon Web Services",
            ],
        ),
    ]
    issue_date: Annotated[
        str,
        Field(
            description="Date when the certification was issued (ISO format)",
            examples=["2021-05-15", "2022-03-01"],
        ),
    ]
    expiration_date: Annotated[
        str | None,
        Field(
            description="Expiration date of the certification (ISO format), if applicable",
            default=None,
            examples=["2023-05-15", None],
        ),
    ]
    credential_id: Annotated[
        str | None,
        Field(
            description="Unique identifier for the certification credential, if applicable",
            default=None,
            examples=["1234567890", "abcdefg-1234-5678-90ab-cdef12345678"],
        ),
    ]
