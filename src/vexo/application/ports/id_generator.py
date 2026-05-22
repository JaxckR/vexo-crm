from abc import abstractmethod
from typing import Protocol

from vexo.domain.entities.session import SessionId
from vexo.domain.entities.user import UserId


class IdGenerator(Protocol):
    @abstractmethod
    def generate_user_id(self) -> UserId: ...

    @abstractmethod
    def generate_session_id(self) -> SessionId: ...
