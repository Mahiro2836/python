def initialize_inventory():
    inventory = {
        "1": {"name": "Laptop", "category": "Electronics", "price": 1200, "quantity": 50},
        "2": {"name": "T-Shirt", "category": "Clothing", "price": 25, "quantity": 200},
        "3": {"name": "Book", "category": "Books", "price": 15, "quantity": 100},
        "4": {"name": "Keyboard", "category": "Electronics", "price": 75, "quantity": 75},
         "5": {"name": "Jeans", "category": "Clothing", "price": 60, "quantity": 150},
    }
    categories = set(item["category"] for item in inventory.values())
    return inventory, categories

def add_product(inventory, categories, product_id, name, category, price, quantity):
    if product_id in inventory:
        inventory[product_id]["quantity"] += quantity
        print(f"Товар {product_id} обновлен, добавлено {quantity} шт. Всего: {inventory[product_id]['quantity']}")
    else:
        inventory[product_id] = {"name": name, "category": category, "price": price, "quantity": quantity}
        categories.add(category)
        print(f"Товар {product_id} добавлен.")

def remove_product(inventory, product_id):
    if product_id in inventory:
        del inventory[product_id]
        print(f"Товар {product_id} удален.")
    else:
        print(f"Ошибка: Товар с product_id {product_id} не найден.")

def update_quantity(inventory, product_id, quantity):
    if product_id in inventory:
        if quantity > 0:
            inventory[product_id]["quantity"] = quantity
            print(f"Количество товара {product_id} обновлено до {quantity}.")
        else:
            remove_product(inventory, product_id)
    else:
        print(f"Ошибка: Товар с product_id {product_id} не найден.")

def get_unique_categories(categories):
    return categories

def find_products_by_category(inventory, category):
    return [item for item in inventory.values() if item["category"] == category]

if __name__ == "__main__":
    inventory, categories = initialize_inventory()

    print("Начальный инвентарь:")
    for product_id, product in inventory.items():
        print(f"ID: {product_id}, Название: {product['name']}, Категория: {product['category']}, Цена: {product['price']}, Количество: {product['quantity']}")
    print("\n")
    
    print("Уникальные категории:", get_unique_categories(categories))
    print("\n")

    add_product(inventory, categories, "6", "Mouse", "Electronics", 20, 100)
    add_product(inventory, categories, "1", "Laptop", "Electronics", 1200, 20)

    print("\nИнвентарь после добавления товара:")
    for product_id, product in inventory.items():
        print(f"ID: {product_id}, Название: {product['name']}, Категория: {product['category']}, Цена: {product['price']}, Количество: {product['quantity']}")
    print("\n")
    print("Уникальные категории:", get_unique_categories(categories))
    print("\n")


    update_quantity(inventory, "2", 150)
    update_quantity(inventory, "3", 0)
    update_quantity(inventory, "7", 100)

    print("\nИнвентарь после обновления количества:")
    for product_id, product in inventory.items():
        print(f"ID: {product_id}, Название: {product['name']}, Категория: {product['category']}, Цена: {product['price']}, Количество: {product['quantity']}")
    print("\n")


    remove_product(inventory, "4")
    remove_product(inventory, "8")

    print("\nИнвентарь после удаления товара:")
    for product_id, product in inventory.items():
         print(f"ID: {product_id}, Название: {product['name']}, Категория: {product['category']}, Цена: {product['price']}, Количество: {product['quantity']}")
    print("\n")

    print("Уникальные категории:", get_unique_categories(categories))
    print("\n")

    electronic_products = find_products_by_category(inventory, "Electronics")
    print("Товары категории 'Electronics':")
    for item in electronic_products:
        print(f"Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")

    books_products = find_products_by_category(inventory, "Books")
    print("\nТовары категории 'Books':")
    for item in books_products:
        print(f"Название: {item['name']}, Цена: {item['price']}, Количество: {item['quantity']}")