from datetime import datetime
from typing import cast

from vexo.application.ports import IdGenerator
from vexo.domain.entities.session import Session
from vexo.domain.entities.user import UserId


class SessionFactory:
    def __init__(self, id_generator: IdGenerator) -> None:
        self._id_generator = id_generator

    def create(self, user_id: UserId, expires_at: datetime) -> Session:
        return Session(
            id=self._id_generator.generate_session_id(),
            user_id=user_id,
            expires_at=expires_at,
            created_at=cast(datetime, cast(object, None)),
        )
