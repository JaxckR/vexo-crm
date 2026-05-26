from dataclasses import dataclass

from vexo.application.exceptions import ApplicationException, PermissionDeniedError
from vexo.application.factories.role import RoleFactory
from vexo.application.ports import IdentityProvider, TransactionManager
from vexo.application.ports.repositories.permission import PermissionRepository
from vexo.application.ports.repositories.role import RoleRepository
from vexo.domain.entities.permission import Resource, Action


@dataclass(slots=True, frozen=True)
class CreateRoleRequest:
    name: str
    description: str


@dataclass(slots=True, frozen=True)
class CreateRoleHandler:
    _identity_provider: IdentityProvider
    _permission_repository: PermissionRepository
    _role_factory: RoleFactory
    _role_repository: RoleRepository
    _transaction_manager: TransactionManager

    async def handle(self, request: CreateRoleRequest) -> None:
        user = await self._identity_provider.get_user()

        if user.organization_id is None:
            raise ApplicationException("You're not in organization.")

        if not await self._permission_repository.has_permission(
            user.id, Resource.ROLES, Action.CREATE
        ):
            raise PermissionDeniedError()

        role = self._role_factory.create(
            name=request.name,
            description=request.description,
            organization_id=user.organization_id,
        )

        self._role_repository.add(role)
        await self._transaction_manager.commit()
