from dataclasses import dataclass
from datetime import datetime
from typing import cast

from vexo.application.exceptions import ApplicationException
from vexo.application.factories.organization import OrganizationFactory
from vexo.application.factories.role import RoleFactory
from vexo.application.ports import TransactionManager, IdentityProvider
from vexo.application.ports.repositories.organization import OrganizationRepository
from vexo.application.ports.repositories.permission import PermissionRepository
from vexo.application.ports.repositories.role import RoleRepository
from vexo.application.ports.repositories.user import UserRoleRepository
from vexo.domain.entities.user import UserRole


@dataclass(slots=True, frozen=True)
class CreateOrganizationRequest:
    name: str


@dataclass(slots=True, frozen=True)
class CreateOrganizationHandler:
    _organization_repository: OrganizationRepository
    _organization_factory: OrganizationFactory
    _permission_repository: PermissionRepository
    _role_factory: RoleFactory
    _role_repository: RoleRepository
    _user_role_repository: UserRoleRepository
    _identity_provider: IdentityProvider
    _transaction_manager: TransactionManager

    async def handle(self, request: CreateOrganizationRequest) -> None:
        user = await self._identity_provider.get_user()

        if user.organization_id is not None:
            raise ApplicationException("You are already have an organization")

        organization = self._organization_factory.create(request.name)
        role = self._role_factory.create(
            name="owner",
            description="Organization owner. Can do everything",
            organization_id=organization.id,
            permissions=await self._permission_repository.get_all(),
        )

        self._organization_repository.add(organization)
        self._role_repository.add(role)
        await self._transaction_manager.flush()
        self._user_role_repository.add(
            UserRole(
                id=cast(int, cast(object, None)),
                role_id=role.id,
                user_id=user.id,
                created_at=cast(datetime, cast(object, None)),
                updated_at=None,
            )
        )

        user.organization_id = organization.id
        await self._transaction_manager.commit()
