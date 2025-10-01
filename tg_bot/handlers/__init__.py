from aiogram.dispatcher.router import Router

from .start_handler import router as start_router
from .pending_handler import router as pending_router
from .done_handler import router as done_router

routers: list[Router] = [start_router, pending_router, done_router]
__all__ = [
    "routers"
]


