from dataclasses import dataclass
from enum import StrEnum
from typing import Final, NewType
from uuid import UUID

from vexo.domain.entities.common import IDEntity

PermissionId = NewType("PermissionId", UUID)


class Action(StrEnum):
    READ = "read"
    CREATE = "create"
    DELETE = "delete"
    UPDATE = "update"
    IMPORT = "import"
    EXPORT = "export"


class Resource(StrEnum):
    USERS = "users"


@dataclass
class Permission(IDEntity[PermissionId]):
    resource: Resource
    action: Action


RESOURCE_ACTIONS: Final[dict[Resource, list[Action]]] = {
    Resource.USERS: [Action.READ, Action.CREATE, Action.UPDATE, Action.DELETE]
}
