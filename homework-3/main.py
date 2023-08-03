from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 0.2, 1)
    assert repr(item1) == "Item('Смартфон', 10000, 0.2, 1)"
    assert str(item1) == 'Смартфон'

