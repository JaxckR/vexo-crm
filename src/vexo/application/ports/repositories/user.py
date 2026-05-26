from abc import abstractmethod
from typing import Protocol

from vexo.domain.entities.user import User, UserId, UserRole


class UserRepository(Protocol):
    @abstractmethod
    async def add(self, instance: User) -> None: ...

    @abstractmethod
    async def get(self, id_: UserId) -> User | None: ...

    @abstractmethod
    async def get_by_login(self, login: str) -> User | None: ...


class UserRoleRepository(Protocol):
    @abstractmethod
    def add(self, instance: UserRole) -> None: ...
