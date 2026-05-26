from sqlalchemy import exists, select, and_

from vexo.application.ports.repositories.permission import PermissionRepository
from vexo.domain.entities.permission import Resource, Action, Permission
from vexo.domain.entities.role import RolePermission
from vexo.domain.entities.user import UserId, UserRole
from vexo.infrastructure.persistence.adapters.common import SQLAMixin


class PermissionRepositoryImpl(SQLAMixin, PermissionRepository):
    def add(self, instance: Permission) -> None:
        self._session.add(instance)

    async def get_all(self) -> list[Permission]:
        query = await self._session.execute(select(Permission))
        return list(query.scalars().all())

    async def exists(self, resource: Resource, action: Action) -> bool:
        query = await self._session.execute(
            select(
                exists(Permission.id).where(
                    and_(Permission.action == action, Permission.resource == resource)
                )
            )
        )
        return query.scalar()

    async def has_permission(
        self, user_id: UserId, resource: Resource, action: Action
    ) -> bool:
        query = await self._session.execute(
            select(
                exists(
                    select(Permission.id)
                    .join(
                        RolePermission,
                        and_(RolePermission.permission_id == Permission.id),
                    )
                    .join(UserRole, and_(UserRole.role_id == RolePermission.role_id))
                    .where(
                        and_(
                            UserRole.user_id == user_id,
                            Permission.action == action,
                            Permission.resource == resource,
                        )
                    )
                )
            )
        )
        return query.scalar()
