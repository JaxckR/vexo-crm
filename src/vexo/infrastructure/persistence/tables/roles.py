import sqlalchemy as sa

from vexo.domain.entities.role import Role, RolePermission
from vexo.infrastructure.persistence.tables.common import mapper_registry

roles_table = sa.Table(
    "roles",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
    sa.Column("name", sa.String, nullable=False),
    sa.Column("description", sa.String, nullable=True),
    sa.Column(
        "organization_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("organizations.id"),
        nullable=False,
    ),
    sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        onupdate=sa.func.now(),
        server_onupdate=sa.func.now(),
    ),
    sa.UniqueConstraint("name", "organization_id"),
)

roles_permissions_table = sa.Table(
    "roles_permissions",
    mapper_registry.metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
    sa.Column(
        "role_id", sa.UUID(as_uuid=True), sa.ForeignKey("roles.id"), nullable=False
    ),
    sa.Column(
        "permission_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("permissions.id"),
        nullable=False,
    ),
    sa.UniqueConstraint("role_id", "permission_id"),
)


def _map_roles_table() -> None:
    _ = mapper_registry.map_imperatively(
        Role,
        roles_table,
        properties={
            "id": roles_table.c.id,
            "name": roles_table.c.name,
            "description": roles_table.c.description,
            "organization_id": roles_table.c.organization_id,
            "created_at": roles_table.c.created_at,
            "updated_at": roles_table.c.updated_at,
        },
        column_prefix="_",
    )


def _map_roles_permissions_table() -> None:
    _ = mapper_registry.map_imperatively(
        RolePermission,
        roles_permissions_table,
        properties={
            "id": roles_permissions_table.c.id,
            "role_id": roles_permissions_table.c.role_id,
            "permission_id": roles_permissions_table.c.permission_id,
        },
        column_prefix="_",
    )
