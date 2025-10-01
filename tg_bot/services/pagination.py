from typing import Tuple

from tg_bot.models import Todo


class PaginationService:
    def __init__(self, done: bool):
        self.done = done
    async def fetch_tasks_page(self, user_id: int, page: int, items_per_page: int) -> Tuple[list[Todo], int, bool, bool]:
        total = await Todo.filter(user_id=user_id, done=self.done).count()
        offset = max(page, 0) * items_per_page
        tasks = (
            await Todo.filter(user_id=user_id, done=self.done)
            .order_by("-id")
            .offset(offset)
            .limit(items_per_page)
            .all()
        )
        has_prev = page > 0
        has_next = offset + len(tasks) < total
        return tasks, total, has_prev, has_next
