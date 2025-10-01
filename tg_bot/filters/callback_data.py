from aiogram.filters.callback_data import CallbackData


class PendingPageCallback(CallbackData, prefix="pending"):
    page: int


class DonePageCallback(CallbackData, prefix="view_done"):
    page: int


class AddTaskCallback(CallbackData, prefix="add_task"):
    pass


class DeleteDoneCallback(CallbackData, prefix="delete_done"):
    pass


class PendingItemCallback(CallbackData, prefix="pending_item"):
    todo_id: int
    page: int


class BackToStartCallback(CallbackData, prefix="back_start"):
    pass


class MarkDoneCallback(CallbackData, prefix="mark_done"):
    todo_id: int
    page: int


class DeleteDonePageCallback(CallbackData, prefix="delete_done_item"):
    todo_id: int
    page: int


class DoneItemCallback(CallbackData, prefix="done_item"):
    todo_id: int
    page: int


