from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from .base_model import BaseModel

DocumentJobApplication = Table(
    "document_job_application",
    BaseModel.metadata,
    Column("document_id", PG_UUID(as_uuid=True), ForeignKey("document.id"), primary_key=True),
    Column("job_application_id", PG_UUID(as_uuid=True), ForeignKey("job_application.id"), primary_key=True),
)
