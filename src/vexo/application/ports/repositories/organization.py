from abc import abstractmethod
from typing import Protocol

from vexo.domain.entities.organization import Organization, OrganizationId


class OrganizationRepository(Protocol):
    @abstractmethod
    async def get(self, id_: OrganizationId) -> Organization | None: ...

    @abstractmethod
    def add(self, instance: Organization) -> None: ...
