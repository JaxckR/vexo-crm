import sqlalchemy as sa
from sqlalchemy.orm import relationship

from vexo.domain.entities.role import Role
from vexo.domain.entities.user import User
from vexo.infrastructure.persistence.tables.common import mapper_registry

users_table = sa.Table(
    "users",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID(as_uuid=True), primary_key=True),
    sa.Column("login", sa.String, unique=True, nullable=False),
    sa.Column("password_hash", sa.String, nullable=False),
    sa.Column("email", sa.String, unique=True, nullable=False),
    sa.Column("first_name", sa.String, nullable=False),
    sa.Column("last_name", sa.String, nullable=False),
    sa.Column(
        "organization_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("organizations.id"),
        nullable=False,
    ),
    sa.Column("role_id", sa.UUID, sa.ForeignKey("roles.id"), nullable=False),
    sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        onupdate=sa.func.now(),
        server_onupdate=sa.func.now(),
    ),
)


def _map_users_table() -> None:
    _ = mapper_registry.map_imperatively(
        User,
        users_table,
        properties={
            "id": users_table.c.id,
            "login": users_table.c.login,
            "password_hash": users_table.c.password_hash,
            "email": users_table.c.email,
            "first_name": users_table.c.first_name,
            "last_name": users_table.c.last_name,
            "organization_id": users_table.c.organization_id,
            "created_at": users_table.c.created_at,
            "updated_at": users_table.c.updated_at,
            "role": relationship(Role, lazy="joined"),
        },
        column_prefix="_",
    )
