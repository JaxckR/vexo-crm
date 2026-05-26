from abc import abstractmethod
from typing import Protocol

from vexo.domain.entities.permission import Resource, Action, Permission
from vexo.domain.entities.user import UserId


class PermissionRepository(Protocol):
    @abstractmethod
    def add(self, instance: Permission) -> None: ...

    @abstractmethod
    async def get_all(self) -> list[Permission]: ...

    @abstractmethod
    async def exists(self, resource: Resource, action: Action) -> bool: ...

    @abstractmethod
    async def has_permission(
        self, user_id: UserId, resource: Resource, action: Action
    ) -> bool: ...
