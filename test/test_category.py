from src.category import Category
from src.product import Product


def test_category_initialization_with_products(category_with_products, sample_products):
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