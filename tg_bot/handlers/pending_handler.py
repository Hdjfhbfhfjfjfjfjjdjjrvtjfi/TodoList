from aiogram import Router
from aiogram.types import CallbackQuery

from tg_bot.filters import PendingPageCallback, PendingItemCallback, MarkDoneCallback
from tg_bot.keyboards import build_pending_keyboard, build_todo_item_keyboard
from tg_bot.models import Todo
from tg_bot.services import PaginationService
from tg_bot.utils import (
    get_pending_tasks_text,
    get_todo_details_text,
    get_task_marked_done_text,
    get_task_not_found_error_text,
)


class PendingHandler:
    def __init__(self, pending_router: Router):
        self.router = pending_router
        self._register_handlers()
    
    def _register_handlers(self) -> None:
        self.router.callback_query.register(
            self.on_pending_page, PendingPageCallback.filter()
        )
        self.router.callback_query.register(
            self.on_view_todo_item, PendingItemCallback.filter()
        )
        self.router.callback_query.register(
            self.on_mark_done, MarkDoneCallback.filter()
        )

    # noinspection PyMethodMayBeStatic
    async def on_pending_page(self, callback: CallbackQuery, callback_data: PendingPageCallback, items_per_page: int
                              )-> None:
        page = max(callback_data.page, 0)
        tasks, total, has_prev, has_next = await PaginationService(False).fetch_tasks_page(
            callback.from_user.id,
            page,
            items_per_page
        )
        await callback.message.edit_text(
            get_pending_tasks_text(total),
            reply_markup=build_pending_keyboard(
                page=page,
                has_prev=has_prev,
                has_next=has_next,
                todos=tasks
            )
        )
        await callback.answer()

    # noinspection PyMethodMayBeStatic
    async def on_view_todo_item(self, callback: CallbackQuery, callback_data: PendingItemCallback) -> None:
        todo = await Todo.filter(
            id=callback_data.todo_id,
            user_id=callback.from_user.id,
            done=False,
        ).first()
        created_str = getattr(todo, "created_at", None).strftime("%Y-%m-%d %H:%M") \
            if getattr(todo, "created_at", None) else "Неизвестно"
        details = get_todo_details_text(
            text=todo.text,
            done=todo.done,
            created_str=created_str,
        )
        await callback.message.edit_text(
            details,
            reply_markup=(
                build_todo_item_keyboard(
                    callback_data.todo_id,
                    callback_data.page
                )
            )
        )
        await callback.answer()
    
    async def on_mark_done(self, callback: CallbackQuery, callback_data: MarkDoneCallback, items_per_page: int) -> None:
        todo = await Todo.filter(
            id=callback_data.todo_id,
            user_id=callback.from_user.id,
            done=False,
        ).first()
        
        if todo:
            todo.done = True
            await todo.save()
            await self.on_pending_page(callback, PendingPageCallback(page=callback_data.page), items_per_page)
            await callback.answer(get_task_marked_done_text())
        else:
            await callback.answer(get_task_not_found_error_text())


router = Router()
PendingHandler(router)


