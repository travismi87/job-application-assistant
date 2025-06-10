from .base_schema import InternalBase, MutableInternalBase, RequestBase, ResponseBase


class DocumentInternalBase(InternalBase):
    """
    Base model for internal document schemas.
    This model is used to define common fields and methods for internal document schemas.
    """

    pass


class DocumentMutableInternalBase(MutableInternalBase):
    """
    Mutable base model for internal document schemas.
    This model allows modification of fields after instantiation.
    """

    pass


class DocumentRequestBase(RequestBase):
    """
    Base model for document request schemas.
    This model is used to define common fields and methods for document request schemas.
    """

    pass


class DocumentResponseBase(ResponseBase):
    """
    Base model for document response schemas.
    This model is used to define common fields and methods for document response schemas.
    """

    pass
