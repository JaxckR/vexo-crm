from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from vexo.domain.entities.common import IDEntity, TimeStampEntity

OrganizationId = NewType("OrganizationId", UUID)


@dataclass
class Organization(IDEntity[OrganizationId], TimeStampEntity):
    name: str
