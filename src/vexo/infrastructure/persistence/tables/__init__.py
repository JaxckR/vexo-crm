__all__ = (
    # Tables
    "organizations_table",
    "users_table",
    "roles_table",
    "roles_permissions_table",
    "permissions_table",
    "sessions_table",
    "users_roles_table",
    # Ostal'noe
    "setup_tables",
    "mapper_registry",
)

from .common import mapper_registry
from .organizations import organizations_table, _map_organizations_table
from .permissions import permissions_table, _map_permissions_table
from .roles import (
    roles_table,
    _map_roles_table,
    roles_permissions_table,
    _map_roles_permissions_table,
)
from .sessions import sessions_table, _map_sessions_table
from .users import (
    users_table,
    _map_users_table,
    users_roles_table,
    _map_users_roles_table,
)


def setup_tables() -> None:
    _map_organizations_table()
    _map_users_table()
    _map_roles_table()
    _map_permissions_table()
    _map_roles_permissions_table()
    _map_sessions_table()
    _map_users_roles_table()
