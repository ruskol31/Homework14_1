class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
