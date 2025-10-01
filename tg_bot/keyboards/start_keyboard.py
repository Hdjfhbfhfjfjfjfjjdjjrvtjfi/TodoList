from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from typing import Optional, List

from tg_bot.filters.callback_data import (
    DonePageCallback,
    AddTaskCallback,
    DeleteDonePageCallback, PendingPageCallback,
)
from tg_bot.models import Todo
from tg_bot.utils import (
    get_pending_button_text,
    get_done_button_text,
    get_add_button_text,
    get_delete_done_button_text,
)
from tg_bot.utils.interfaces import KeyboardInterface


class StartKeyboard(KeyboardInterface):
    
    def __init__(self):
        super().__init__()
    
    def build_keyboard(
        self,
        page: int = 0,
        has_prev: bool = False,
        has_next: bool = False,
        todos: Optional[List[Todo]] = None,
        **kwargs
    ) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text=get_pending_button_text(), callback_data=PendingPageCallback(page=0).pack()),
                    InlineKeyboardButton(text=get_done_button_text(), callback_data=DonePageCallback(page=0).pack()),
                ],
                [
                    InlineKeyboardButton(text=get_add_button_text(), callback_data=AddTaskCallback().pack()),
                ],
            ]
        )


def build_start_keyboard() -> InlineKeyboardMarkup:
    keyboard = StartKeyboard()
    return keyboard.build_keyboard()


