import sqlalchemy as sa

from vexo.domain.entities.user import User, UserRole
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
    sa.Column("is_active", sa.Boolean, server_default=sa.text("true"), nullable=False),
    sa.Column(
        "organization_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("organizations.id", ondelete="SET NULL"),
        nullable=True,
    ),
    sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        onupdate=sa.func.now(),
        server_onupdate=sa.func.now(),
    ),
)

users_roles_table = sa.Table(
    "users_roles",
    mapper_registry.metadata,
    sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column(
        "user_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    ),
    sa.Column(
        "role_id",
        sa.UUID(as_uuid=True),
        sa.ForeignKey("roles.id", ondelete="CASCADE"),
        nullable=False,
    ),
    sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        onupdate=sa.func.now(),
        server_onupdate=sa.func.now(),
    ),
    sa.UniqueConstraint("user_id", "role_id"),
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
            "is_active": users_table.c.is_active,
            "organization_id": users_table.c.organization_id,
            "created_at": users_table.c.created_at,
            "updated_at": users_table.c.updated_at,
        },
        column_prefix="_",
    )


def _map_users_roles_table() -> None:
    _ = mapper_registry.map_imperatively(
        UserRole,
        users_roles_table,
        properties={
            "id": users_roles_table.c.id,
            "user_id": users_roles_table.c.user_id,
            "role_id": users_roles_table.c.role_id,
            "created_at": users_roles_table.c.created_at,
            "updated_at": users_roles_table.c.updated_at,
        },
        column_prefix="_",
    )
