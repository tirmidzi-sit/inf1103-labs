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

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("\n===== Inventory Report =====")
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

inventory = 0
failed_entries = 0
deliveries_processed = 0

while True:
    stock = get_valid_input()

    if stock == "quit":
        break

    elif stock is None:
        failed_entries += 1

    else:
        inventory = process_delivery(inventory, stock)
        tax = calculate_tax(stock)
        deliveries_processed += 1
        print("Current inventory:", inventory)
        print("Tax for this delivery:", tax)

        if inventory > 500:
            print("ALERT: Overstock!")
            break

generate_report(deliveries_processed, failed_entries)