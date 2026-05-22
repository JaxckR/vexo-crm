from abc import abstractmethod
from typing import Protocol

from vexo.domain.entities.session import Session, SessionId


class SessionRepository(Protocol):
    @abstractmethod
    def add(self, instance: Session) -> None: ...

    @abstractmethod
    async def get(self, id_: SessionId) -> Session | None: ...

    @abstractmethod
    async def delete(self, id_: SessionId) -> None: ...
