__all__ = [
    "StartKeyboard"
]
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tg_bot.filters.callback_data import (
    DonePageCallback,
    AddTaskCallback,
    PendingPageCallback,
)
from tg_bot.utils import (
    get_pending_button_text,
    get_done_button_text,
    get_add_button_text,
)


class StartKeyboard:
    def build_keyboard(self) -> InlineKeyboardMarkup:
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
