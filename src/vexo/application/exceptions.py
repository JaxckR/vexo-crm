from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ApplicationException(Exception):
    message: str = "Application error occurred"


class NotFoundError(ApplicationException): ...


class AlreadyExistsError(ApplicationException): ...


class UnauthorizedError(ApplicationException): ...


class PermissionDeniedError(ApplicationException):
    message: str = "Permission denied"
