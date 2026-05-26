from sqlalchemy import select, and_

from vexo.application.ports.repositories.role import RoleRepository
from vexo.domain.entities.role import RoleId, Role
from vexo.infrastructure.persistence.adapters.common import SQLAMixin


class RoleRepositoryImpl(SQLAMixin, RoleRepository):
    def add(self, instance: Role) -> None:
        self._session.add(instance)

    async def get(self, id_: RoleId) -> Role | None:
        query = await self._session.execute(select(Role).where(and_(Role.id == id_)))
        return query.scalar_one_or_none()
