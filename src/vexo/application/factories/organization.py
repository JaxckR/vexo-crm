from datetime import datetime
from typing import cast

from vexo.application.ports import IdGenerator
from vexo.domain.entities.organization import Organization


class OrganizationFactory:
    def __init__(self, id_generator: IdGenerator) -> None:
        self._id_generator = id_generator

    def create(self, name: str) -> Organization:
        return Organization(
            id=self._id_generator.generate_organization_id(),
            name=name,
            created_at=cast(datetime, cast(object, None)),
            updated_at=None,
        )
