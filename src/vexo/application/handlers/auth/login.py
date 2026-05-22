from dataclasses import dataclass
from datetime import datetime, timedelta, UTC

from vexo.application.exceptions import NotFoundError, ApplicationException
from vexo.application.factories.session import SessionFactory
from vexo.application.ports import Verifier, TransactionManager
from vexo.application.ports.repositories.session import SessionRepository
from vexo.application.ports.repositories.user import UserRepository
from vexo.domain.entities.session import Session


@dataclass(slots=True, frozen=True)
class LoginRequest:
    login: str
    password: str


@dataclass(slots=True, frozen=True)
class LoginHandler:
    _user_repository: UserRepository
    _session_repository: SessionRepository
    _session_factory: SessionFactory
    _transaction_manager: TransactionManager
    _verifier: Verifier

    async def handle(self, request: LoginRequest) -> Session:
        user = await self._user_repository.get_by_login(request.login)

        if not user:
            raise NotFoundError("User not found")

        if not self._verifier.verify_password(request.password, user.password_hash):
            raise ApplicationException("Invalid password")

        session = self._session_factory.create(
            user_id=user.id, expires_at=datetime.now(UTC) + timedelta(days=90)
        )
        self._session_repository.add(session)
        await self._transaction_manager.commit()
        return session
