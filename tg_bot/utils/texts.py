def get_start_menu_text() -> str:
    return "Главное меню. Выберите действие:"


def get_pending_tasks_text(total: int) -> str:
    return f"Невыполненные задачи (всего: {total})"


def get_task_not_found_text() -> str:
    return "Задача не найдена"


def get_todo_details_text(text: str, done: bool, created_str: str) -> str:
    status_icon = "✅" if done else "⬜"
    return (
        f"{status_icon} <b>Детали задачи</b>\n\n"
        f"<b>Текст:</b> {text}\n"
        f"<b>Создана:</b> {created_str}\n"
    )


def get_back_to_list_button_text() -> str:
    return "⬅ К списку"


def get_back_button_text() -> str:
    return "⬅ Назад"


def get_prev_page_button_text() -> str:
    return "◀"


def get_next_page_button_text() -> str:
    return "▶"


def get_page_button_text(page: int) -> str:
    return f"Стр. {page + 1}"


def get_pending_button_text() -> str:
    return "Невыполненные"


def get_done_button_text() -> str:
    return "Выполненные"


def get_add_button_text() -> str:
    return "Добавить"


def get_delete_done_button_text() -> str:
    return "Удалить выполненное"


def get_mark_done_button_text() -> str:
    return "✅ Выполнено"


def get_task_marked_done_text() -> str:
    return "✅ Задача отмечена как выполненная!"


def get_task_not_found_error_text() -> str:
    return "❌ Задача не найдена!"


def get_delete_done_item_button_text() -> str:
    return "🗑 Удалить"


def get_done_tasks_text(total: int) -> str:
    return f"Выполненные задачи (всего: {total})"


def get_task_deleted_text() -> str:
    return "🗑 Задача удалена!"