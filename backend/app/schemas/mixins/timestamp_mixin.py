import datetime
from typing import Annotated

from pydantic import BaseModel, Field


class TimestampMixin(BaseModel):
    """
    Mixin for timestamp fields.
    This mixin is used to define common timestamp fields for various schemas.
    """

    created_at: Annotated[
        datetime.datetime,
        Field(
            description="Timestamp when the resource was created",
            examples=["2023-01-01T12:00:00Z", "2023-12-31T23:59:59Z"],
        ),
    ]
    updated_at: Annotated[
        datetime.datetime,
        Field(
            description="Timestamp when the resource was last updated",
            examples=["2023-01-01T12:00:00Z", "2023-12-31T23:59:59Z"],
        ),
    ]
