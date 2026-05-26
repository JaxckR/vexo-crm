import json

from dishka import AsyncContainer

from vexo.application.ports import TransactionManager, IdGenerator
from vexo.application.ports.repositories.permission import PermissionRepository
from vexo.bootstrap.config import SETTINGS_DIR
from vexo.domain.entities.permission import Resource, Action, Permission


async def permissions_seed(container: AsyncContainer) -> None:
    with open(SETTINGS_DIR / "allow_actions.json", "r") as f:
        RESOURCE_ACTIONS = json.loads(f.read())

    async with container() as c:
        repository = await c.get(PermissionRepository)
        id_generator = await c.get(IdGenerator)
        transaction_manager = await c.get(TransactionManager)

        for resource, actions in RESOURCE_ACTIONS.items():
            for action in actions:
                if await repository.exists(Resource(resource), Action(action)):
                    continue

                repository.add(
                    Permission(
                        id=id_generator.generate_permission_id(),
                        resource=resource,
                        action=action,
                    )
                )

        await transaction_manager.commit()
