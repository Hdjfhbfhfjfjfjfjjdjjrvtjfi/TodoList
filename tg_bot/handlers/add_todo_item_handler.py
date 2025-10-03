__all__ = ["router"]
from aiogram import Bot
from aiogram.dispatcher.router import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from tg_bot.states import AddTodoItemFSM
from tg_bot.filters import AddTodoItemCallback
from tg_bot.utils import get_get_todo_item_description_text, get_start_menu_text
from tg_bot.models import Todo
from tg_bot.keyboards import StartKeyboard


class AddTodoItemHandler:
    def __init__(self, add_todo_item_router: Router):
        self.router = add_todo_item_router
        self._register_handlers()

    def _register_handlers(self):
        self.router.callback_query.register(
            self.on_add_todo_item_handler, AddTodoItemCallback.filter()
        )
        self.router.message.register(
            self.get_text_handler, StateFilter(AddTodoItemFSM.get_text_of_todo_item)
        )

    async def on_add_todo_item_handler(self, callback: CallbackQuery, bot: Bot, state: FSMContext):
        await callback.message.delete()
        await state.set_data({
            "last_message": await bot.send_message(
                chat_id=callback.message.chat.id,
                text=get_get_todo_item_description_text()
            )
        })
        await state.set_state(AddTodoItemFSM.get_text_of_todo_item)
        await callback.answer()

    async def get_text_handler(self, message: Message, bot: Bot, state: FSMContext):
        await message.delete()
        last_message: Message = (await state.get_data())["last_message"]
        await Todo.create_from_fields_parameters(message.chat.id, message.text)
        await last_message.edit_text(
            text=get_start_menu_text(),
            reply_markup=StartKeyboard().build_keyboard()
        )
        await state.clear()

router: Router = Router()
AddTodoItemHandler(router)
