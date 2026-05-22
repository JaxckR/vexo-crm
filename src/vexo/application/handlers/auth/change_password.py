from dataclasses import dataclass

from vexo.application.exceptions import ApplicationException
from vexo.application.factories.user import UserFactory
from vexo.application.ports import IdentityProvider, TransactionManager, Verifier
from vexo.application.ports.repositories.user import UserRepository


@dataclass(slots=True, frozen=True)
class ChangePasswordRequest:
    old_password: str
    new_password: str


@dataclass(slots=True, frozen=True)
class ChangePasswordHandler:
    _user_repository: UserRepository
    _identity_provider: IdentityProvider
    _user_factory: UserFactory
    _verifier: Verifier
    _transaction_manager: TransactionManager

    async def handle(self, request: ChangePasswordRequest) -> None:
        user_id = await self._identity_provider.get_current_user_id()
        user = await self._user_repository.get(user_id)

        if user is None:
            raise ApplicationException("User not found")

        if not self._verifier.verify_password(request.old_password, user.password_hash):
            raise ApplicationException("Invalid password")

        user = self._user_factory.change_password(user, request.new_password)
        await self._transaction_manager.commit()
