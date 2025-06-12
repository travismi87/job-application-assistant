from typing import Annotated, List

from pydantic import EmailStr, Field, HttpUrl

from ...core.enums import SkillProficiency
from ..base_schema import InternalBase
from ..mixins.date_range_mixin import DateRangeMixin


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
    address: Annotated[
        str | None,
        Field(
            description="Address of the contact person",
            default=None,
            examples=["123 Main St, City, State, ZIP", "456 Elm St, City, State, ZIP"],
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


class ExperienceSection(InternalBase):
    """
    Base model for work experience sections.
    This model is used to define common fields and methods for work experience section schemas.
    """

    title: Annotated[
        str,
        Field(
            description="Title of the work experience section",
            examples=["Professional Experience", "Work History"],
        ),
    ]
    experiences: Annotated[
        List[Experience],
        Field(
            description="List of work experiences in the section",
            default_factory=list,
            examples=[
                {
                    "company_name": "Tech Solutions Inc.",
                    "job_title": "Software Engineer",
                    "start_date": "2020-01-01",
                    "end_date": "2022-01-01",
                    "bullet_points": [
                        "Developed and maintained web applications using Python and Django",
                        "Led a team of developers in building a scalable microservices architecture",
                    ],
                },
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


class EducationSection(InternalBase):
    """
    Base model for education sections.
    This model is used to define common fields and methods for education section schemas.
    """

    title: Annotated[
        str,
        Field(
            description="Title of the education section",
            examples=["Educational Qualifications", "Academic Background"],
        ),
    ]
    education: Annotated[
        List[Education],
        Field(
            description="List of educational qualifications in the section",
            default_factory=list,
            examples=[
                {
                    "institution_name": "University of Technology",
                    "degree": "Bachelor of Science in Computer Science",
                    "field_of_study": "Computer Science",
                    "start_date": "2015-09-01",
                    "end_date": "2019-06-01",
                    "bullet_points": [
                        "Completed coursework in Data Structures and Algorithms",
                        "Graduated with honors, top 10% of the class",
                    ],
                },
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
            default_factory=list,
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


class CertificationSection(InternalBase):
    """Base model for certification sections.
    This model is used to define common fields and methods for certification section schemas.
    """

    title: Annotated[
        str,
        Field(
            description="Title of the certification section",
            examples=["Professional Certifications", "Technical Certifications"],
        ),
    ]
    certifications: Annotated[
        List[Certification],
        Field(
            description="List of certifications in the section",
            default_factory=list,
            examples=[
                {
                    "name": "Certified Kubernetes Administrator",
                    "issuing_organization": "Cloud Native Computing Foundation",
                    "issue_date": "2021-05-15",
                    "expiration_date": None,
                    "credential_id": "1234567890",
                },
                {
                    "name": "AWS Certified Solutions Architect",
                    "issuing_organization": "Amazon Web Services",
                    "issue_date": "2022-03-01",
                    "expiration_date": "2024-03-01",
                    "credential_id": None,
                },
            ],
        ),
    ]


class ProfessionalProfileStructure(InternalBase):
    """
    Base model for professional profile structure.
    This model is used to define common fields and methods for professional profile schemas.
    """

    contact_info: Annotated[
        ContactInfo,
        Field(
            description="Contact information of the individual",
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
    summary: Annotated[
        str,
        Field(
            description="Summary of the individual's professional profile",
            examples=[
                "Results-driven software engineer with 5+ years of experience in developing scalable web applications.",
                "Creative graphic designer specializing in branding and user experience design.",
            ],
        ),
    ]
    skills: Annotated[
        List[SkillSection],
        Field(
            description="List of skill sections in the profile",
            default_factory=list,
            examples=[
                {
                    "title": "Programming Languages",
                    "skills": [
                        {
                            "name": "Python",
                            "proficiency": SkillProficiency.PROFICIENT,
                            "years_of_experience": 5,
                            "context": "Developed multiple web applications using Django and Flask",
                        },
                        {
                            "name": "JavaScript",
                            "proficiency": SkillProficiency.EXPERIENCED,
                            "years_of_experience": 4,
                            "context": "Built interactive web applications using React and Node.js",
                        },
                    ],
                },
            ],
        ),
    ]
    certifications: Annotated[
        List[CertificationSection],
        Field(
            description="List of certification sections in the profile",
            default_factory=list,
            examples=[
                {
                    "title": "Cloud Certifications",
                    "certifications": [
                        {
                            "name": "Certified Kubernetes Administrator",
                            "issuing_organization": "Cloud Native Computing Foundation",
                            "issue_date": "2021-05-15",
                            "expiration_date": None,
                            "credential_id": "1234567890",
                        },
                        {
                            "name": "AWS Certified Solutions Architect",
                            "issuing_organization": "Amazon Web Services",
                            "issue_date": "2022-03-01",
                            "expiration_date": "2024-03-01",
                            "credential_id": None,
                        },
                    ],
                },
            ],
        ),
    ]
    experience: Annotated[
        List[ExperienceSection],
        Field(
            description="List of work experience sections in the profile",
            default_factory=list,
            examples=[
                {
                    "title": "Professional Experience",
                    "experiences": [
                        {
                            "company_name": "Tech Solutions Inc.",
                            "job_title": "Software Engineer",
                            "start_date": "2020-01-01",
                            "end_date": "2022-01-01",
                            "bullet_points": [
                                "Developed and maintained web applications using Python and Django",
                                "Led a team of developers in building a scalable microservices architecture",
                            ],
                        },
                    ],
                },
            ],
        ),
    ]
    education: Annotated[
        List[EducationSection],
        Field(
            description="List of education sections in the profile",
            default_factory=list,
            examples=[
                {
                    "title": "Educational Qualifications",
                    "education": [
                        {
                            "institution_name": "University of Technology",
                            "degree": "Bachelor of Science in Computer Science",
                            "field_of_study": "Computer Science",
                            "start_date": "2015-09-01",
                            "end_date": "2019-06-01",
                            "bullet_points": [
                                "Completed coursework in Data Structures and Algorithms",
                                "Graduated with honors, top 10% of the class",
                            ],
                        },
                    ],
                },
            ],
        ),
    ]
