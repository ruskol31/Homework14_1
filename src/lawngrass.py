from src.product import Product


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country,
                 germination_period, color, inventory=0):
        super().__init__(name, description, price, quantity, inventory)
        self.country = country
        self.germination_period = germination_period
        self.color = color
