from dataclasses import dataclass
from datetime import datetime
from typing import NewType

from vexo.domain.entities.common import IDEntity
from vexo.domain.entities.user import UserId

SessionId = NewType("SessionId", str)


@dataclass
class Session(IDEntity[SessionId]):
    user_id: UserId
    created_at: datetime
    expires_at: datetime
