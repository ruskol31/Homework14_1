def test_product_with_fixture(sample_product):
    """Тест с использованием фикстуры"""
    assert sample_product.name == "Test Product"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10
