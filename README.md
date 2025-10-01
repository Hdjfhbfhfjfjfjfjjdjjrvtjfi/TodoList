## Telegram Todo Bot (aiogram + Tortoise ORM)

### Требования
- Python 3.10+
- Зависимости из `requirements.txt`

### Установка
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Переменные окружения
Задайте токен бота:
```powershell
$env:BOT_TOKEN = "<TELEGRAM_BOT_TOKEN>"
```

### Запуск
```bash
python -m tg_bot.main
```

### Команды
- `/start` — помощь
- `/add <текст>` — добавить задачу
- `/list` — показать задачи
- `/done <id>` — отметить выполненной
- `/undone <id>` — вернуть в работу
- `/delete <id>` — удалить задачу

Данные сохраняются в SQLite (`db.sqlite3`) с использованием `tortoise-orm`.


