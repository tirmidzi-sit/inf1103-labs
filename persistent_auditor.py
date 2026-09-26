def load_inventory():
    inventory = []

    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line:
                    parts = line.split(",")

                    order_id = parts[0]
                    product_name = parts[1]
                    quantity = parts[2]

                    inventory.append((order_id, product_name, quantity))

    except FileNotFoundError:
        pass

    return inventory


def save_inventory(inventory):
    with open("inventory.txt", "w") as file:
        for order in inventory:
            file.write(f"{order[0]},{order[1]},{order[2]}\n")


inventory = load_inventory()

print("Current Orders:")
print()

for order in inventory:
    print(f"{order[0]}, {order[1]}, {order[2]}")

while True:
    print()

    product_name = input("Enter Product Name (or quit): ")

    if product_name.lower() == "quit":
        save_inventory(inventory)
        print()
        print("Orders successfully saved to inventory.txt")
        break

    while True:
        quantity = input("Enter Quantity: ")

        if quantity.isdigit() and int(quantity) > 0:
            break

        print("Invalid quantity. Please enter a positive number.")

    if inventory:
        last_id = int(inventory[-1][0])
        new_id = last_id + 1
    else:
        new_id = 1001

    new_order = (str(new_id), product_name, quantity)
    inventory.append(new_order)

    print()
    print("New Order Added:")
    print()
    print(f"{new_order[0]},{new_order[1]},{new_order[2]}")