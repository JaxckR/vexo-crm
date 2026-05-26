from datetime import datetime
from typing import cast

from vexo.application.ports import IdGenerator
from vexo.domain.entities.organization import OrganizationId
from vexo.domain.entities.permission import Permission
from vexo.domain.entities.role import Role


class RoleFactory:
    def __init__(self, id_generator: IdGenerator) -> None:
        self._id_generator = id_generator

    def create(
        self,
        name: str,
        description: str,
        organization_id: OrganizationId,
        permissions: list[Permission] | None = None,
    ) -> Role:
        return Role(
            id=self._id_generator.generate_role_id(),
            name=name,
            description=description,
            organization_id=organization_id,
            permissions=permissions or [],
            created_at=cast(datetime, cast(object, None)),
            updated_at=None,
        )
