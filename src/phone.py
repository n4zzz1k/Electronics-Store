from src.item import Item

class Phone(Item):
    def __init__(self, name, price, discount, quantity, number_of_sim):
        super().__init__(name, price, discount, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.discount}, {self.quantity}, {self.number_of_sim})"
