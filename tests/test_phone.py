from src.phone import Phone
from src.item import Item

def test_phone_inheritance():
    phone = Phone("iPhone 14", 120_000, 5, 2, 2)
    assert isinstance(phone, Item)
    assert isinstance(phone, Phone)

def test_phone_repr_str():
    phone = Phone("iPhone 14", 120_000, 5, 2, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2, 2)"
    assert str(phone) == "iPhone 14"

def test_phone_add_item():
    phone = Phone("iPhone 14", 120_000, 5, 2, 2)
    item = Item("Телефон", 10000, 5, 1)
    assert phone + item == 3

def test_phone_add_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2, 2)
    phone2 = Phone("Samsung Galaxy", 100_000, 5, 1, 1)
    assert phone1 + phone2 == 3

def test_phone_add_invalid():
    phone = Phone("iPhone 14", 120_000, 5, 2, 2)
    invalid_obj = object()
    try:
        phone + invalid_obj
    except TypeError as e:
        assert str(e) == "Нельзя сложить экземпляры разных классов."
