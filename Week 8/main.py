
import json
import os
from product import Product
from inventory import Inventory


def load_inventory():
    inventory = Inventory()

    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            products = json.load(file)

        for item in products:
            product = Product(
                item["id"],
                item["name"],
                item["price"],
                item["stock"]
            )
            inventory.add_product(product)

        print("Inventory loaded successfully.")
    else:
        print("inventory.json not found. Starting with empty inventory.")

    return inventory


def save_inventory(inventory):
    products = []

    for product in inventory.get_all_products():
        products.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(products, file, indent=4)

    print("Inventory saved successfully.")


def add_product(inventory):
    product_id = input("Enter Product ID: ").strip()
    name = input("Enter Product Name: ").strip()

    if not product_id or not name:
        print("Product ID and name cannot be empty.")
        return

    try:
        price = float(input("Enter Product Price: "))
        stock = int(input("Enter Stock Quantity: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative.")
            return

    except ValueError:
        print("Invalid input. Enter a valid price and whole-number stock.")
        return

    product = Product(product_id, name, price, stock)
    inventory.add_product(product)


def update_stock(inventory):
    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)

    if product is not None:
        try:
            new_stock = int(input("Enter New Stock Quantity: "))

            if new_stock < 0:
                print("Stock cannot be negative.")
                return

            product.update_stock(new_stock)

        except ValueError:
            print("Invalid stock quantity. Please enter a whole number.")
    else:
        print("Product not found.")


def search_product(inventory):
    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)

    if product is not None:
        product.display_information()
    else:
        print("Product not found.")


def menu():
    inventory = load_inventory()

    while True:
        print("\n===== Inventory Management System =====")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            add_product(inventory)

        elif choice == "3":
            update_stock(inventory)

        elif choice == "4":
            search_product(inventory)

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            save_inventory(inventory)
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
