def get_start_menu_text() -> str:
    """Get start menu message text."""
    return "Главное меню. Выберите действие:"


def get_pending_tasks_text(total: int) -> str:
    """Get pending tasks list text."""
    return f"Невыполненные задачи (всего: {total})"


def get_task_not_found_text() -> str:
    """Get task not found error text."""
    return "Задача не найдена"


def get_todo_details_text(text: str, done: bool, created_str: str) -> str:
    """Get todo item details text."""
    status_icon = "✅" if done else "⬜"
    return (
        f"{status_icon} <b>Детали задачи</b>\n\n"
        f"<b>Текст:</b> {text}\n"
        f"<b>Создана:</b> {created_str}\n"
    )


def get_back_to_list_button_text() -> str:
    """Get back to list button text."""
    return "⬅ К списку"


def get_back_button_text() -> str:
    """Get back button text."""
    return "⬅ Назад"


def get_prev_page_button_text() -> str:
    """Get previous page button text."""
    return "◀"


def get_next_page_button_text() -> str:
    """Get next page button text."""
    return "▶"


def get_page_button_text(page: int) -> str:
    """Get page indicator button text."""
    return f"Стр. {page + 1}"


def get_pending_button_text() -> str:
    """Get pending tasks button text."""
    return "Невыполненные"


def get_done_button_text() -> str:
    """Get done tasks button text."""
    return "Выполненные"


def get_add_button_text() -> str:
    """Get add task button text."""
    return "Добавить"


def get_delete_done_button_text() -> str:
    """Get delete done tasks button text."""
    return "Удалить выполненное"


def get_mark_done_button_text() -> str:
    """Get mark as done button text."""
    return "✅ Выполнено"


def get_task_marked_done_text() -> str:
    """Get task marked as done success message."""
    return "✅ Задача отмечена как выполненная!"


def get_task_not_found_error_text() -> str:
    """Get task not found error message."""
    return "❌ Задача не найдена!"


def get_delete_done_item_button_text() -> str:
    """Get delete done item button text."""
    return "🗑 Удалить"


def get_done_tasks_text(total: int) -> str:
    """Get done tasks list text."""
    return f"Выполненные задачи (всего: {total})"


def get_task_deleted_text() -> str:
    """Get task deleted success message."""
    return "🗑 Задача удалена!"