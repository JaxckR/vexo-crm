from fastapi import APIRouter

index_router = APIRouter()


@index_router.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
