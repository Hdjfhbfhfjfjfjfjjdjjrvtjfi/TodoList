__all__ = [
    "IActionWithTodoItemAndTodoItemCallback"
]
from abc import ABC


class IActionWithTodoItemAndTodoItemCallback(ABC):
    todo_id: int
    page: int
