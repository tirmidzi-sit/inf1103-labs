
from product import Product


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        for existing_product in self.__products:
            if existing_product.get_product_id() == product.get_product_id():
                print("Product ID already exists.")
                return False

        self.__products.append(product)
        print("Product added successfully.")
        return True

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def display_all(self):
        print("\nCurrent Inventory")
        print("----------------------------------------")

        if not self.__products:
            print("No products in inventory.")

        for product in self.__products:
            print(
                f"ID: {product.get_product_id()} | "
                f"{product.to_dict()['name']} | "
                f"Stock: {product.get_stock()} | "
                f"Price: ${product.to_dict()['price']:.2f}"
            )

        print("----------------------------------------")

    def get_all_products(self):
        return self.__products
