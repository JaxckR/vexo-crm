from sqlalchemy import select, and_

from vexo.application.ports.repositories.organization import OrganizationRepository
from vexo.domain.entities.organization import Organization, OrganizationId
from vexo.infrastructure.persistence.adapters.common import SQLAMixin


class OrganizationRepositoryImpl(SQLAMixin, OrganizationRepository):
    async def get(self, id_: OrganizationId) -> Organization | None:
        query = await self._session.execute(
            select(Organization).where(and_(Organization.id == id_))
        )
        return query.scalar_one_or_none()

    def add(self, instance: Organization) -> None:
        self._session.add(instance)
