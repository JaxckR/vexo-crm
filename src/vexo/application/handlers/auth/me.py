from dataclasses import dataclass

from vexo.application.dtos import UserDTO
from vexo.application.exceptions import NotFoundError
from vexo.application.ports import IdentityProvider
from vexo.application.ports.repositories.user import UserRepository


@dataclass(slots=True, frozen=True)
class MeHandler:
    _user_repository: UserRepository
    _identity_provider: IdentityProvider

    async def handle(self) -> UserDTO:
        user_id = await self._identity_provider.get_current_user_id()
        user = await self._user_repository.get(user_id)

        if not user:
            raise NotFoundError("User not found")

        return UserDTO.from_entity(user)
