from sqlalchemy import select, and_
from sqlalchemy.exc import IntegrityError

from vexo.application.exceptions import AlreadyExistsError, NotFoundError
from vexo.application.ports.repositories.user import UserRepository, UserRoleRepository
from vexo.domain.entities.user import User, UserId, UserRole
from vexo.infrastructure.persistence.adapters.common import SQLAMixin


class UserRepositoryImpl(SQLAMixin, UserRepository):
    async def get_by_login(self, login: str) -> User | None:
        query = await self._session.execute(
            select(User).where(and_(User.login == login))
        )
        return query.scalar_one_or_none()

    async def get(self, id_: UserId) -> User | None:
        query = await self._session.execute(select(User).where(and_(User.id == id_)))
        return query.scalar_one_or_none()

    async def add(self, instance: User) -> None:
        self._session.add(instance)
        try:
            await self._session.flush()
        except IntegrityError as exc:
            self._handle_exceptions(exc)
            await self._session.rollback()

    def _handle_exceptions(self, exc: IntegrityError) -> None:
        exc = str(exc)
        if "uq_users_login" in exc:
            raise AlreadyExistsError("Login already exists")
        elif "uq_users_email" in exc:
            raise AlreadyExistsError("Email already exists")
        elif "fk_users_organization_id_organizations" in exc:
            raise NotFoundError("Organization not found")


class UserRoleRepositoryImpl(SQLAMixin, UserRoleRepository):
    def add(self, instance: UserRole) -> None:
        self._session.add(instance)
