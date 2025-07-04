from typing import Annotated, List

from pydantic import UUID4, EmailStr, Field

from ..core.enums import UserRole
from .base_schema import InternalBase, MutableInternalBase, RequestBase, ResponseBase


class UserInfo(InternalBase):
    """
    Schema for user information.
    This schema defines the fields related to user details, such as ID, username, email, and role.
    """

    id: UUID4 = Field(
        description="Unique identifier for the user",
        examples=["b3c1e2d4-5678-1234-9abc-1234567890ab"],
    )
    username: str = Field(
        description="Unique username for the user",
        min_length=3,
        max_length=50,
        examples=["johndoe", "janesmith"],
    )
    email: EmailStr = Field(
        description="Email address of the user",
        max_length=100,
        examples=["john.doe@example.com", "jane.smith@example.com"],
    )
    first_name: str | None = Field(
        description="First name of the user",
        max_length=50,
        default=None,
        examples=["John", "Jane"],
    )
    last_name: str | None = Field(
        description="Last name of the user",
        max_length=50,
        default=None,
        examples=["Doe", "Smith"],
    )
    role: UserRole = Field(
        description="Role of the user in the system",
        examples=[UserRole.USER, UserRole.ADMIN],
    )
    is_active: bool = Field(
        description="Indicates if the user account is active",
        default=True,
        examples=[True, False],
    )


class UserCreateRequest(RequestBase):
    """
    Schema for user creation request.
    This schema defines the fields required to create a new user, including username, email, password, and optional first and last names.
    """

    username: Annotated[
        str,
        Field(
            description="Unique username for the user",
            min_length=3,
            max_length=50,
            examples=["johndoe", "janesmith"],
            pattern=r"^[a-zA-Z0-9_]+$",
        ),
    ]
    email: Annotated[
        EmailStr,
        Field(
            description="Email address of the user",
            max_length=100,
            examples=["john.doe@example.com", "jane.smith@example.com"],
        ),
    ]
    first_name: Annotated[
        str | None,
        Field(
            description="First name of the user",
            max_length=50,
            default=None,
            examples=["John", "Jane"],
        ),
    ] = None
    last_name: Annotated[
        str | None,
        Field(
            description="Last name of the user",
            max_length=50,
            default=None,
            examples=["Doe", "Smith"],
        ),
    ] = None
    password: Annotated[
        str,
        Field(
            description="Password for the user account",
            min_length=8,
            max_length=128,
            examples=["StrongPassw0rd!", "Another$ecret123"],
            pattern=r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$%^&*()_+\-=]{8,128}$",
        ),
    ]


class UserUpdateRequest(MutableInternalBase):
    """
    Schema for user update request.
    This schema defines the fields that can be updated for an existing user, including optional fields for username, email, first name, last name, role, and password.
    """

    username: Annotated[
        str | None,
        Field(
            description="Unique username for the user",
            min_length=3,
            max_length=50,
            default=None,
            examples=["johndoe", "janesmith"],
            pattern=r"^[a-zA-Z0-9_]+$",
        ),
    ] = None
    email: Annotated[
        EmailStr | None,
        Field(
            description="Email address of the user",
            max_length=100,
            default=None,
            examples=["john.doe@example.com", "jane.smith@example.com"],
        ),
    ] = None
    first_name: Annotated[
        str | None,
        Field(
            description="First name of the user",
            max_length=50,
            default=None,
            examples=["John", "Jane"],
        ),
    ] = None
    last_name: Annotated[
        str | None,
        Field(
            description="Last name of the user",
            max_length=50,
            default=None,
            examples=["Doe", "Smith"],
        ),
    ] = None
    role: Annotated[
        UserRole | None,
        Field(
            description="Role of the user in the system",
            default=None,
            examples=[UserRole.USER, UserRole.ADMIN],
        ),
    ] = None
    previous_password: Annotated[
        str | None,
        Field(
            description="Previous password for the user account, required for password updates",
            min_length=8,
            max_length=128,
            default=None,
            examples=["OldPassw0rd!"],
            pattern=r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$%^&*()_+\-=]{8,128}$",
        ),
    ] = None
    new_password: Annotated[
        str | None,
        Field(
            description="New password for the user account, required for password updates",
            min_length=8,
            max_length=128,
            default=None,
            examples=["NewStr0ngPass!"],
            pattern=r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d!@#$%^&*()_+\-=]{8,128}$",
        ),
    ] = None


class UserInfoResponse(ResponseBase):
    """
    Schema for user information response.
    This schema defines the fields returned in the response for user information retrieval.
    """

    users: Annotated[
        List[UserInfo],
        Field(
            description="List or single user information",
            examples=[
                [
                    {
                        "id": "b3c1e2d4-5678-1234-9abc-1234567890ab",
                        "username": "johndoe",
                        "email": "john.doe@example.com",
                    }
                ]
            ],
        ),
    ]


class UserIdResponse(ResponseBase):
    """
    Schema for user ID response.
    This schema defines the fields returned in the response for user ID retrieval.
    """

    ids: Annotated[
        List[UUID4],
        Field(
            description="List or single user IDs",
            examples=[["b3c1e2d4-5678-1234-9abc-1234567890ab"]],
        ),
    ]
