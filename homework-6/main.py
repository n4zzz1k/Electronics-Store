# main.py
from src.item import Item, InstantiateCSVError

if __name__ == '__main__':
    try:
        Item.instantiate_from_csv()
        for item in Item.all_items:
            print(f"Item: {item.name}, Price: {item.price}")
    except InstantiateCSVError as e:
        print(f"Error: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
