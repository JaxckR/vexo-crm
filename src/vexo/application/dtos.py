from dataclasses import dataclass

from vexo.domain.entities.organization import OrganizationId
from vexo.domain.entities.role import Role
from vexo.domain.entities.user import User


@dataclass(slots=True, frozen=True)
class UserDTO:
    login: str
    email: str
    first_name: str
    last_name: str
    organization_id: OrganizationId
    role: Role

    @staticmethod
    def from_entity(entity: User) -> "UserDTO":
        return UserDTO(
            login=entity.login,
            email=entity.email,
            first_name=entity.first_name,
            last_name=entity.last_name,
            organization_id=entity.organization_id,
            role=entity.role,
        )
