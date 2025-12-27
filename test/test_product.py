from src.product import Product


def test_product_with_fixture(sample_product):
    """Тест с использованием фикстуры"""
    assert sample_product.name == "Test Product"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


def test_product_creation():
    """тест создания продукта"""
    product = Product("Laptop", "Gaming laptop", 1500.0, 5)

    assert product.name == "Laptop"
    assert product.description == "Gaming laptop"
    assert product.price == 1500.0
    assert product.quantity == 5


def test_price_getter():
    """Тест получения цены"""
    product = Product("Phone", "Smartphone", 500.0, 10)

    assert product.price == 500.0
    assert isinstance(product.price, float)


def test_price_setter_valid():
    """Тест установки корректной цены"""
    product = Product("Test", "Test", 100.0, 5)

    product.price = 200.0
    assert product.price == 200.0
