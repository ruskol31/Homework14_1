from src.product import Product


class Smartphone(Product):
    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color, inventory=0):
        super().__init__(name, description, price, quantity, inventory)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):

        return self.inventory + other.inventory

print(Smartphone.__mro__)