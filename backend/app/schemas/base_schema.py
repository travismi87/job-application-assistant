from pydantic import AliasGenerator, BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class InternalBase(BaseModel):
    """
    Base model for internal schemas.
    This model is used to define common fields and methods for internal schemas.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        frozen=True,
        use_enum_values=False,
        populate_by_name=True,
    )


class MutableInternalBase(InternalBase):
    """
    Mutable base model for internal schemas.
    This model allows modification of fields after instantiation.
    """

    model_config = InternalBase.model_config.copy()
    model_config.update(
        frozen=False,
    )


class RequestBase(BaseModel):
    """
    Base model for request schemas.
    This model is used to define common fields and methods for request schemas.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        alias_generator=AliasGenerator(
            validation_alias=to_camel,
            serialization_alias=to_camel,
        ),
        populate_by_name=True,
        use_enum_values=True,
    )


class ResponseBase(BaseModel):
    """
    Base model for response schemas.
    This model is used to define common fields and methods for response schemas.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        alias_generator=to_camel,
        populate_by_name=True,
        use_enum_values=True,
    )
