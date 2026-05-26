from abc import abstractmethod
from typing import Protocol

from vexo.domain.entities.role import RoleId, Role


class RoleRepository(Protocol):
    @abstractmethod
    def add(self, instance: Role) -> None: ...

    @abstractmethod
    async def get(self, id_: RoleId) -> Role | None: ...
