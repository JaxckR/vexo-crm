from datetime import datetime, UTC

from starlette.requests import Request

from vexo.application.exceptions import UnauthorizedError
from vexo.application.ports import IdentityProvider
from vexo.application.ports.repositories.session import SessionRepository
from vexo.domain.entities.session import SessionId
from vexo.domain.entities.user import UserId


class IdentityProviderImpl(IdentityProvider):
    def __init__(self, request: Request, session_repository: SessionRepository) -> None:
        self._request = request
        self._session_repository = session_repository

    async def get_current_user_id(self) -> UserId:
        session_id = self._request.cookies.get("session_id")

        if session_id is None:
            raise UnauthorizedError("You are not logged in")

        session = await self._session_repository.get(SessionId(session_id))

        if session is None:
            raise UnauthorizedError("You are not logged in")

        if session.expires_at < datetime.now(UTC):
            raise UnauthorizedError("You are not logged in")

        return session.user_id
