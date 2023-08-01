# tests/test_item.py
from src.item import Item

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    item = Item("Смартфон", 10000, 1)

    item.apply_discount()
    assert item.price == 10000  # Без скидки, так как уровень цен пока равен 1.0

    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000  # Применили скидку, новый уровень цен равен 0.8
