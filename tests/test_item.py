

from src.item import Item

def test_calculate_total_price():
    item = Item("Телефон", 10000, 5)
    assert item.calculate_total_price() == 50000

def test_apply_discount():
    item = Item("Телефон", 10000, 5)
    item.apply_discount(0.2)  # 20% discount
    assert item.price == 8000

def test_all_items():
    Item.all_items.clear()  # Очищаем список перед тестом

    item1 = Item("Телефон", 10000, 5)
    item2 = Item("Ноутбук", 20000, 3)
    assert len(Item.all_items) == 2
    assert item1 in Item.all_items
    assert item2 in Item.all_items
