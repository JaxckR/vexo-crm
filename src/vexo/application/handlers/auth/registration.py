from dataclasses import dataclass

from vexo.application.exceptions import NotFoundError
from vexo.application.factories.user import UserFactory
from vexo.application.ports import TransactionManager
from vexo.application.ports.repositories.role import RoleRepository
from vexo.application.ports.repositories.user import UserRepository
from vexo.domain.entities.organization import OrganizationId
from vexo.domain.entities.role import RoleId


@dataclass(slots=True, frozen=True)
class RegistrationRequest:
    login: str
    email: str
    password: str
    first_name: str
    last_name: str
    organization_id: OrganizationId
    role_id: RoleId


@dataclass(slots=True, frozen=True)
class RegistrationHandler:
    _user_factory: UserFactory
    _user_repository: UserRepository
    _role_repository: RoleRepository
    _transaction_manager: TransactionManager

    async def handle(self, request: RegistrationRequest) -> None:
        role = await self._role_repository.get(request.role_id)

        if not role:
            raise NotFoundError("Role not found")

        user = self._user_factory.create(
            login=request.login,
            email=request.email,
            password=request.password,
            first_name=request.first_name,
            last_name=request.last_name,
            organization_id=request.organization_id,
            role=role,
        )
        await self._user_repository.add(user)
        await self._transaction_manager.commit()
