from aiogram.dispatcher.router import Router

from .start_handler import router as start_router
from .todo_items_actions_handler import router as todo_items_actions_router

routers: list[Router] = [start_router, todo_items_actions_router]

__all__ = [
    "routers"
]


