# tests/test_item.py

from src.item import Item

def test_calculate_total_price():
    # Создаем экземпляры товаров
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    # Проверяем, что метод calculate_total_price возвращает правильное значение
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    # Создаем экземпляр товара
    item = Item("Смартфон", 10000, 20)

    # Проверяем, что метод apply_discount устанавливает правильную скидку
    item.apply_discount(0.2)  # 20% discount
    assert item.price == 8000.0

    item.apply_discount(0.1)  # 10% discount (applied to the discounted price)
    assert item.price == 7200.0

def test_instances_tracking():
    # Проверяем, что все созданные экземпляры класса Item отслеживаются в атрибуте класса all
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert len(Item.all) == 2
    assert item1 in Item.all
    assert item2 in Item.all

