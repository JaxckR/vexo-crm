from secrets import token_urlsafe

from uuid_extensions import uuid7

from vexo.application.ports.id_generator import IdGenerator
from vexo.domain.entities.organization import OrganizationId
from vexo.domain.entities.permission import PermissionId
from vexo.domain.entities.role import RoleId
from vexo.domain.entities.session import SessionId
from vexo.domain.entities.user import UserId


class IdGeneratorImpl(IdGenerator):
    def generate_user_id(self) -> UserId:
        return UserId(uuid7())

    def generate_organization_id(self) -> OrganizationId:
        return OrganizationId(uuid7())

    def generate_session_id(self) -> SessionId:
        return SessionId(token_urlsafe(32))

    def generate_permission_id(self) -> PermissionId:
        return PermissionId(uuid7())

    def generate_role_id(self) -> RoleId:
        return RoleId(uuid7())
