class ItemKeyboard:
    def __init__(self, name, price, discount, quantity):
        self.name = name
        self.price = price
        self.discount = discount
        self.quantity = quantity

    def __str__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.discount}, {self.quantity})"
