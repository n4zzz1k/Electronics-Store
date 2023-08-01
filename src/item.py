# src/item.py
class Item:
    all_items = []  # Статическая переменная для хранения всех экземпляров класса

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all_items.append(self)  # Добавляем созданный экземпляр в список всех экземпляров

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self, discount):
        self.price = self.price * (1 - discount)

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name
