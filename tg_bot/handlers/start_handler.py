__all__ = [
    "router"
]
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from tg_bot.filters.callback_data import BackToStartCallback
from tg_bot.keyboards import StartKeyboard
from tg_bot.utils import get_start_menu_text


class StartHandler:
    
    def __init__(self, start_router: Router):
        self.router = start_router
        self._register_handlers()
    
    def _register_handlers(self) -> None:
        self.router.message.register(
            self._on_start, Command("start")
        )
        self.router.callback_query.register(
            self._on_back_to_start, BackToStartCallback.filter()
        )

    async def _on_start(self, message: Message) -> None:
        await message.answer(
            get_start_menu_text(),
            reply_markup=StartKeyboard().build_keyboard(),
        )
        await message.delete()

    async def _on_back_to_start(self, callback: CallbackQuery) -> None:
        await callback.message.edit_text(get_start_menu_text())
        await callback.message.edit_reply_markup(reply_markup=StartKeyboard().build_keyboard())
        await callback.answer()


router = Router()
StartHandler(router)


