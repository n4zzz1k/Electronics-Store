
class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def apply_discount(self):
        self.price *= self.pay_rate

    def calculate_total_price(self):
        return self.price * self.quantity
