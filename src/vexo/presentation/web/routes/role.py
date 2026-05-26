from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from vexo.application.handlers.role.create import CreateRoleRequest, CreateRoleHandler

role_router = APIRouter(prefix="/role", tags=["role"], route_class=DishkaRoute)


@role_router.post("/")
async def create(
    request: CreateRoleRequest, handler: FromDishka[CreateRoleHandler]
) -> None:
    await handler.handle(request)
