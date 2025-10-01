from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from typing import List, Optional

from tg_bot.filters.callback_data import DonePageCallback, DoneItemCallback, BackToStartCallback
from tg_bot.models import Todo
from tg_bot.utils import (
    get_prev_page_button_text,
    get_next_page_button_text,
    get_page_button_text,
    get_back_button_text,
)
from tg_bot.utils.interfaces import KeyboardInterface


class DoneKeyboard(KeyboardInterface):
    
    def __init__(self):
        super().__init__()
    
    def build_keyboard(
        self,
        page: int,
        has_prev: bool,
        has_next: bool,
        todos: Optional[List[Todo]] = None,
        **kwargs
    ) -> InlineKeyboardMarkup:
        if todos is None:
            todos = []
            
        buttons = []

        for todo in todos:
            buttons.append([InlineKeyboardButton(
                text=f"✅ {todo.text[:50]}{'...' if len(todo.text) > 50 else ''}",
                callback_data=DoneItemCallback(todo_id=todo.id, page=page).pack()
            )])

        nav_buttons = []
        if has_prev:
            nav_buttons.append(InlineKeyboardButton(
                text=get_prev_page_button_text(),
                callback_data=DonePageCallback(page=page - 1).pack()
            ))
        
        nav_buttons.append(InlineKeyboardButton(
            text=get_page_button_text(page),
            callback_data=DonePageCallback(page=page).pack()
        ))
        
        if has_next:
            nav_buttons.append(InlineKeyboardButton(
                text=get_next_page_button_text(),
                callback_data=DonePageCallback(page=page + 1).pack()
            ))
        
        if nav_buttons:
            buttons.append(nav_buttons)

        buttons.append([InlineKeyboardButton(
            text=get_back_button_text(),
            callback_data=BackToStartCallback().pack()
        )])
        
        return InlineKeyboardMarkup(inline_keyboard=buttons)


def build_done_keyboard(page: int, has_prev: bool, has_next: bool, todos: list) -> InlineKeyboardMarkup:
    keyboard = DoneKeyboard()
    return keyboard.build_keyboard(page, has_prev, has_next, todos)
