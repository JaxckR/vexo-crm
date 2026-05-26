from dataclasses import dataclass
from enum import StrEnum
from typing import NewType
from uuid import UUID

from vexo.domain.entities.common import IDEntity

PermissionId = NewType("PermissionId", UUID)


class Action(StrEnum):
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"
    IMPORT = "import"
    EXPORT = "export"
    CONVERT = "convert"


class Resource(StrEnum):
    CONTACTS = "contacts"
    COMPANIES = "companies"
    LEADS = "leads"
    DEALS = "deals"
    TASKS = "tasks"
    PRODUCTS = "products"
    REPORTS = "reports"
    USERS = "users"
    SETTINGS = "settings"
    ORGANIZATIONS = "organizations"
    ROLES = "roles"


@dataclass
class Permission(IDEntity[PermissionId]):
    resource: Resource
    action: Action
