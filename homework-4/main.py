from src.item import Item
from src.phone import Phone

if __name__ == '__main__':
    # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
    phone1 = Phone("iPhone 14", 120_000, 5, 5, 2)
    print(phone1)               # Вывод: Phone('iPhone 14', 120000, 5, 5, 2)
    print(str(phone1))          # Вывод: iPhone 14
    print(repr(phone1))         # Вывод: Phone('iPhone 14', 120000, 5, 5, 2)
    print(phone1.number_of_sim) # Вывод: 2

    item1 = Item("Смартфон", 10000, 20, 1)
    print(item1.calculate_total_price()) # Вывод: 12000.0

    print(item1 + phone1)     # Вывод: 25

    phone1.number_of_sim = 0
    print(phone1.number_of_sim) # Вывод: 0
