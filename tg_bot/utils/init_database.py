__all__ = [
    "init_tortoise_database"
]
from typing import Sequence

from tortoise import Tortoise


async def init_tortoise_database(
    db_url: str,
    model_modules: Sequence[str],
    generate_schemas: bool,
) -> None:
    await Tortoise.init(db_url=db_url, modules={"models": list(model_modules)})
    if generate_schemas:
        await Tortoise.generate_schemas()


