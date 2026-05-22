import asyncio
import sys
from contextlib import asynccontextmanager
from typing import AsyncIterator

import uvicorn
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from vexo.bootstrap.config import get_config
from vexo.bootstrap.ioc import get_async_container
from vexo.bootstrap.logging import setup_logging
from vexo.infrastructure.persistence.tables import setup_tables
from vexo.presentation.web import setup_exceptions, setup_routes, setup_middleware


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield
    await app.state.dishka_container.close()


def create_app() -> FastAPI:
    app = FastAPI(
        title="VexoCRM",
        description="VexoCRM for any organizations",
        version="0.0.1",
        lifespan=lifespan,
    )
    setup_logging()

    setup_dishka(get_async_container(get_config()), app)

    setup_routes(app)
    setup_exceptions(app)
    setup_middleware(app)
    setup_tables()

    return app


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    uvicorn.run(create_app(), host="0.0.0.0", port=8000, loop="none")
