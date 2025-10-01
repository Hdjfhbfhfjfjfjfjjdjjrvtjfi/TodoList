__all__ = [
    "Todo"
]
from tortoise import fields
from tortoise.models import Model


class Todo(Model):
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField(index=True)
    text = fields.CharField(max_length=512)
    done = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "todos"
