

def test_smartphone_init(sample_smartphone_1):
    assert sample_smartphone_1.name == "iPhone"
    assert sample_smartphone_1.efficiency == "Высокая"


def test_add_same_class_products(sample_smartphone_1, sample_smartphone_2):
    """Тест сложения товаров одного класса"""

    result = sample_smartphone_1 + sample_smartphone_2
    assert result == (80000.0 * 5) + (60000.0 * 3)


def test_add_different_class_products(sample_smartphone_1, grass_1):
    """Тест что нельзя складывать товары разных классов"""
    smartphone = sample_smartphone_1
    grass = grass_1
    result = smartphone + grass
    print(result)
    # with pytest.raises(TypeError) as exc_info:
    #     result = smartphone + grass
