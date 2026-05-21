import sqlalchemy as sa

from vexo.domain.entities.permission import Resource, Action, Permission
from vexo.infrastructure.persistence.tables.common import mapper_registry

permissions_table = sa.Table(
    "permissions",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
    sa.Column("resource", sa.Enum(Resource), nullable=False),
    sa.Column("action", sa.Enum(Action), nullable=False),
    sa.UniqueConstraint("resource", "action"),
)


def _map_permissions_table() -> None:
    _ = mapper_registry.map_imperatively(
        Permission,
        permissions_table,
        properties={
            "id": permissions_table.c.id,
            "resource": permissions_table.c.resource,
            "action": permissions_table.c.action,
        },
        column_prefix="_",
    )
