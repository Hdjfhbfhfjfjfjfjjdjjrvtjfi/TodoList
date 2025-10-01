__all__ = [
    "ItemKeyboard"
]
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData

from typing import Optional

from tg_bot.utils import get_back_to_list_button_text, get_mark_done_button_text, get_delete_done_item_button_text
from tg_bot.utils.interfaces import IFlippingPageCallback, IActionWithTodoItemAndTodoItemCallback


class ItemKeyboard:
    def __init__(
            self,
            back_callback_data_type: type[IFlippingPageCallback | CallbackData],
            action_callback_data_type: type[IActionWithTodoItemAndTodoItemCallback | CallbackData],
            done: bool
    ) -> None:
        self.back_callback_data_type = back_callback_data_type
        self.action_callback_data_type = action_callback_data_type
        self.done = done

    def build_keyboard(
        self,
        page: int,
        todo_id: Optional[int] = None,
    ) -> InlineKeyboardMarkup:
            
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=get_mark_done_button_text() if not self.done else get_delete_done_item_button_text(),
                    callback_data=self.action_callback_data_type(todo_id=todo_id, page=page).pack()
                )
            ],
            [
                InlineKeyboardButton(
                    text=get_back_to_list_button_text(),
                    callback_data=self.back_callback_data_type(page=page).pack()
                )
            ]
        ])
