__all__ = ("setup_routes",)

from typing import Final

from fastapi import FastAPI, APIRouter

from .auth import auth_router
from .index import index_router


def setup_routes(app: FastAPI) -> None:
    ROUTERS: Final[list[APIRouter]] = [index_router, auth_router]

    for router in ROUTERS:
        app.include_router(router)
