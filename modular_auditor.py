# Inventory Auditor

def get_valid_input():
    stock = input("Enter stock quantity or 'quit': ")

    if stock.lower() == "quit":
        return "quit"

    elif stock.startswith("-") and stock[1:].isdigit():
        print("Error: Negative numbers are not allowed.")
        return None

    elif stock.isdigit():
        return int(stock)

    else:
        print("Error: Invalid input.")
        return None

inventory = 0
failed_entries = 0

while True:
    stock = get_valid_input()

    if stock == "quit":
        break

    elif stock is None:
        failed_entries += 1

    else:
        inventory += stock
        print("Current inventory:", inventory)

        if inventory > 500:
            print("ALERT: Overstock!")
            break
        
print("\n===== Inventory Report =====")
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)