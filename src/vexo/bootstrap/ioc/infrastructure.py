from dishka import Provider, Scope, provide_all, WithParents

from vexo.infrastructure.adapters.hasher import HasherImpl
from vexo.infrastructure.adapters.id_generator import IdGeneratorImpl
from vexo.infrastructure.adapters.idp import IdentityProviderImpl
from vexo.infrastructure.adapters.verifier import VerifierImpl
from vexo.infrastructure.persistence.adapters.role_repository import RoleRepositoryImpl
from vexo.infrastructure.persistence.adapters.session_repository import (
    SessionRepositoryImpl,
)
from vexo.infrastructure.persistence.adapters.user_repository import UserRepositoryImpl


class InfrastructureProvider(Provider):
    scope = Scope.REQUEST

    adapters = provide_all(
        WithParents[IdGeneratorImpl],
        WithParents[VerifierImpl],
        WithParents[HasherImpl],
        WithParents[IdentityProviderImpl],
    )

    repositories = provide_all(
        WithParents[UserRepositoryImpl],
        WithParents[RoleRepositoryImpl],
        WithParents[SessionRepositoryImpl],
    )
