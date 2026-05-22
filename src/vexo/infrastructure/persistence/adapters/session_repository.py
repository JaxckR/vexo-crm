from sqlalchemy import select, and_, delete

from vexo.application.ports.repositories.session import SessionRepository
from vexo.domain.entities.session import Session, SessionId
from vexo.infrastructure.persistence.adapters.common import SQLAMixin


class SessionRepositoryImpl(SQLAMixin, SessionRepository):
    async def delete(self, id_: SessionId) -> None:
        await self._session.execute(delete(Session).where(and_(Session.id == id_)))

    async def get(self, id_: SessionId) -> Session | None:
        query = await self._session.execute(
            select(Session).where(and_(Session.id == id_))
        )
        return query.scalar_one_or_none()

    def add(self, instance: Session) -> None:
        self._session.add(instance)
