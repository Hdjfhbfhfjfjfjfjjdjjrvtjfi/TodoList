import asyncio

import os

from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import load_dotenv

from tortoise import Tortoise

from tg_bot.handlers import routers
from tg_bot.utils import init_tortoise_database


async def main() -> None:
    # Load environment variables from project root .env
    project_root = Path(__file__).resolve().parents[1]
    load_dotenv(project_root / ".env")

    token = os.getenv("TOKEN")
    if not token:
        raise RuntimeError("TOKEN не задан. Установите переменную окружения.")

    # Initialize database using URL from .env
    db_url = os.getenv("DATABASE_PATH")
    await init_tortoise_database(
        db_url=db_url,
        model_modules=("tg_bot.models",),
        generate_schemas=True,
    )

    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(*routers)

    try:
        await dp.start_polling(bot, items_per_page=int(os.getenv("ITEMS_PER_PAGE")))
    finally:
        await bot.session.close()
        await Tortoise.close_connections()


if __name__ == "__main__":
    asyncio.run(main())


