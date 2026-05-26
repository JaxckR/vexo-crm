from dishka import Provider, Scope, provide_all

from vexo.application.factories.organization import OrganizationFactory
from vexo.application.factories.role import RoleFactory
from vexo.application.factories.session import SessionFactory
from vexo.application.factories.user import UserFactory
from vexo.application.handlers.auth.change_password import ChangePasswordHandler
from vexo.application.handlers.auth.login import LoginHandler
from vexo.application.handlers.auth.logout import LogoutHandler
from vexo.application.handlers.auth.me import MeHandler
from vexo.application.handlers.auth.registration import RegistrationHandler
from vexo.application.handlers.organization.create import CreateOrganizationHandler
from vexo.application.handlers.organization.get import GetOrganizationHandler
from vexo.application.handlers.role.create import CreateRoleHandler


class ApplicationProvider(Provider):
    scope = Scope.REQUEST

    fabrics = provide_all(UserFactory, SessionFactory, OrganizationFactory, RoleFactory)

    handlers = provide_all(
        RegistrationHandler,
        LoginHandler,
        LogoutHandler,
        MeHandler,
        ChangePasswordHandler,
        CreateOrganizationHandler,
        GetOrganizationHandler,
        CreateRoleHandler,
    )
