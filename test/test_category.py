

def test_category_initialization_with_products(category_with_products, sample_products):
    """Тест создания категории с продуктами"""
    category = category_with_products

    assert category.name == "Electronics"
    assert category.description == "Electronic devices"
    assert category.products == sample_products
    assert len(category.products) == 3
