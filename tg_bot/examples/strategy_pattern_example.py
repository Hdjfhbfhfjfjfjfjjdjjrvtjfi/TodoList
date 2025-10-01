"""
Пример использования паттерна стратегия с клавиатурами.
Демонстрирует, как все классы клавиатур наследуют общий интерфейс KeyboardInterface.
"""

from tg_bot.utils.interfaces import KeyboardInterface
from tg_bot.utils.keyboard_factory import KeyboardFactory
from tg_bot.keyboards import (
    StartKeyboard,
    PendingKeyboard,
    DoneKeyboard,
    PendingItemKeyboard,
    DoneItemKeyboard,
)


def demonstrate_strategy_pattern():
    """Демонстрация паттерна стратегия с клавиатурами."""
    
    print("=== Демонстрация паттерна стратегия для клавиатур ===\n")
    
    # 1. Создание клавиатур через фабрику
    print("1. Создание клавиатур через фабрику:")
    keyboard_types = ['start', 'pending', 'done', 'todo_item', 'done_item']
    
    keyboards = []
    for keyboard_type in keyboard_types:
        keyboard = KeyboardFactory.create_keyboard(keyboard_type)
        keyboards.append(keyboard)
        print(f"   - Создана клавиатура: {type(keyboard).__name__}")
    
    print()
    
    # 2. Демонстрация единого интерфейса
    print("2. Демонстрация единого интерфейса KeyboardInterface:")
    for keyboard in keyboards:
        print(f"   - {type(keyboard).__name__} наследует KeyboardInterface: {isinstance(keyboard, KeyboardInterface)}")
    
    print()
    
    # 3. Использование полиморфизма
    print("3. Использование полиморфизма - все клавиатуры имеют метод build_keyboard():")
    for keyboard in keyboards:
        try:
            # Все клавиатуры имеют одинаковый интерфейс
            markup = keyboard.build_keyboard(
                page=0,
                has_prev=False,
                has_next=False,
                todos=None
            )
            print(f"   - {type(keyboard).__name__}: успешно создана клавиатура")
        except Exception as e:
            print(f"   - {type(keyboard).__name__}: ошибка - {e}")
    
    print()
    
    # 4. Демонстрация замены стратегий во время выполнения
    print("4. Демонстрация замены стратегий во время выполнения:")
    
    # Создаем контекст, который может использовать разные стратегии
    class KeyboardContext:
        def __init__(self, keyboard: KeyboardInterface):
            self.keyboard = keyboard
        
        def set_keyboard(self, keyboard: KeyboardInterface):
            """Замена стратегии во время выполнения."""
            self.keyboard = keyboard
        
        def create_markup(self, **kwargs):
            """Создание клавиатуры с текущей стратегией."""
            return self.keyboard.build_keyboard(**kwargs)
    
    # Создаем контекст с начальной стратегией
    context = KeyboardContext(StartKeyboard())
    print("   - Начальная стратегия: StartKeyboard")
    
    # Заменяем стратегию на PendingKeyboard
    context.set_keyboard(PendingKeyboard())
    print("   - Заменена на: PendingKeyboard")
    
    # Заменяем стратегию на DoneKeyboard
    context.set_keyboard(DoneKeyboard())
    print("   - Заменена на: DoneKeyboard")
    
    print()
    
    # 5. Демонстрация регистрации новых стратегий
    print("5. Демонстрация регистрации новых стратегий:")
    
    # Создаем новую стратегию клавиатуры
    class CustomKeyboard(KeyboardInterface):
        def __init__(self):
            super().__init__()
        
        def build_keyboard(self, page: int, has_prev: bool, has_next: bool, todos=None, **kwargs):
            from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
            return InlineKeyboardMarkup(inline_keyboard=[[
                InlineKeyboardButton(text="Custom Button", callback_data="custom_action")
            ]])
    
    # Регистрируем новую стратегию
    KeyboardFactory.register_keyboard('custom', CustomKeyboard)
    print("   - Зарегистрирована новая стратегия: CustomKeyboard")
    
    # Создаем экземпляр новой стратегии
    custom_keyboard = KeyboardFactory.create_keyboard('custom')
    print(f"   - Создан экземпляр: {type(custom_keyboard).__name__}")
    
    print()
    print("=== Паттерн стратегия успешно реализован! ===")


if __name__ == "__main__":
    demonstrate_strategy_pattern()
