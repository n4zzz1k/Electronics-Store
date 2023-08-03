from src.keyboard_mixin import KeyboardMixin
from src.item_keyboard import ItemKeyboard

class Keyboard(KeyboardMixin, ItemKeyboard):
    def __init__(self, name, price, discount, quantity):
        # Вызываем конструктор родительских классов с нужными аргументами
        ItemKeyboard.__init__(self, name, price, discount, quantity)
        KeyboardMixin.__init__(self)

    def __repr__(self):
        # Используем атрибуты, которые были инициализированы в родительском классе
        return f"Keyboard('{self.name}', {self.price}, {self.discount}, {self.quantity})"
