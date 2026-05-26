from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from vexo.application.handlers.organization.create import (
    CreateOrganizationRequest,
    CreateOrganizationHandler,
)
from vexo.application.handlers.organization.get import GetOrganizationHandler
from vexo.domain.entities.organization import Organization

organization_router = APIRouter(
    prefix="/organization", tags=["organization"], route_class=DishkaRoute
)


@organization_router.post("/")
async def create(
    request: CreateOrganizationRequest, handler: FromDishka[CreateOrganizationHandler]
) -> None:
    await handler.handle(request)


@organization_router.get("/me")
async def my_organization(
    handler: FromDishka[GetOrganizationHandler],
) -> Organization | None:
    return await handler.handle()
