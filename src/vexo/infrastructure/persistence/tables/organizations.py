import sqlalchemy as sa

from vexo.domain.entities.organization import Organization
from vexo.infrastructure.persistence.tables.common import mapper_registry

organizations_table = sa.Table(
    "organizations",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
    sa.Column("name", sa.String(), nullable=False),
    sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        onupdate=sa.func.now(),
        server_onupdate=sa.func.now(),
    ),
)


def _map_organizations_table() -> None:
    _ = mapper_registry.map_imperatively(
        Organization,
        organizations_table,
        properties={
            "id": organizations_table.c.id,
            "name": organizations_table.c.name,
            "created_at": organizations_table.c.created_at,
            "updated_at": organizations_table.c.updated_at,
        },
        column_prefix="_",
    )
