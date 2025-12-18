from typing import List

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_product():
    """Фикстура для создания тестового продукта"""
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_products() -> List[Product]:
    """Фикстура для создания списка тестовых продуктов"""
    return [
        Product("Product 1", "Description 1", 50.0, 5),
        Product("Product 2", "Description 2", 75.0, 8),
        Product("Product 3", "Description 3", 120.0, 3),
    ]


@pytest.fixture
def category_with_products(sample_products) -> Category:
    """Фикстура для создания категории с продуктами"""
    return Category("Electronics", "Electronic devices", sample_products)
