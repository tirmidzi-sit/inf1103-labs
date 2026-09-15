# Inventory Auditor

inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity or 'quit': ")

    if stock.lower() == "quit":
        break

    elif stock.startswith("-") and stock[1:].isdigit():
        print("Error: Negative numbers are not allowed.")
        failed_entries += 1

    elif stock.isdigit():
        quantity = int(stock)
        inventory += quantity
        print("Current inventory:", inventory)

        if inventory > 500:
            print("ALERT: Overstock!")
            break
        
    else:
        print("Error: Invalid input.")
        failed_entries += 1

print("\n===== Inventory Report =====")
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)