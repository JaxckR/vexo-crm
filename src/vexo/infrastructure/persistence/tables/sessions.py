import sqlalchemy as sa

from vexo.domain.entities.session import Session
from vexo.infrastructure.persistence.tables import mapper_registry

sessions_table = sa.Table(
    "sessions",
    mapper_registry.metadata,
    sa.Column("id", sa.String(), primary_key=True),
    sa.Column(
        "user_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    ),
    sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
)


def _map_sessions_table() -> None:
    _ = mapper_registry.map_imperatively(
        Session,
        sessions_table,
        properties={
            "id": sessions_table.c.id,
            "user_id": sessions_table.c.user_id,
            "created_at": sessions_table.c.created_at,
            "expires_at": sessions_table.c.expires_at,
        },
        column_prefix="_",
    )
