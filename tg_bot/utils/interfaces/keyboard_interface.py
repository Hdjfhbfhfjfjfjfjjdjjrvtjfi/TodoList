from abc import ABC, abstractmethod
from typing import List, Optional
from aiogram.types import InlineKeyboardMarkup

from tg_bot.models import Todo


class FlippingKeyboardInterface(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def build_keyboard(
        self,
        page: int,
        has_prev: bool,
        has_next: bool,
        todos: Optional[List[Todo]] = None,
        **kwargs
    ) -> InlineKeyboardMarkup:
        pass
