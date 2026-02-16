from src.category import Category
from src.product import Product


def test_category_initialization_with_products(category_with_products,
                                               sample_products):
    """Тест создания категории с продуктами"""
    category = category_with_products

    assert category.name == "Electronics"
    assert category.description == "Electronic devices"
    assert isinstance(category.products, str)
    for product in sample_products:
        assert product.name in category.products
        assert str(product.price) in category.products
        assert str(product.quantity) in category.products
    lines = category.products.strip().split('\n')
    assert len(lines) == 3
    assert str(category_with_products) == ("Название категории Electronics, "
                                           "количество продуктов: 3 шт.")


def test_add_product_basic():
    """Базовый тест add_product"""
    category = Category("Test", "Test", [])
    product = Product("New", "New product", 50.0, 10)

    # Добавляем продукт
    category.add_product(product)

    assert "New" in category.products
    assert "50.0" in category.products
    assert "10" in category.products

    result = category.products
    assert "New, 50.0 руб. Остаток: 10 шт." in result


def test_average_price_for_norm_products():
    """Тест средней цены для категории с несколькими продуктами"""

    products = [
        Product("Товар 1", "Описание 1", 100.0, 5),
        Product("Товар 2", "Описание 2", 200.0, 3),
        Product("Товар 3", "Описание 3", 300.0, 2),
        Product("Товар 4", "Описание 4", 400.0, 1),
    ]

    category = Category("Тестовая категория", "Описание", products)

    # Ожидаемая средняя цена: (100 + 200 + 300 + 400) / 4 = 250.0
    result = category.average_price()

    assert result == 250.0
    assert isinstance(result, float)


def test_average_price_with_zero_prices():
    """Тест средней цены когда есть товары с нулевой ценой"""
    products = [
        Product("Бесплатный товар", "Акция", 0.0, 10),
        Product("Платный товар", "Обычный", 100.0, 5),
        Product("Дорогой товар", "Премиум", 500.0, 2),
    ]

    category = Category("Смешанные цены", "Есть бесплатные товары", products)

    # Ожидаемая средняя цена: (0 + 100 + 500) / 3 = 200.0
    result = category.average_price()

    assert result == 200.0

