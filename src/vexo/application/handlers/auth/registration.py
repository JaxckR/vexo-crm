from dataclasses import dataclass

from vexo.application.factories.user import UserFactory
from vexo.application.ports import TransactionManager
from vexo.application.ports.repositories.user import UserRepository


@dataclass(slots=True, frozen=True)
class RegistrationRequest:
    login: str
    email: str
    password: str
    first_name: str
    last_name: str


@dataclass(slots=True, frozen=True)
class RegistrationHandler:
    _user_factory: UserFactory
    _user_repository: UserRepository
    _transaction_manager: TransactionManager

    async def handle(self, request: RegistrationRequest) -> None:
        user = self._user_factory.create(
            login=request.login,
            email=request.email,
            password=request.password,
            first_name=request.first_name,
            last_name=request.last_name,
        )
        await self._user_repository.add(user)
        await self._transaction_manager.commit()
