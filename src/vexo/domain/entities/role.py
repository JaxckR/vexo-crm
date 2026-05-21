from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from vexo.domain.entities.common import IDEntity, TimeStampEntity
from vexo.domain.entities.organization import OrganizationId
from vexo.domain.entities.permission import PermissionId

RoleId = NewType("RoleId", UUID)
RolePermissionId = NewType("RolePermissionId", int)


@dataclass
class Role(IDEntity[RoleId], TimeStampEntity):
    name: str
    description: str
    organization_id: OrganizationId


@dataclass
class RolePermission(IDEntity[RoleId]):
    role_id: RoleId
    permission_id: PermissionId
