from datetime import datetime
from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from fastapi.params import Cookie
from starlette.responses import Response

from vexo.application.dtos import UserDTO
from vexo.application.handlers.auth.change_password import (
    ChangePasswordRequest,
    ChangePasswordHandler,
)
from vexo.application.handlers.auth.login import LoginRequest, LoginHandler
from vexo.application.handlers.auth.logout import LogoutHandler
from vexo.application.handlers.auth.me import MeHandler
from vexo.application.handlers.auth.registration import (
    RegistrationHandler,
    RegistrationRequest,
)
from vexo.domain.entities.session import SessionId

auth_router = APIRouter(prefix="/auth", tags=["auth"], route_class=DishkaRoute)


@auth_router.post("/login")
async def login(
    request: LoginRequest, handler: FromDishka[LoginHandler], response: Response
) -> None:
    result = await handler.handle(request)
    response.set_cookie(
        key="session_id",
        value=result.id,
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=int((result.expires_at - datetime.now()).total_seconds()),
    )


@auth_router.delete("/logout")
async def logout(
    handler: FromDishka[LogoutHandler],
    response: Response,
    session_id: Annotated[SessionId, Cookie()] = None,
) -> None:
    if session_id is None:
        return

    await handler.handle(session_id)
    response.delete_cookie(key="session_id")


@auth_router.get("/me")
async def me(handler: FromDishka[MeHandler]) -> UserDTO:
    return await handler.handle()


@auth_router.patch("/me/change_password")
async def change_password(
    request: ChangePasswordRequest, handler: FromDishka[ChangePasswordHandler]
) -> None:
    await handler.handle(request)


@auth_router.post("/registration")
async def registration(
    request: RegistrationRequest, handler: FromDishka[RegistrationHandler]
) -> None:
    await handler.handle(request)
