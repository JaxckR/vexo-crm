from dataclasses import dataclass

from vexo.application.ports import TransactionManager
from vexo.application.ports.repositories.session import SessionRepository
from vexo.domain.entities.session import SessionId


@dataclass(slots=True, frozen=True)
class LogoutHandler:
    _session_repository: SessionRepository
    _transaction_manager: TransactionManager

    async def handle(self, session_id: SessionId) -> None:
        await self._session_repository.delete(session_id)
        await self._transaction_manager.commit()
