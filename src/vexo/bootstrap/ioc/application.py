from dishka import Provider, Scope, provide_all

from vexo.application.factories.session import SessionFactory
from vexo.application.factories.user import UserFactory
from vexo.application.handlers.auth.change_password import ChangePasswordHandler
from vexo.application.handlers.auth.login import LoginHandler
from vexo.application.handlers.auth.logout import LogoutHandler
from vexo.application.handlers.auth.me import MeHandler
from vexo.application.handlers.auth.registration import RegistrationHandler


class ApplicationProvider(Provider):
    scope = Scope.REQUEST

    fabrics = provide_all(UserFactory, SessionFactory)

    handlers = provide_all(
        RegistrationHandler,
        LoginHandler,
        LogoutHandler,
        MeHandler,
        ChangePasswordHandler,
    )
