# Inventory Auditor

inventory = 0

while True:
    stock = input("Enter stock quantity or 'quit': ")

    if stock.lower() == "quit":
        break

    quantity = int(stock)

    print("Stock quantity:", quantity)