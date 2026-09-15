# Inventory Auditor

inventory = 0

while True:
    stock = input("Enter stock quantity or 'quit': ")

    if stock.lower() == "quit":
        break

    elif stock.startswith("-") and stock[1:].isdigit():
        print("Error: Negative numbers are not allowed.")

    elif stock.isdigit():
        quantity = int(stock)
        inventory += quantity
        print("Current inventory:", inventory)

        if inventory > 500:
            print("ALERT: Overstock!")
            break
        
    else:
        print("Error: Invalid input.")