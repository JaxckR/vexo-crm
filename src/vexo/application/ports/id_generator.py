from abc import abstractmethod
from typing import Protocol

from vexo.domain.entities.organization import OrganizationId
from vexo.domain.entities.permission import PermissionId
from vexo.domain.entities.role import RoleId
from vexo.domain.entities.session import SessionId
from vexo.domain.entities.user import UserId


class IdGenerator(Protocol):
    @abstractmethod
    def generate_user_id(self) -> UserId: ...

    @abstractmethod
    def generate_session_id(self) -> SessionId: ...

    @abstractmethod
    def generate_organization_id(self) -> OrganizationId: ...

    @abstractmethod
    def generate_permission_id(self) -> PermissionId: ...

    @abstractmethod
    def generate_role_id(self) -> RoleId: ...
