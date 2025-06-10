from typing import Annotated

from pydantic import UUID4, EmailStr, Field

from ..core.enums import UserRole
from .base_schema import InternalBase, MutableInternalBase, RequestBase, ResponseBase


class UserInternalBase(InternalBase):
    pass


class UserMutableInternalBase(MutableInternalBase):
    pass


class UserRequestBase(RequestBase):
    pass


class UserResponseBase(ResponseBase):
    pass


class UserCreateRequest(UserRequestBase):
    username: Annotated[
        str,
        Field(
            description="Unique username for the user",
            min_length=3,
            max_length=50,
        ),
    ]
    email: Annotated[
        EmailStr,
        Field(
            description="Email address of the user",
            max_length=100,
        ),
    ]
    first_name: Annotated[
        str | None,
        Field(
            description="First name of the user",
            max_length=50,
            default=None,
        ),
    ] = None
    last_name: Annotated[
        str | None,
        Field(
            description="Last name of the user",
            max_length=50,
            default=None,
        ),
    ] = None
    password: Annotated[
        str,
        Field(
            description="Password for the user account",
            min_length=8,
            max_length=128,
        ),
    ]


class UserUpdateRequest(UserMutableInternalBase):
    username: Annotated[
        str | None,
        Field(
            description="Unique username for the user",
            min_length=3,
            max_length=50,
            default=None,
        ),
    ] = None
    email: Annotated[
        EmailStr | None,
        Field(
            description="Email address of the user",
            max_length=100,
            default=None,
        ),
    ] = None
    first_name: Annotated[
        str | None,
        Field(
            description="First name of the user",
            max_length=50,
            default=None,
        ),
    ] = None
    last_name: Annotated[
        str | None,
        Field(
            description="Last name of the user",
            max_length=50,
            default=None,
        ),
    ] = None
    role: Annotated[
        UserRole | None,
        Field(
            description="Role of the user in the system",
            default=None,
        ),
    ] = None
    previous_password: Annotated[
        str | None,
        Field(
            description="Previous password for the user account, required for password updates",
            min_length=8,
            max_length=128,
            default=None,
        ),
    ] = None
    new_password: Annotated[
        str | None,
        Field(
            description="New password for the user account, required for password updates",
            min_length=8,
            max_length=128,
            default=None,
        ),
    ] = None


class UserResponse(UserResponseBase):
    id: UUID4 = Field(
        description="Unique identifier for the user",
    )
    username: str = Field(
        description="Unique username for the user",
    )
    email: EmailStr = Field(
        description="Email address of the user",
    )
    first_name: str | None = Field(
        description="First name of the user",
        default=None,
    )
    last_name: str | None = Field(
        description="Last name of the user",
        default=None,
    )
    role: UserRole = Field(
        description="Role of the user in the system",
    )
    is_active: bool = Field(
        description="Indicates if the user account is active",
        default=True,
    )
