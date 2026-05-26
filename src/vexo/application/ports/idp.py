from abc import abstractmethod
from typing import Protocol

from vexo.domain.entities.user import UserId, User


class IdentityProvider(Protocol):
    @abstractmethod
    async def get_current_user_id(self) -> UserId: ...

    @abstractmethod
    async def get_user(self) -> User: ...
