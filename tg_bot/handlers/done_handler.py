from aiogram import Router
from aiogram.types import CallbackQuery

from tg_bot.filters.callback_data import DonePageCallback, DoneItemCallback, DeleteDonePageCallback
from tg_bot.keyboards import build_done_keyboard, build_done_item_keyboard
from tg_bot.models import Todo
from tg_bot.services import PaginationService
from tg_bot.utils import (
    get_done_tasks_text,
    get_todo_details_text,
    get_task_deleted_text,
    get_task_not_found_error_text,
)


class DoneHandler:
    def __init__(self, done_router: Router):
        self.router = done_router
        self._register_handlers()
    
    def _register_handlers(self) -> None:
        self.router.callback_query.register(
            self.on_done_page, DonePageCallback.filter()
        )
        self.router.callback_query.register(
            self.on_view_done_item, DoneItemCallback.filter()
        )
        self.router.callback_query.register(
            self.on_delete_done_item, DeleteDonePageCallback.filter()
        )

    # noinspection PyMethodMayBeStatic
    async def on_done_page(self, callback: CallbackQuery, callback_data: DonePageCallback, items_per_page: int) -> None:
        page = max(callback_data.page, 0)
        tasks, total, has_prev, has_next = await PaginationService(True).fetch_tasks_page(
            callback.from_user.id, page,
            items_per_page
        )
        await callback.message.edit_text(
            get_done_tasks_text(total),
            reply_markup=build_done_keyboard(
                page=page,
                has_prev=has_prev,
                has_next=has_next,
                todos=tasks
            )
        )
        await callback.answer()

    # noinspection PyMethodMayBeStatic
    async def on_view_done_item(self, callback: CallbackQuery, callback_data: DoneItemCallback) -> None:
        todo = await Todo.filter(
            id=callback_data.todo_id,
            user_id=callback.from_user.id,
            done=True,
        ).first()
        created_str = getattr(todo, "created_at", None).strftime("%Y-%m-%d %H:%M") \
            if getattr(todo, "created_at", None) else "Неизвестно"
        details = get_todo_details_text(
            text=todo.text,
            done=todo.done,
            created_str=created_str,
        )
        await callback.message.edit_text(details, reply_markup=(build_done_item_keyboard(callback_data.todo_id, callback_data.page)))
        await callback.answer()

    # noinspection PyMethodMayBeStatic
    async def on_delete_done_item(self, callback: CallbackQuery, callback_data: DeleteDonePageCallback, items_per_page: int) -> None:
        todo = await Todo.filter(
            id=callback_data.todo_id,
            user_id=callback.from_user.id,
            done=True,
        ).first()
        
        if todo:
            await todo.delete()
            await self.on_done_page(callback, DonePageCallback(page=callback_data.page), items_per_page)
            await callback.answer(get_task_deleted_text())
        else:
            await callback.answer(get_task_not_found_error_text())


router = Router()
DoneHandler(router)
