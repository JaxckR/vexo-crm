from dataclasses import dataclass

from vexo.application.ports import IdentityProvider
from vexo.application.ports.repositories.organization import OrganizationRepository
from vexo.domain.entities.organization import Organization


@dataclass(slots=True, frozen=True)
class GetOrganizationHandler:
    _identity_provider: IdentityProvider
    _organization_repository: OrganizationRepository

    async def handle(self) -> Organization | None:
        user = await self._identity_provider.get_user()

        if user.organization_id is None:
            return None

        organization = await self._organization_repository.get(user.organization_id)
        return organization
