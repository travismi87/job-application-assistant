"""
Base exception classes for the application.

Define shared custom exception types here for reuse across the project.
"""


class AppBaseException(Exception):
    """Base exception for all custom exceptions in the application."""

    pass


class ConfigurationError(AppBaseException):
    """Raised when there is a configuration-related error."""

    pass


class ValidationError(AppBaseException):
    """Raised when input validation fails."""

    def __init__(self, message: str = "Validation failed."):
        super().__init__(message)


class NotFoundError(AppBaseException):
    """Raised when a requested resource is not found."""

    def __init__(self, resource: str = "Resource", detail: str = "not found."):
        super().__init__(f"{resource} {detail}")


class PermissionDeniedError(AppBaseException):
    """Raised when a user does not have permission to perform an action."""

    def __init__(self, message: str = "Permission denied."):
        super().__init__(message)


class ExternalServiceError(AppBaseException):
    """Raised when an external service/API call fails."""

    def __init__(self, service: str = "External service", detail: str = "error."):
        super().__init__(f"{service}: {detail}")


class DatabaseError(AppBaseException):
    """Raised when a database operation fails."""

    def __init__(self, message: str = "Database operation failed."):
        super().__init__(message)


class DuplicateResourceError(AppBaseException):
    """Raised when attempting to create a resource that already exists."""

    def __init__(self, resource: str = "Resource", detail: str = "already exists."):
        super().__init__(f"{resource} {detail}")


class AuthenticationError(AppBaseException):
    """Raised when authentication fails."""

    def __init__(self, message: str = "Authentication failed."):
        super().__init__(message)


class RateLimitExceededError(AppBaseException):
    """Raised when a user exceeds the allowed rate limit."""

    def __init__(self, message: str = "Rate limit exceeded."):
        super().__init__(message)


class BusinessRuleViolationError(AppBaseException):
    """Raised when a business rule or domain logic is violated."""

    def __init__(self, rule: str = "Business rule", detail: str = "was violated."):
        super().__init__(f"{rule} {detail}")
