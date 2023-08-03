from src.item import Item

def test_calculate_total_price():
    item = Item("Телефон", 10000, 5, 1)
    assert item.calculate_total_price() == 12000

def test_apply_discount():
    item = Item("Телефон", 10000, 5, 1)
    item.apply_discount(0.2)  # 20% скидка
    assert item.price == 8000

def test_name_length_limit():
    item = Item("Смартфон", 10000, 5, 1)
    assert item.name == "Смартфон"

    item.name = "СуперСмартфон"
    assert item.name == "СуперСмарт"

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all_items) == 5

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
