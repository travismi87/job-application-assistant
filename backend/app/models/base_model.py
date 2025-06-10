import uuid

from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column

from ..utils.string_formatters import camel_to_snake_case


class BaseModel(DeclarativeBase):
    """
    Base class for all models, providing common functionality.
    """

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """
        Automatically generate the table name in snake_case format.
        """
        return camel_to_snake_case(cls.__name__)

    id: Mapped[uuid.UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
