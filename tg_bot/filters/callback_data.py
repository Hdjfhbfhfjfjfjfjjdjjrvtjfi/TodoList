__all__ = [
    "PendingPageCallback",
    "DonePageCallback",
    "MarkDoneCallback",
    "PendingItemCallback",
    "DoneItemCallback",
    "AddTaskCallback",
    "DeleteDonePageCallback",
    "BackToStartCallback",
]
from aiogram.filters.callback_data import CallbackData

from tg_bot.utils.interfaces import IFlippingPageCallback, IActionWithTodoItemAndTodoItemCallback


class PendingPageCallback(CallbackData, IFlippingPageCallback, prefix="pending"):
    page: int


class DonePageCallback(CallbackData, IFlippingPageCallback, prefix="view_done"):
    page: int


class AddTaskCallback(CallbackData, prefix="add_task"):
    pass

class PendingItemCallback(CallbackData, IActionWithTodoItemAndTodoItemCallback, prefix="pending_item"):
    todo_id: int
    page: int

class DoneItemCallback(CallbackData, IActionWithTodoItemAndTodoItemCallback, prefix="done_item"):
    todo_id: int
    page: int

class MarkDoneCallback(CallbackData, IActionWithTodoItemAndTodoItemCallback, prefix="mark_done"):
    todo_id: int
    page: int


class DeleteDonePageCallback(CallbackData, IActionWithTodoItemAndTodoItemCallback, prefix="delete_done_item"):
    todo_id: int
    page: int

class BackToStartCallback(CallbackData, prefix="back_start"):
    pass
