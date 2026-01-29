from typing import List

import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


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


@pytest.fixture
def sample_smartphone_1():
    return Smartphone(
        "iPhone", "Смартфон Apple", 80000.0, 5,
        "Высокая", "15 Pro", 256, "Black"
    )


@pytest.fixture
def sample_smartphone_2():
    return Smartphone(
        "Samsung", "Смартфон Samsung", 60000.0, 3,
        "Средняя", "Galaxy S23", 128, "White"
    )


@pytest.fixture
def grass_1():
    return LawnGrass(
        "Универсальная", "Трава для газона", 500.0, 10,
        "Россия", "14 дней", "Зеленый"
    )


@pytest.fixture
def grass_2():
    return LawnGrass(
        "Элитная", "Трава премиум класса", 800.0, 5,
        "Германия", "10 дней", "Изумрудный"
    )
