import datetime
from typing import Annotated

from pydantic import BaseModel, Field


class DateRangeMixin(BaseModel):
    """
    Mixin for date range fields.
    This mixin is used to define common date range fields for various schemas.
    """

    start_date: Annotated[
        datetime.date,
        Field(
            description="Start date of the range",
            examples=["2023-01-01", "2023-12-31"],
        ),
    ]
    end_date: Annotated[
        datetime.date,
        Field(
            description="End date of the range",
            examples=["2023-01-31", "2023-12-31"],
        ),
    ]
