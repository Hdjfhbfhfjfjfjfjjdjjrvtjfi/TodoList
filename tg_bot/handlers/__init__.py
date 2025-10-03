from aiogram.dispatcher.router import Router

from .start_handler import router as start_router
from .todo_items_actions_handler import router as todo_items_actions_router
from .add_todo_item_handler import router as add_todo_item_router

routers: list[Router] = [start_router, todo_items_actions_router, add_todo_item_router]

__all__ = [
    "routers"
]


