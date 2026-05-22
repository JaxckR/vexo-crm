from dishka import Provider, from_context, Scope

from vexo.bootstrap.config import PostgresConfig


class ContextProvider(Provider):
    scope = Scope.APP

    database_config = from_context(PostgresConfig)
