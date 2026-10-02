import json
import os


inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
]


def load_inventory():
    global inventory

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("Inventory loaded successfully.")
    else:
        print("inventory.json not found.")
        inventory = []


def save_inventory():
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)

    print("Inventory saved successfully.")


def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Stock Quantity: "))

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)

    print("Product added successfully.")


def update_stock():
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            new_stock = int(input("Enter New Stock Quantity: "))
            product["stock"] = new_stock

            print("Stock updated successfully.")
            return

    print("Product not found.")


def search_product():
    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found")
            print("----------------------------------------")
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("----------------------------------------")
            return

    print("Product not found.")


def display_all():
    print("\nCurrent Inventory")
    print("----------------------------------------")

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("----------------------------------------")


def menu():
    while True:
        print("\n===== Inventory Management System =====")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_all()

        elif choice == "2":
            add_product()

        elif choice == "3":
            update_stock()

        elif choice == "4":
            search_product()

        elif choice == "5":
            save_inventory()

        elif choice == "6":
            save_inventory()
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


load_inventory()
menu()
