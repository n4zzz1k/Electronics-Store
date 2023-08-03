class Item:
    pay_rate = 1.2
    all_items = []

    def __init__(self, name, price, discount, quantity):
        self._name = name
        self._price = price
        self.discount = discount
        self.quantity = quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self._name = value[:10]
            print("Длина наименования товара превышает 10 символов.")
        else:
            self._name = value

    @property
    def price(self):
        return self._price

    def calculate_total_price(self):
        return self.price * self.pay_rate

    def apply_discount(self, discount):
        self._price = self.price * (1 - discount)

    @classmethod
    def instantiate_from_csv(cls):
        import os
        import csv
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file_path = os.path.join(base_dir, 'items.csv')
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                discount = cls.string_to_number(row['discount'])
                quantity = cls.string_to_number(row['quantity'])
                item = cls(name, price, discount, quantity)
                cls.all_items.append(item)

    @staticmethod
    def string_to_number(value):
        return int(float(value))

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.discount}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя сложить экземпляры разных классов.")
