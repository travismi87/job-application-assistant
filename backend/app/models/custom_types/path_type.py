from pathlib import Path

from sqlalchemy.types import String, TypeDecorator


class PathType(TypeDecorator):
    """
    Custom SQLAlchemy type to store pathlib.Path objects as strings in the database.
    """

    impl = String

    def process_bind_param(self, value: Path | None, dialect) -> str | None:
        """
        Convert a Path object to a string for storage in the database.
        """
        return str(value) if value is not None else None

    def process_result_value(self, value: str | None, dialect) -> Path | None:
        """
        Convert a string from the database back to a Path object.
        """
        return Path(value) if value is not None else None
