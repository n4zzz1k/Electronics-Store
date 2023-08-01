from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 0.2, 1)
    item2 = Item("Ноутбук", 20000, 0.05, 1)

    print(item1.calculate_total_price())  # 12000.0
    print(item2.calculate_total_price())  # 21000.0

    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount(0.2)

    print(item1.price)  # 8000.0
    print(item2.price)  # 21000.0

    print(Item.all_items)  # [<src.item.Item object at 0x000001EC6250C690>, <src.item.Item object at 0x000001EC6250C6D0>]
