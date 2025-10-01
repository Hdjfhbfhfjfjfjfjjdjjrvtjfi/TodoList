from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from typing import Optional, List

from tg_bot.filters.callback_data import DonePageCallback, DeleteDonePageCallback
from tg_bot.models import Todo
from tg_bot.utils import get_back_to_list_button_text, get_delete_done_item_button_text
from tg_bot.utils.interfaces import FlippingKeyboardInterface


class DoneItemFlippingKeyboard(FlippingKeyboardInterface):
    
    def __init__(self):
        super().__init__()
    
    def build_keyboard(
        self,
        page: int,
        has_prev: bool = False,
        has_next: bool = False,
        todos: Optional[List[Todo]] = None,
        todo_id: Optional[int] = None,
        **kwargs
    ) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=get_delete_done_item_button_text(),
                    callback_data=DeleteDonePageCallback(todo_id=todo_id, page=page).pack()
                )
            ],
            [
                InlineKeyboardButton(
                    text=get_back_to_list_button_text(),
                    callback_data=DonePageCallback(page=page).pack()
                )
            ]
        ])


def build_done_item_keyboard(todo_id: int, page: int) -> InlineKeyboardMarkup:
    keyboard = DoneItemFlippingKeyboard()
    return keyboard.build_keyboard(page=page, todo_id=todo_id)
