"""Update job application model: add assistant_current_step, improve relationships, and adjust nullable fields

Revision ID: 1191d0464e85
Revises: d985138e2cb8
Create Date: 2025-06-13 18:33:33.820036

"""

from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1191d0464e85"
down_revision: Union[str, None] = "d985138e2cb8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###

    assistant_step_type = postgresql.ENUM(
        "PENDING",
        "INITIAL_SYNTHESIS",
        "MASTER_LIST",
        "CANDIDATE_VALIDATION",
        "TAILORED_RESUME",
        "TAILORED_COVER_LETTER",
        "HIRING_MANAGER_REVIEW",
        "LINKEDIN_OPTIMIZATION",
        "INTERVIEW_PREPARATION",
        "SKILL_DEVELOPMENT_PLAN",
        "FINAL_CHECKLIST",
        name="assistant_step_type",
    )
    assistant_step_type.create(op.get_bind(), checkfirst=True)

    assistant_step_status = postgresql.ENUM(
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
        "NOT_STARTED",
        "WAITING_FOR_USER_INPUT",
        name="assistant_step_status",
    )
    assistant_step_status.create(op.get_bind(), checkfirst=True)

    document_type = postgresql.ENUM(
        "RESUME",
        "COVER_LETTER",
        "SUPPORTING_DOCUMENT",
        "MASTER_LIST",
        "JOB_DESCRIPTION",
        "GENERAL",
        name="document_type",
    )
    document_type.create(op.get_bind(), checkfirst=True)

    mime_type = postgresql.ENUM(
        "PDF",
        "DOCX",
        "DOC",
        "CSV",
        "XLSX",
        "XLS",
        "PPTX",
        "PPT",
        "ODT",
        "ODS",
        "ODP",
        "RTF",
        "XML",
        "YAML",
        "MARKDOWN",
        "TXT",
        "HTML",
        "JSON",
        "UNKNOWN",
        name="mime_type",
    )
    mime_type.create(op.get_bind(), checkfirst=True)

    file_type = postgresql.ENUM(
        "PDF",
        "DOCX",
        "DOC",
        "CSV",
        "XLSX",
        "XLS",
        "PPTX",
        "PPT",
        "ODT",
        "ODS",
        "ODP",
        "RTF",
        "XML",
        "YAML",
        "MARKDOWN",
        "TXT",
        "HTML",
        "JSON",
        "UNKNOWN",
        name="file_type",
    )
    file_type.create(op.get_bind(), checkfirst=True)

    document_status = postgresql.ENUM(
        "PENDING",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
        "NOT_STARTED",
        "WAITING_FOR_USER_INPUT",
        name="document_status",
    )
    document_status.create(op.get_bind(), checkfirst=True)

    document_visibility = postgresql.ENUM(
        "PUBLIC",
        "PRIVATE",
        "INTERNAL",
        name="document_visibility",
    )
    document_visibility.create(op.get_bind(), checkfirst=True)

    document_source = postgresql.ENUM(
        "USER_UPLOAD",
        "SYSTEM_GENERATED",
        "EXTERNAL",
        name="document_source",
    )
    document_source.create(op.get_bind(), checkfirst=True)

    document_version = postgresql.ENUM(
        "V1",
        "V2",
        "V3",
        name="document_version",
    )
    document_version.create(op.get_bind(), checkfirst=True)

    job_type = postgresql.ENUM(
        "FULL_TIME",
        "PART_TIME",
        "CONTRACT",
        "INTERNSHIP",
        name="job_type",
    )
    job_type.create(op.get_bind(), checkfirst=True)

    job_application_status = postgresql.ENUM(
        "PENDING",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
        "NOT_STARTED",
        "WAITING_FOR_USER_INPUT",
        name="job_application_status",
    )
    job_application_status.create(op.get_bind(), checkfirst=True)

    sso_provider = postgresql.ENUM(
        "GOOGLE",
        "MICROSOFT",
        "LINKEDIN",
        "GITHUB",
        name="sso_provider",
    )
    sso_provider.create(op.get_bind(), checkfirst=True)

    op.alter_column(
        "assistant_step",
        "step_name",
        existing_type=postgresql.ENUM(
            "INITIAL",
            "MASTER_LIST",
            "TAILORED_RESUME",
            "TAILORED_COVER_LETTER",
            "CANDIDATE_VALIDATION",
            "APPLICATION_TIPS",
            "HIRING_MANAGER_REVIEW",
            name="assistantsteptype",
        ),
        type_=postgresql.ENUM(
            "PENDING",
            "INITIAL_SYNTHESIS",
            "MASTER_LIST",
            "CANDIDATE_VALIDATION",
            "TAILORED_RESUME",
            "TAILORED_COVER_LETTER",
            "HIRING_MANAGER_REVIEW",
            "LINKEDIN_OPTIMIZATION",
            "INTERVIEW_PREPARATION",
            "SKILL_DEVELOPMENT_PLAN",
            "FINAL_CHECKLIST",
            name="assistant_step_type",
        ),
        existing_nullable=False,
        postgresql_using="step_name::text::assistant_step_type",
    )
    op.alter_column(
        "assistant_step",
        "step_status",
        existing_type=postgresql.ENUM(
            "IN_PROGRESS", "COMPLETED", "FAILED", "CANCELLED", "NOT_STARTED", name="assistantstepstatus"
        ),
        type_=postgresql.ENUM(
            "IN_PROGRESS",
            "COMPLETED",
            "FAILED",
            "CANCELLED",
            "NOT_STARTED",
            "WAITING_FOR_USER_INPUT",
            name="assistant_step_status",
        ),
        existing_nullable=False,
        postgresql_using="step_status::text::assistant_step_status",
    )
    op.alter_column(
        "document",
        "type",
        existing_type=postgresql.ENUM(
            "RESUME",
            "COVER_LETTER",
            "SUPPORTING_DOCUMENT",
            "MASTER_LIST",
            "JOB_DESCRIPTION",
            "GENERAL",
            name="documenttype",
        ),
        type_=postgresql.ENUM(
            "RESUME",
            "COVER_LETTER",
            "SUPPORTING_DOCUMENT",
            "MASTER_LIST",
            "JOB_DESCRIPTION",
            "GENERAL",
            name="document_type",
        ),
        existing_nullable=False,
        postgresql_using="type::text::document_type",
    )
    op.alter_column(
        "document",
        "mime_type",
        existing_type=postgresql.ENUM(
            "PDF",
            "DOCX",
            "DOC",
            "CSV",
            "XLSX",
            "XLS",
            "PPTX",
            "PPT",
            "ODT",
            "ODS",
            "ODP",
            "RTF",
            "XML",
            "YAML",
            "MARKDOWN",
            "TXT",
            "HTML",
            "JSON",
            "UNKNOWN",
            name="mimetype",
        ),
        type_=postgresql.ENUM(
            "PDF",
            "DOCX",
            "DOC",
            "CSV",
            "XLSX",
            "XLS",
            "PPTX",
            "PPT",
            "ODT",
            "ODS",
            "ODP",
            "RTF",
            "XML",
            "YAML",
            "MARKDOWN",
            "TXT",
            "HTML",
            "JSON",
            "UNKNOWN",
            name="mime_type",
        ),
        existing_nullable=True,
        postgresql_using="mime_type::text::mime_type",
    )
    op.alter_column(
        "document",
        "file_type",
        existing_type=postgresql.ENUM(
            "PDF",
            "DOCX",
            "DOC",
            "CSV",
            "XLSX",
            "XLS",
            "PPTX",
            "PPT",
            "ODT",
            "ODS",
            "ODP",
            "RTF",
            "XML",
            "YAML",
            "MARKDOWN",
            "TXT",
            "HTML",
            "JSON",
            "UNKNOWN",
            name="filetype",
        ),
        type_=postgresql.ENUM(
            "PDF",
            "DOCX",
            "DOC",
            "CSV",
            "XLSX",
            "XLS",
            "PPTX",
            "PPT",
            "ODT",
            "ODS",
            "ODP",
            "RTF",
            "XML",
            "YAML",
            "MARKDOWN",
            "TXT",
            "HTML",
            "JSON",
            "UNKNOWN",
            name="file_type",
        ),
        existing_nullable=True,
        postgresql_using="file_type::text::file_type",
    )
    op.alter_column(
        "document",
        "status",
        existing_type=postgresql.ENUM(
            "UPLOADED",
            "PROCESSING",
            "PARSED",
            "VALIDATED",
            "ERROR",
            "ARCHIVED",
            "PENDING",
            name="documentstatus",
        ),
        type_=postgresql.ENUM(
            "UPLOADED",
            "PROCESSING",
            "PARSED",
            "VALIDATED",
            "ERROR",
            "ARCHIVED",
            "PENDING",
            name="document_status",
        ),
        existing_nullable=False,
        postgresql_using="status::text::document_status",
    )
    op.alter_column(
        "document",
        "visibility",
        existing_type=postgresql.ENUM(
            "PUBLIC", "PRIVATE", "INTERNAL", "CONFIDENTIAL", name="documentvisibility"
        ),
        type_=postgresql.ENUM("PUBLIC", "PRIVATE", "INTERNAL", "CONFIDENTIAL", name="document_visibility"),
        existing_nullable=False,
        postgresql_using="visibility::text::document_visibility",
    )
    op.alter_column(
        "document",
        "source",
        existing_type=postgresql.ENUM(
            "USER_UPLOAD", "EMAIL", "EXTERNAL_API", "SCRAPED", "IMPORTED", "GENERATED", name="documentsource"
        ),
        type_=postgresql.ENUM(
            "USER_UPLOAD", "EMAIL", "EXTERNAL_API", "SCRAPED", "IMPORTED", "GENERATED", name="document_source"
        ),
        existing_nullable=False,
        postgresql_using="source::text::document_source",
    )
    op.alter_column(
        "document",
        "version",
        existing_type=postgresql.ENUM(
            "DRAFT", "FINAL", "REVISED", "ARCHIVED", "TEMPLATE", name="documentversion"
        ),
        type_=postgresql.ENUM("DRAFT", "FINAL", "REVISED", "ARCHIVED", "TEMPLATE", name="document_version"),
        existing_nullable=True,
        postgresql_using="version::text::document_version",
    )
    op.add_column(
        "job_application",
        sa.Column(
            "assistant_status",
            postgresql.ENUM(
                "IN_PROGRESS",
                "COMPLETED",
                "FAILED",
                "CANCELLED",
                "NOT_STARTED",
                "WAITING_FOR_USER_INPUT",
                name="assistant_step_status",
            ),
            nullable=False,
        ),
    )
    op.add_column(
        "job_application",
        sa.Column(
            "assistant_current_step",
            postgresql.ENUM(
                "PENDING",
                "INITIAL_SYNTHESIS",
                "MASTER_LIST",
                "CANDIDATE_VALIDATION",
                "TAILORED_RESUME",
                "TAILORED_COVER_LETTER",
                "HIRING_MANAGER_REVIEW",
                "LINKEDIN_OPTIMIZATION",
                "INTERVIEW_PREPARATION",
                "SKILL_DEVELOPMENT_PLAN",
                "FINAL_CHECKLIST",
                name="assistant_step_type",
            ),
            nullable=False,
        ),
    )
    op.alter_column(
        "job_application",
        "type",
        existing_type=postgresql.ENUM(
            "FULL_TIME", "PART_TIME", "CONTRACT", "INTERNSHIP", "TEMPORARY", "FREELANCE", name="jobtype"
        ),
        type_=postgresql.ENUM(
            "FULL_TIME", "PART_TIME", "CONTRACT", "INTERNSHIP", "TEMPORARY", "FREELANCE", name="job_type"
        ),
        existing_nullable=False,
        postgresql_using="type::text::job_type",
    )
    op.alter_column(
        "job_application",
        "application_status",
        existing_type=postgresql.ENUM(
            "APPLIED",
            "INTERVIEW_SCHEDULED",
            "OFFERED",
            "REJECTED",
            "ACCEPTED",
            "WITHDRAWN",
            "PENDING",
            name="jobapplicationstatus",
        ),
        type_=postgresql.ENUM(
            "APPLIED",
            "INTERVIEW_SCHEDULED",
            "OFFERED",
            "REJECTED",
            "ACCEPTED",
            "WITHDRAWN",
            "PENDING",
            name="job_application_status",
        ),
        existing_nullable=False,
        postgresql_using="application_status::text::job_application_status",
    )
    op.alter_column(
        "user",
        "sso_provider",
        existing_type=postgresql.ENUM(
            "GOOGLE",
            "MICROSOFT",
            "GITHUB",
            "FACEBOOK",
            "OKTA",
            "DISCORD",
            "APPLE",
            "CUSTOM",
            name="ssoprovider",
        ),
        type_=postgresql.ENUM(
            "GOOGLE",
            "MICROSOFT",
            "GITHUB",
            "FACEBOOK",
            "OKTA",
            "DISCORD",
            "APPLE",
            "CUSTOM",
            name="sso_provider",
        ),
        existing_nullable=True,
        postgresql_using="sso_provider::text::sso_provider",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "user",
        "sso_provider",
        existing_type=postgresql.ENUM(
            "GOOGLE",
            "MICROSOFT",
            "GITHUB",
            "FACEBOOK",
            "OKTA",
            "DISCORD",
            "APPLE",
            "CUSTOM",
            name="sso_provider",
        ),
        type_=postgresql.ENUM(
            "GOOGLE",
            "MICROSOFT",
            "GITHUB",
            "FACEBOOK",
            "OKTA",
            "DISCORD",
            "APPLE",
            "CUSTOM",
            name="ssoprovider",
        ),
        existing_nullable=True,
    )
    op.alter_column(
        "job_application",
        "application_status",
        existing_type=postgresql.ENUM(
            "APPLIED",
            "INTERVIEW_SCHEDULED",
            "OFFERED",
            "REJECTED",
            "ACCEPTED",
            "WITHDRAWN",
            "PENDING",
            name="job_application_status",
        ),
        type_=postgresql.ENUM(
            "APPLIED",
            "INTERVIEW_SCHEDULED",
            "OFFERED",
            "REJECTED",
            "ACCEPTED",
            "WITHDRAWN",
            "PENDING",
            name="jobapplicationstatus",
        ),
        existing_nullable=False,
    )
    op.alter_column(
        "job_application",
        "type",
        existing_type=postgresql.ENUM(
            "FULL_TIME", "PART_TIME", "CONTRACT", "INTERNSHIP", "TEMPORARY", "FREELANCE", name="job_type"
        ),
        type_=postgresql.ENUM(
            "FULL_TIME", "PART_TIME", "CONTRACT", "INTERNSHIP", "TEMPORARY", "FREELANCE", name="jobtype"
        ),
        existing_nullable=False,
    )
    op.drop_column("job_application", "assistant_current_step")
    op.drop_column("job_application", "assistant_status")
    op.alter_column(
        "document",
        "version",
        existing_type=postgresql.ENUM(
            "DRAFT", "FINAL", "REVISED", "ARCHIVED", "TEMPLATE", name="document_version"
        ),
        type_=postgresql.ENUM("DRAFT", "FINAL", "REVISED", "ARCHIVED", "TEMPLATE", name="documentversion"),
        existing_nullable=True,
    )
    op.alter_column(
        "document",
        "source",
        existing_type=postgresql.ENUM(
            "USER_UPLOAD", "EMAIL", "EXTERNAL_API", "SCRAPED", "IMPORTED", "GENERATED", name="document_source"
        ),
        type_=postgresql.ENUM(
            "USER_UPLOAD", "EMAIL", "EXTERNAL_API", "SCRAPED", "IMPORTED", "GENERATED", name="documentsource"
        ),
        existing_nullable=False,
    )
    op.alter_column(
        "document",
        "visibility",
        existing_type=postgresql.ENUM(
            "PUBLIC", "PRIVATE", "INTERNAL", "CONFIDENTIAL", name="document_visibility"
        ),
        type_=postgresql.ENUM("PUBLIC", "PRIVATE", "INTERNAL", "CONFIDENTIAL", name="documentvisibility"),
        existing_nullable=False,
    )
    op.alter_column(
        "document",
        "status",
        existing_type=postgresql.ENUM(
            "UPLOADED",
            "PROCESSING",
            "PARSED",
            "VALIDATED",
            "ERROR",
            "ARCHIVED",
            "PENDING",
            name="document_status",
        ),
        type_=postgresql.ENUM(
            "UPLOADED",
            "PROCESSING",
            "PARSED",
            "VALIDATED",
            "ERROR",
            "ARCHIVED",
            "PENDING",
            name="documentstatus",
        ),
        existing_nullable=False,
    )
    op.alter_column(
        "document",
        "file_type",
        existing_type=postgresql.ENUM(
            "PDF",
            "DOCX",
            "DOC",
            "CSV",
            "XLSX",
            "XLS",
            "PPTX",
            "PPT",
            "ODT",
            "ODS",
            "ODP",
            "RTF",
            "XML",
            "YAML",
            "MARKDOWN",
            "TXT",
            "HTML",
            "JSON",
            "UNKNOWN",
            name="file_type",
        ),
        type_=postgresql.ENUM(
            "PDF",
            "DOCX",
            "DOC",
            "CSV",
            "XLSX",
            "XLS",
            "PPTX",
            "PPT",
            "ODT",
            "ODS",
            "ODP",
            "RTF",
            "XML",
            "YAML",
            "MARKDOWN",
            "TXT",
            "HTML",
            "JSON",
            "UNKNOWN",
            name="filetype",
        ),
        existing_nullable=True,
    )
    op.alter_column(
        "document",
        "mime_type",
        existing_type=postgresql.ENUM(
            "PDF",
            "DOCX",
            "DOC",
            "CSV",
            "XLSX",
            "XLS",
            "PPTX",
            "PPT",
            "ODT",
            "ODS",
            "ODP",
            "RTF",
            "XML",
            "YAML",
            "MARKDOWN",
            "TXT",
            "HTML",
            "JSON",
            "UNKNOWN",
            name="mime_type",
        ),
        type_=postgresql.ENUM(
            "PDF",
            "DOCX",
            "DOC",
            "CSV",
            "XLSX",
            "XLS",
            "PPTX",
            "PPT",
            "ODT",
            "ODS",
            "ODP",
            "RTF",
            "XML",
            "YAML",
            "MARKDOWN",
            "TXT",
            "HTML",
            "JSON",
            "UNKNOWN",
            name="mimetype",
        ),
        existing_nullable=True,
    )
    op.alter_column(
        "document",
        "type",
        existing_type=postgresql.ENUM(
            "RESUME",
            "COVER_LETTER",
            "SUPPORTING_DOCUMENT",
            "MASTER_LIST",
            "JOB_DESCRIPTION",
            "GENERAL",
            name="document_type",
        ),
        type_=postgresql.ENUM(
            "RESUME",
            "COVER_LETTER",
            "SUPPORTING_DOCUMENT",
            "MASTER_LIST",
            "JOB_DESCRIPTION",
            "GENERAL",
            name="documenttype",
        ),
        existing_nullable=False,
    )
    op.alter_column(
        "assistant_step",
        "step_status",
        existing_type=postgresql.ENUM(
            "IN_PROGRESS",
            "COMPLETED",
            "FAILED",
            "CANCELLED",
            "NOT_STARTED",
            "WAITING_FOR_USER_INPUT",
            name="assistant_step_status",
        ),
        type_=postgresql.ENUM(
            "IN_PROGRESS", "COMPLETED", "FAILED", "CANCELLED", "NOT_STARTED", name="assistantstepstatus"
        ),
        existing_nullable=False,
    )
    op.alter_column(
        "assistant_step",
        "step_name",
        existing_type=postgresql.ENUM(
            "PENDING",
            "INITIAL_SYNTHESIS",
            "MASTER_LIST",
            "CANDIDATE_VALIDATION",
            "TAILORED_RESUME",
            "TAILORED_COVER_LETTER",
            "HIRING_MANAGER_REVIEW",
            "LINKEDIN_OPTIMIZATION",
            "INTERVIEW_PREPARATION",
            "SKILL_DEVELOPMENT_PLAN",
            "FINAL_CHECKLIST",
            name="assistant_step_type",
        ),
        type_=postgresql.ENUM(
            "INITIAL",
            "MASTER_LIST",
            "TAILORED_RESUME",
            "TAILORED_COVER_LETTER",
            "CANDIDATE_VALIDATION",
            "APPLICATION_TIPS",
            "HIRING_MANAGER_REVIEW",
            name="assistantsteptype",
        ),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
