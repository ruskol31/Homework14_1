from src.base_product import BaseProduct
from src.printmixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int
    inventory: int

    def __init__(self, name, description, price, quantity, inventory=0):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.inventory = price * quantity
        # super().__init__(**kwargs)
        BaseProduct.__init__(self)
        PrintMixin.__init__(self)

    def __str__(self):
        return (f"Название продукта {self.name}, {self.__price} руб. "
                f"Остаток: {self.quantity} шт.")

    def __add__(self, other):
        if type(self) is type(other):
            return self.inventory + other.inventory
        raise TypeError(f"Нельзя складывать {type(self).__name__} "
                        f"с {type(other).__name__}")

    @classmethod
    def new_product(cls, product_data: dict):
        """класс-метод принимет на вход параметры товара в словаре
        и возвращает созданный объект класса"""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )

    @property
    def price(self):
        """Геттер для получения цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Сеттер для установки цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
