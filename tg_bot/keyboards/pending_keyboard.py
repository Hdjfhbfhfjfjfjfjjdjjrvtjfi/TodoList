from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from typing import List, Optional

from tg_bot.filters.callback_data import PendingPageCallback, PendingItemCallback, BackToStartCallback
from tg_bot.models import Todo
from tg_bot.utils import (
    get_prev_page_button_text,
    get_next_page_button_text,
    get_page_button_text,
    get_back_button_text,
)
from tg_bot.utils.interfaces import KeyboardInterface


class PendingKeyboard(KeyboardInterface):
    
    def __init__(self):
        super().__init__()
    
    def build_keyboard(
        self,
        page: int,
        has_prev: bool,
        has_next: bool,
        todos: Optional[List[Todo]] = None,
        current_page: Optional[int] = None,
        **kwargs
    ) -> InlineKeyboardMarkup:
        if todos is None:
            todos = []
        else:
            page_for_items = page if current_page is None else current_page
            todos = [[
                InlineKeyboardButton(
                    text=f"⬜ {todo.text[:50]}{'...' if len(todo.text) > 50 else ''}",
                    callback_data=PendingItemCallback(todo_id=todo.id, page=page_for_items).pack(),
                ) for todo in todos
            ]]

        row = []
        if has_prev:
            row.append(
                InlineKeyboardButton(
                    text=get_prev_page_button_text(),
                    callback_data=PendingPageCallback(page=page - 1).pack(),
                )
            )
        row.append(InlineKeyboardButton(text=get_page_button_text(page), callback_data=PendingPageCallback(page=page).pack()))
        if has_next:
            row.append(
                InlineKeyboardButton(
                    text=get_next_page_button_text(),
                    callback_data=PendingPageCallback(page=page + 1).pack(),
                )
            )
        if row:
            todos.append(row)

        # Back to start menu row
        todos.append([
            InlineKeyboardButton(text=get_back_button_text(), callback_data=BackToStartCallback(page=page).pack())
        ])
        return InlineKeyboardMarkup(inline_keyboard=todos)


def build_pending_keyboard(
    page: int,
    has_prev: bool,
    has_next: bool,
    todos: List[Todo] | None = None,
    current_page: int | None = None,
) -> InlineKeyboardMarkup:
    keyboard = PendingKeyboard()
    return keyboard.build_keyboard(page, has_prev, has_next, todos, current_page)


