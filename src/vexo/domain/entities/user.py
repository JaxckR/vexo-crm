from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from vexo.domain.entities.common import IDEntity, TimeStampEntity
from vexo.domain.entities.organization import OrganizationId
from vexo.domain.entities.role import Role

UserId = NewType("UserId", UUID)


@dataclass
class User(IDEntity[UserId], TimeStampEntity):
    login: str
    email: str
    password_hash: str
    first_name: str
    last_name: str
    organization_id: OrganizationId
    role: Role
