from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from vexo.domain.entities.common import IDEntity, TimeStampEntity
from vexo.domain.entities.organization import OrganizationId
from vexo.domain.entities.role import RoleId

UserId = NewType("UserId", UUID)
UserRoleId = NewType("UserRoleId", int)


@dataclass
class User(IDEntity[UserId], TimeStampEntity):
    login: str
    email: str
    password_hash: str
    first_name: str
    last_name: str
    is_active: bool
    organization_id: OrganizationId | None


@dataclass
class UserRole(IDEntity[UserRoleId], TimeStampEntity):
    user_id: UserId
    role_id: RoleId
