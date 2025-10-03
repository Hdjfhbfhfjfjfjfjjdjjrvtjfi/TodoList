__all__ =[
    "AddTodoItemFSM"
]
from aiogram.filters.state import State, StatesGroup


class AddTodoItemFSM(StatesGroup):
    get_text_of_todo_item = State()