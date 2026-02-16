from src.product import Product


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0

    def __str__(self):
        return (f"Название категории {self.name}, "
                f"количество продуктов: {Category.product_count} шт.")

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    def add_product(self, product):
        """Метод для добавления продукта в категорию"""
        if not isinstance(product, Product):
            raise TypeError(
                f"Можно добавлять только объекты типа Product или наследников."
                f"Получен: {type(product).__name__}"
            )

        if self.__products is None:
            self.__products = []

        self.__products.append(product)
        Category.product_count += 1

    def average_price(self):
        """
               Подсчитывает средний ценник всех товаров в категории.
               Если в категории нет товаров, возвращает 0.
               """
        try:
            if not self.__products or len(self.__products) == 0:
                return 0

            total_price = sum(product.price for product in self.__products)
            average = total_price / len(self.__products)
            return round(average, 2)

        except ZeroDivisionError:
            return 0
        except Exception as e:
            print(f"Ошибка при вычислении средней цены: {e}")
            return 0
