import re
from datetime import datetime
from re import Pattern
from typing import Final, cast

from vexo.application.exceptions import ApplicationException
from vexo.application.ports import Hasher
from vexo.application.ports.id_generator import IdGenerator
from vexo.domain.entities.user import User


class UserFactory:
    MIN_PASSWORD_LENGTH: Final[int] = 8
    EMAIL_REGEX: Final[Pattern[str]] = re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )
    LOGIN_REGEX: Final[Pattern[str]] = re.compile(
        r"^[a-zA-Z0-9](?:[a-zA-Z0-9_]{1,253}[a-zA-Z0-9])?$"
    )

    def __init__(self, id_generator: IdGenerator, hasher: Hasher) -> None:
        self._id_generator = id_generator
        self._hasher = hasher

    def _validate_password(self, password: str) -> None:
        if len(password) < self.MIN_PASSWORD_LENGTH:
            raise ApplicationException("Password too short")

    def change_password(self, instance: User, new_password: str) -> User:
        self._validate_password(new_password)
        instance.password_hash = self._hasher.hash_password(new_password)
        return instance

    def create(
        self,
        login: str,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
    ) -> User:
        self._validate_password(password)
        if not self.LOGIN_REGEX.match(login):
            raise ApplicationException("Invalid login")

        if not self.EMAIL_REGEX.match(email):
            raise ApplicationException("Invalid email address")

        password_hash = self._hasher.hash_password(password)

        return User(
            id=self._id_generator.generate_user_id(),
            login=login,
            email=email,
            password_hash=password_hash,
            first_name=first_name,
            last_name=last_name,
            organization_id=None,
            is_active=True,
            created_at=cast(datetime, cast(object, None)),
            updated_at=None,
        )
