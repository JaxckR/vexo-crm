__all__ = ("get_async_container",)

from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import FastapiProvider

from vexo.bootstrap.config import PostgresConfig, Config
from vexo.bootstrap.ioc.application import ApplicationProvider
from vexo.bootstrap.ioc.context import ContextProvider
from vexo.bootstrap.ioc.database import DatabaseProvider
from vexo.bootstrap.ioc.infrastructure import InfrastructureProvider


def get_async_container(config: Config) -> AsyncContainer:
    return make_async_container(
        *(
            FastapiProvider(),
            ContextProvider(),
            ApplicationProvider(),
            DatabaseProvider(),
            InfrastructureProvider(),
        ),
        context={PostgresConfig: config.database},
    )
