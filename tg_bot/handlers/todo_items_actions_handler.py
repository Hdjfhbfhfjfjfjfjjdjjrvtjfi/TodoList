__all__ = [
    "router"
]
from typing import Callable, Generic, TypeVar

from aiogram.dispatcher.router import Router
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery

from tg_bot.filters import (DonePageCallback, DoneItemCallback, DeleteDonePageCallback, PendingPageCallback,
                            PendingItemCallback, MarkDoneCallback)
from tg_bot.services import PaginationService
from tg_bot.keyboards import FlippingKeyboard, ItemKeyboard
from tg_bot.models import Todo
from tg_bot.utils.interfaces import IFlippingPageCallback, IActionWithTodoItemAndTodoItemCallback
from tg_bot.utils import (
    get_done_tasks_text,
    get_task_marked_done_text,
    get_task_deleted_text,
    get_pending_tasks_text,
    get_todo_details_text
)


T = TypeVar('T', bound=IFlippingPageCallback | CallbackData)
K = TypeVar('K', bound=IActionWithTodoItemAndTodoItemCallback | CallbackData)
Y = TypeVar('Y', bound=IActionWithTodoItemAndTodoItemCallback | CallbackData)

class TodoItemsActionsHandler(Generic[T, K, Y]):
    def __init__(
            self,
            router: Router,
            done: bool,
            on_view_text: Callable[[int], str],
            on_view_item_text: Callable[[str, bool, str], str],
            callback_answer_text: Callable[[], str],
            on_view_callback: type[IFlippingPageCallback | CallbackData],
            on_view_item_callback: type[IActionWithTodoItemAndTodoItemCallback | CallbackData],
            on_item_action_callback: type[IActionWithTodoItemAndTodoItemCallback | CallbackData]
    ) -> None:
        self.router = router
        self.done = done
        self.pagination_service = PaginationService(done)
        self.on_view_text = on_view_text
        self.on_view_item_text = on_view_item_text
        self.callback_answer_text = callback_answer_text
        self.on_view_callback = on_view_callback
        self.on_view_item_callback = on_view_item_callback
        self.on_item_action_callback = on_item_action_callback
        self._register_handlers()

    def _register_handlers(self) -> None:
        self.router.callback_query.register(
            self.on_done_page, self.on_view_callback.filter()
        )
        self.router.callback_query.register(
            self.on_view_done_item, self.on_view_item_callback.filter()
        )
        self.router.callback_query.register(
            self.on_delete_done_item, self.on_item_action_callback.filter()
        )

    async def on_done_page(self, callback: CallbackQuery, callback_data: T, items_per_page: int) -> None:
        page = max(callback_data.page, 0)
        tasks, total, has_prev, has_next = await self.pagination_service.fetch_tasks_page(
            callback.from_user.id,
            page,
            items_per_page
        )
        await callback.message.edit_text(
            self.on_view_text(total),
            reply_markup=FlippingKeyboard(self.on_view_callback, self.on_view_item_callback, self.done).
            build_keyboard(
                page=page,
                has_prev=has_prev,
                has_next=has_next,
                todos=tasks
            )
        )
        await callback.answer()

    async def on_view_done_item(self, callback: CallbackQuery, callback_data: K) -> None:
        todo = await Todo.filter(
            id=callback_data.todo_id,
            user_id=callback.from_user.id,
            done=True,
        ).first()
        created_str = getattr(todo, "created_at", None).strftime("%Y-%m-%d %H:%M") \
            if getattr(todo, "created_at", None) else "Неизвестно"
        await callback.message.edit_text(
            self.on_view_item_text(
                todo.text,
                todo.done,
                created_str,
            ),
            reply_markup=(
                ItemKeyboard(self.on_view_callback, self.on_item_action_callback, self.done).build_keyboard(
                    callback_data.page,
                    callback_data.todo_id
                )
            )
        )
        await callback.answer()

    async def on_delete_done_item(self, callback: CallbackQuery, callback_data: Y, items_per_page: int) -> None:
        todo = await Todo.filter(
            id=callback_data.todo_id,
            user_id=callback.from_user.id,
            done=True,
        ).first()

        if todo:
            await todo.delete()
            await self.on_done_page(callback, self.on_view_callback(page=callback_data.page), items_per_page)
            await callback.answer(self.callback_answer_text())

router = Router()
TodoItemsActionsHandler[DonePageCallback, DoneItemCallback, DeleteDonePageCallback](
    router,
    True,
    get_done_tasks_text,
    get_todo_details_text,
    get_task_deleted_text,
    DonePageCallback,
    DoneItemCallback,
    DeleteDonePageCallback
)
TodoItemsActionsHandler[PendingPageCallback, PendingItemCallback, MarkDoneCallback](
    router,
    False,
    get_pending_tasks_text,
    get_todo_details_text,
    get_task_marked_done_text,
    PendingPageCallback,
    PendingItemCallback,
    MarkDoneCallback
)
