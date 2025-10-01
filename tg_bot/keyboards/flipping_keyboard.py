__all__ = [
    "FlippingKeyboard"
]
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData

from typing import List, Optional

from tg_bot.filters.callback_data import BackToStartCallback
from tg_bot.models import Todo
from tg_bot.utils import (
    get_prev_page_button_text,
    get_next_page_button_text,
    get_page_button_text,
    get_back_button_text,
    get_todo_item_button_text
)
from tg_bot.utils.interfaces import IFlippingPageCallback, IActionWithTodoItemAndTodoItemCallback


class FlippingKeyboard:
    def __init__(
            self,
            flip_callback_data_type: type[IFlippingPageCallback | CallbackData],
            action_callback_data_type: type[IActionWithTodoItemAndTodoItemCallback | CallbackData],
            done: bool
    ) -> None:
        self.flip_callback_data_type = flip_callback_data_type
        self.action_callback_data_type = action_callback_data_type
        self.done = done

    def build_keyboard(
        self,
        page: int,
        has_prev: bool,
        has_next: bool,
        todos: Optional[List[Todo]] = None,
        current_page: Optional[int] = None,
    ) -> InlineKeyboardMarkup:
        if todos is None:
            todos = []
        else:
            page_for_items = page if current_page is None else current_page
            todos = [[
                InlineKeyboardButton(
                    text=get_todo_item_button_text(self.done, todo.text),
                    callback_data=self.action_callback_data_type(todo_id=todo.id, page=page_for_items).pack(),
                ) for todo in todos
            ]]

        row = []
        if has_prev:
            row.append(
                InlineKeyboardButton(
                    text=get_prev_page_button_text(),
                    callback_data=self.flip_callback_data_type(page=page - 1).pack(),
                )
            )
        row.append(
            InlineKeyboardButton(
                text=get_page_button_text(page),
                callback_data=self.flip_callback_data_type(page=page).pack()
            )
        )
        if has_next:
            row.append(
                InlineKeyboardButton(
                    text=get_next_page_button_text(),
                    callback_data=self.flip_callback_data_type(page=page + 1).pack(),
                )
            )
        if row:
            todos.append(row)

        todos.append([
            InlineKeyboardButton(text=get_back_button_text(), callback_data=BackToStartCallback().pack())
        ])
        return InlineKeyboardMarkup(inline_keyboard=todos)
