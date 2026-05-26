from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from vexo.domain.entities.common import IDEntity, TimeStampEntity
from vexo.domain.entities.organization import OrganizationId
from vexo.domain.entities.permission import PermissionId, Permission, Action, Resource

RoleId = NewType("RoleId", UUID)
RolePermissionId = NewType("RolePermissionId", int)


@dataclass
class Role(IDEntity[RoleId], TimeStampEntity):
    name: str
    description: str
    organization_id: OrganizationId

    permissions: list[Permission]

    def has_permissions(self, resource: Resource, action: Action) -> bool:
        for permission in self.permissions:
            if resource == permission.resource and action == permission.action:
                return True
        return False


@dataclass
class RolePermission(IDEntity[RoleId]):
    role_id: RoleId
    permission_id: PermissionId
